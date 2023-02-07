#
# from pathlib import Path
from tkinter import Tk, filedialog
from sys import argv, exc_info
from io import open, TextIOWrapper
from unidecode import unidecode

import Darwin.CharReplace as CharReplace


def getfiles():
    root = Tk()
    root.withdraw()
    input_file = filedialog.askopenfilename(
        parent=None, title="Please select a file")
    output_file = filedialog.asksaveasfilename(
        parent=None, title="Please provide output file name")
    root.destroy()
    return (input_file, output_file)


def splitHeader(s):
    r = [name[1:-1] for name in s.split(',')]
    return r


def parseRec(theRecord):
    f = theRecord.split(',')
    for s in f:
        print(s)
    print()


def readFile(thePath):
    theFile = open(thePath)
    doHeader = True
    rcdNbr = 0

    for rec in theFile:
        if doHeader:
            fieldNames = splitHeader(rec.strip())
            print(fieldNames)
            doHeader = False
        else:
            rcdNbr += 1
            print(rec[:80])
            parseRec(rec.strip())
            if rcdNbr > 3:
                break

    theFile.close()


def countChars(s):
    d = {}
    for c in s:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1
    return d


def main():
    #   thePath = "C:/Users/mhagerma/Desktop/AGC_GU@BL001.CSV"
    theFileName = argv[1]
    # theFileName = "P:/test data/export_20220829-190511_acct_1BvV7aFQA4XJoMjP_avtechmediausa.bkp"
    print(theFileName)
    f = open(theFileName, 'r', buffering=4096, encoding='UTF-8')
    try:
        content = f.read()
        print(len(content))
        pos = 0
        while pos > -1:
            pos = -1
    except:
        e = exc_info()
        print(e)

    s = input("Done?")


if __name__ == "__main__":
    main()
