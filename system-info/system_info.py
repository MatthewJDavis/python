#!/usr/bin/python3
import platform

def system_info():

    system = platform.system()
    architecture = platform.machine()
    print('The system is: {}'.format(system))
    print('The architecture is: {}'.format(architecture))

def main():
    print('running main')

if __name__ == '__main__':
    system_info()