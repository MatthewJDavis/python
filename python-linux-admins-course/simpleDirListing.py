#!/usr/bin/python3
#List the file name and size of items in the current directory

import os

for file in os.listdir("."):
    info = os.stat(file)
    print("%-20s : size %d" % (file, info.st_size))