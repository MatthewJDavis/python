import os
import requests
from requests.exceptions import HTTPError

def get_latest_version_number():
    """ Get the latest chrome version from omahaproxy website """
    version_url = 'https://omahaproxy.appspot.com/win'

    try:
        response = requests.get(version_url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    return response.content.decode()

def download_chrome_msi(directory):
    """ Download the latest chrome msi from google """
    url = 'https://dl.google.com/tag/s/dl/chrome/install/GoogleChromeStandaloneEnterprise64.msi'
    try:
        response = requests.get(url)
        response.raise_for_status()
    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')
    os.mkdir(directory)
    file = open('{}/GoogleChromeStandaloneEnterprise64.msi'.format(directory), 'wb')
    for chunk in response.iter_content(100000):
        file.write(chunk)
    file.close()
    print(f'Latest chrome downloaded to {directory}')

def remove_file(file_location):
    """ Remove the downloaded msi """
    os.remove(file_location)
    os.rmdir(file_location.rsplit('/', 1)[0])
    print(f'Downloaded msi has been removed')
