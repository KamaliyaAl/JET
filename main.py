from argparse import ArgumentParser
from functions import *

if __name__ == "__main__":
    args = inpuut()

    type = args.type

    if type == "1":
        version()
    elif type == "2":
        newDirectory(args.nameOfFile)
    elif type == "3":
        listOfFiles()


