from CharReplace import UADict

class FormatError(Exception):
  pass  

class State():
  WHITESPACE = {' ', '\t'}
  POSITIONS = ['start', 'progress', 'end']

  def __init__(self):
    self.position = 'start'
    self.quoted = False
    self.spaces = False

  def do_char(self, ch):
    rch = ''
    codepoint = ord(ch)
    try:
      print(f"{ch}({codepoint}) -> {UADict[codepoint]}")
      ch = UADict[codepoint]
    except:
      pass

# start of a field
    if self.position == 'start':
      if self.quoted:
        if self.spaces:
          if ch == '"':
            self.position = 'end'
            self.quoted = False
          if not (ch in State.WHITESPACE or ch == '\n'):
            rch = ch
            self.spaces = False
          return rch

    if self.position == 'start':
      if self.quoted:
        if not self.spaces:
          if ch == '"':
            self.position = 'end'
            self.quoted = False
          if not (ch in State.WHITESPACE or ch == '\n'):
            rch = ch
          return rch

    if self.position == 'start':
      if not self.quoted:
        if self.spaces:
          if ch == '"':
            raise FormatError()
          if not (ch in State.WHITESPACE):
            self.spaces = False
            rch = ch
          if not (ch in (',', '\n')):
            self.position = "progress"
          return rch

    if self.position == 'start':
      if not self.quoted:
        if not self.spaces:
          if ch in State.WHITESPACE:
            self.spaces = True
          else:
            rch = ch
          if ch == '"':
            self.quoted = True
          if not (ch in (',', '\n')):
            self.position = 'progress'
          return rch

# continuing a field
    if self.position == 'progress':
      if self.quoted:
        if self.spaces:
          if ch == '"':
            self.position = 'end'
            self.quoted = False
          if not (ch in State.WHITESPACE or ch == '\n'):
            rch = ch
            self.spaces = False
          return rch

    if self.position == 'progress':
      if self.quoted:
        if not self.spaces:
          if ch == '"':
            self.position = 'end'
            self.quoted = False
          if not (ch in State.WHITESPACE or ch == '\n'):
            rch = ch
          else:
            rch = ' '
          return rch

    if self.position == 'progress':
      if not self.quoted:
        if self.spaces:
          if ch == '"':
            raise FormatError()
          if ch in (',', '\n'):
            self.position = "start"
          if (ch in State.WHITESPACE):
            rch = ''
          else:
            rch = ch
            self.spaces = False
          return rch

    if self.position == 'progress':
      if not self.quoted:
        if not self.spaces:
          if ch == '"':
            raise FormatError()
          if ch in (',', '\n'):
            self.position = "start"
          if ch in State.WHITESPACE:
            rch = ' '
            self.spaces = True
          else:
            rch = ch
          return rch
          
# end of field, due to closing quote
    if self.position == 'end':
      if not self.quoted:
        if not self.spaces:
          if ch in (',', '\n'):
            self.position = "start"
          else:
            raise FormatError()
          rch = ch
          return rch

# situations that ought never happen
    raise FormatError