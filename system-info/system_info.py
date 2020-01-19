#!/usr/bin/python3
import platform, json

def system_info():

    info = {}
    info['system'] = platform.system()
    info['processor'] = platform.processor()
    info['system-name'] = platform.node()
    info['system-architecture'] = platform.architecture()
    info['system-distribution'] = platform.dist()
    info['system-python-version'] = platform.python_version()
    return json.dumps(info)

def main():
    print('running main')

if __name__ == '__main__':
    print(system_info())