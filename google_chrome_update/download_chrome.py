# Proof of concept to download google chrome 64 bit msi and latest version number. To upload to package management system.

import requests, os

# get latest version number
def get_version():
    versionUrl = 'https://omahaproxy.appspot.com/win'

    res = requests.get(versionUrl)
    res.raise_for_status()
    version = res.content.decode()

    return version

def get_chrome(directory):
    # download msi
    url = 'https://dl.google.com/tag/s/dl/chrome/install/googlechromestandaloneenterprise64.msi'


    res = requests.get(url)
    res.raise_for_status()
    file = open('{}/googlechrome.msi'.format(directory), 'wb')
    for chunk in res.iter_content(100000):
        file.write(chunk)

    file.close()


if __name__ == '__main__':
    print(get_version())

latest = get_version()
version = latest.replace('.', '-')
os.mkdir(version)

get_chrome(version)
