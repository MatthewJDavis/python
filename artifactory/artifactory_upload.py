import requests, hashlib, os


def get_sha1(file):
    with open(file,"rb") as f:
        bytes = f.read() # read entire file as bytes
        sha1 = hashlib.sha1(bytes).hexdigest();
        return sha1


def upload_to_artifactory(sha1, file_location, url, upload_name, token):
    headers = {'X-JFrog-Art-Api': '{}'.format(token),
                'X-Checksum-Sha1': sha1}
    upload_location = '{}/{}'.format(url, upload_name)

    with open(file_location, 'rb') as f:
        r = requests.put(upload_location, data=f, headers=headers)
    return r.status_code

if __name__ == '__main__':
    print(__name__)