
from tkinter import Tk, filedialog


def getfiles():
  root = Tk()
  root.withdraw()
  input_file = filedialog.askopenfilename(
    parent=None, title="Please select the input file")
  output_file = filedialog.asksaveasfilename(
    parent=root, title="Please provide output file name")
  root.destroy()
  return (input_file, output_file)


def open_file(in_file_name):
  in_file = open(in_file_name, 'r', encoding='utf-8-sig')
  return in_file


def read_data(in_file, in_str):
  return in_str + in_file.readline()
