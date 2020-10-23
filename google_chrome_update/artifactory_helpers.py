import hashlib
import requests
from requests.exceptions import HTTPError

def get_sha1(file):
    """ get the sha1 of the msi to set in artifactory """
    with open(file,"rb") as msi:
        bytes = msi.read() # read entire file as bytes
        sha1 = hashlib.sha1(bytes).hexdigest()
        return sha1

def upload_to_artifactory(sha1, file_location, url, upload_name, token):
    """ upload the msi to artifactory and set the sha1 property """
    headers = {'X-JFrog-Art-Api': '{}'.format(token),
                'X-Checksum-Sha1': sha1}
    upload_location = '{}{}'.format(url, upload_name)
    print(f'Uploading to artifactory')
    with open(file_location, 'rb') as msi:
        try:
            response = requests.put(upload_location, data=msi, headers=headers)
            response.raise_for_status()
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')
    print(f'Uploaded latest chrome to {upload_location}')
    return response.status_code
