#!/usr/bin/python3
#check for files with no owners
import os

uidset = set()

for line in open("/etc/passwd"):
    split = line.split(":")
    uidset.add(int(split[2]))

testdir = "/home/matt"
for folder, dirs, files in os.walk(testdir):
    for file in files:
        path = folder + "/" + file
        try:
            attributes = os.stat(path)
        except FileNotFoundError:
            print(path + " not found")
            continue
        if attributes.st_uid not in uidset:
            print(path + " has no owner ")