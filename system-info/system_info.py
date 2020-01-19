#!/usr/bin/python3
import platform

def system_info():

    system = platform.system()
    print('The system is: {}'.format(system))

def main():
    print('running main')

if __name__ == '__main__':
    system_info()