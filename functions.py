from argparse import ArgumentParser
import sys
import os

def version ():
    print(sys.version)
def newDirectory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)
    else:
        print(f"Directory {directory} already exists")
def listOfFiles():
    print(os.listdir("./.."))
def inpuut():
    parser = ArgumentParser()
    parser.add_argument("-t", '--type')
    parser.add_argument("-n", '--nameOfFile')
    args = parser.parse_args()

    return args