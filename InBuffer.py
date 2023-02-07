from filereader import read_data

class inBuffer():
  def __init__(self, input_file):
    self.infile = input_file
    self.end_of_file = False
    self.text = read_data(self.infile, "")
    self.current_length = len(self.text)
    self.next_char = 0


  def getChar(self):
    if self.next_char >= self.current_length:
      return ""
    ch = self.text[self.next_char]
    self.next_char += 1
    if not self.end_of_file:
      if self.next_char > (self.current_length - 4):
        self.shiftText()
    return ch

  def shiftText(self):
    self.text = read_data(self.infile, self.text[self.next_char:])
    self.current_length = len(self.text)
    self.next_char = 0

  def getDiagnostic(self):
    curr_char = self.next_char - 1
    first_char = curr_char - 16
    if first_char < 0:
      first_char = 0
    last_char = curr_char + 17
    if last_char > self.current_length:
      last_char = self.current_length
    return (f'{self.text[first_char:last_char]}[{curr_char-first_char}]')