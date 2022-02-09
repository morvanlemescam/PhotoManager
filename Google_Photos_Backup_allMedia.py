import os
from Google import Create_Service
from datetime import datetime
import pandas as pd  # pip install pandas
import requests  # pip install requests

pd.set_option('display.max_columns', 100)
pd.set_option('display.max_rows', 150)
pd.set_option('display.max_colwidth', 150)
pd.set_option('display.width', 150)
pd.set_option('expand_frame_repr', True)

CLIENT_SECRET_FILE = 'morvan.secret.json'
API_NAME = 'photoslibrary'
API_VERSION = 'v1'
SCOPES = ['https://www.googleapis.com/auth/photoslibrary']
ROOT_PATH = 'output'


def create_dir_if_not_exists(path: str):
    if not os.path.exists(path):
        os.makedirs(path)


def download_file(url: str, destination_folder: str, file_name: str):
    response = requests.get(url)
    if response.status_code == 200:
        # print('Downloading file ', format(file_name), ' to ', destination_folder)
        with open(os.path.join(destination_folder, file_name), 'wb') as f:
            f.write(response.content)
            f.close()


###############
# MAIN SCRIPT #
###############


service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)
rootPath = os.path.abspath(ROOT_PATH)

oneMoreSearch: bool = True
myNextPageToken = None

totalNumberOfPhotos = 0

while oneMoreSearch:

    allMedia = service.mediaItems().list(pageToken=myNextPageToken).execute()

    totalMediaNumber = len(allMedia['mediaItems'])
    # print('This script will download', totalMediaNumber, 'photos in', rootPath)
    myNextPageToken = allMedia.get('nextPageToken', None)

    # print('[', myNextPageToken, ']')

    oneMoreSearch = (myNextPageToken is not None)

    counter = 0
    for photo in allMedia['mediaItems']:
        counter = counter + 1
        totalNumberOfPhotos = totalNumberOfPhotos + 1
        photoId = photo['id']
        photoFilename = photo['filename']
        photoDownloadUrl = photo['baseUrl'] + '=d'
        photoMetadata = photo['mediaMetadata']
        photoIsoDate = photoMetadata['creationTime']
        photoCreationDate = datetime.fromisoformat(photoIsoDate[:-1])

        # full path creation
        fullPath = os.path.join(rootPath, str(photoCreationDate.year), str(photoCreationDate.month))

        # create_dir_if_not_exists(fullPath)
        # download photos
        print('[', counter, '/', totalMediaNumber, '] Photo [', photoFilename, '] will be downloaded to ', fullPath)
        # download_file(photoDownloadUrl, fullPath, photoFilename)

print('Total number pf photos is', totalNumberOfPhotos)
