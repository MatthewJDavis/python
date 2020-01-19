#!/usr/bin/python3
import platform, json

def system_info():

    system = platform.system()
    architecture = platform.machine()
    print('The system is: {}'.format(system))
    print('The architecture is: {}'.format(architecture))
    print('Processor:{}'.format(platform.processor()))

    info = {}
    info['processor'] = platform.processor()
    info['system-name'] = platform.node()

    return json.dumps(info)

def main():
    print('running main')

if __name__ == '__main__':
    print(system_info())