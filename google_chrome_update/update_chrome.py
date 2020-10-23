from chrome_helpers import get_latest_version_number, download_chrome_msi, remove_file
from artifactory_helpers import get_sha1, upload_to_artifactory
import os

latest = get_latest_version_number()
directory_name = latest.replace('.','-')
upload_location = f"{directory_name}/GoogleChromeStandaloneEnterprise64.msi"
file_location = f"/tmp/{upload_location}"

token = os.getenv('TOKEN')
try:
  token != None
except:
  print('Token not found in environment')

url = 'https://artifactory.cd.je-labs.com/artifactory/static_content/google/chrome/'

download_chrome_msi(f"/tmp/{directory_name}")

sha1 = get_sha1(file_location)
print(f'sha1 value: {sha1}')

upload_to_artifactory(sha1=sha1, file_location=file_location, url=url, upload_name=upload_location, token=token)
remove_file(file_location=file_location)
