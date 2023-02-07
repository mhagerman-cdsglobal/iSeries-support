class outBuffer():
  def __init__(self):
    # create a "mutable string"
    self.char_array = [' ' for i in range(1024)]
    self.count = 0
    return

  def clear(self):
    for i in range(self.count):
      self.char_array[i] = ' '
    self.count = 0
    return

  def unload(self):
    outString = ''.join(self.char_array[:self.count])
    self.clear()
    return outString

  def append(self, s):
    for ch in s:
      self.char_array[self.count] = ch
      self.count += 1
    return self.count