#! /usr/bin/python3

import os

size = 0

for dirpath, dirnames, filenames in os.walk("."):
    print("Files in %s are: " % dirpath)
    for file in filenames:
        print("\t" + file)
        size += os.path.getsize(os.path.join(dirpath, file))
        print(size * 1024)
    
    print("Directories in %s are:" % dirpath)
    for dir in dirnames:
        print("\t" + dir)