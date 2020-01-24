# Proof of concept to download google chrome 64 bit msi and latest version number. To upload to package management system.

import requests, os, hashlib

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


# code to upload to artifactory todo - functions

def get_sha1(file):
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        sha1 = hashlib.sha1(bytes).hexdigest();
        return sha1

token = os.environ['TOKEN']
sha1 = get_sha1('chrome.msi')

headers = {'X-JFrog-Art-Api': '{}'.format(token),
            'X-Checksum-Sha1': sha1}
upload_location = 'http://localhost/artifactory/generic-local/google/chrome/{}/{}'.format(version, 'chrome.msi')
file_location = '{}/googlechrome.msi'.format(version)

with open(file_location, 'rb') as f:
    requests.put(upload_location, data=f, headers=headers)

# todo checksum: https://stackoverflow.com/questions/46703183/fix-checksum-in-artifactory-when-uploading-file-through-rest-api/52067221

