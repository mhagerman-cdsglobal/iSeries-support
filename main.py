
from filereader import *
from InBuffer import *
from OutBuffer import *
from State import *


def main():
  input_file_name, output_file_name = getfiles()
# input_file_name = "Z:/DWN_PENSKE/Subscriber_Detail_2023-01-11T1912_QWCR3j.csv"
# output_file_name = "Z:/DWN_PENSKE/Subscriber_Detail_2023-01-11T1912_QWCR3j_mod.csv"
  print(input_file_name)
  print(output_file_name)

  in_file = open_file(input_file_name)
  out_file = open(output_file_name, 'w', encoding='utf-8-sig', newline = '')    

  inBuf = inBuffer(in_file)
  outBuf = outBuffer()
  state_machine = State()
  char_count = 0

  while ((ch := inBuf.getChar()) > ""):
    try:
      ch = state_machine.do_char(ch)
      char_count += 1
    except FormatError as e:
      print()
      print(f"Format error near character {char_count}.")
      print(inBuf.getDiagnostic())
      print()
      break
    outBufSize = outBuf.append(ch)
    if outBufSize > 1020:
      outString = outBuf.unload()
  #    print(outString, end=None)
      try:
        out_file.write(outString)
      except(UnicodeEncodeError):
        hex_string = '-'.join([hex(ord(ch))[2:] for ch in outString])
        print(hex_string)
        break
  if outBufSize > 0:
    outString = outBuf.unload()
  #  print(outString, end=None)
    out_file.write(outString)
  

if __name__ == "__main__":
  main()
