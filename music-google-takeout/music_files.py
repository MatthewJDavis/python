# %%
#! /usr/bin/python
# Copy music zips from external HD to temp location then extract and move the MP3s.
# Music extract - extract zipped music files from google takeout.
# Update constant vars as required.
import os
import shutil
import zipfile

SOURCE_DIR = "/media/matt/My Passport/Music/play-music1"
DEST_DIR = "/tmp/music"
EXTRACTED_SOURCE = "/tmp/music/Takeout/Google Play Music/Tracks/"
EXTRACTED_DEST = "/tmp/music/library"


def extract_zip(zip_file, destination):
    """Extract zip files into path supplied in destination parameter argument value"""
    if zipfile.is_zipfile(zip_file):
        print(f"Extracting {zip_file}")
        zipped_file = zipfile.ZipFile(zip_file)
        zipped_file.extractall(path=destination)
        zipped_file.close()
    else:
        print(f"Not a zip file: {zip_file}")


if __name__ == "__main__":
    # Copy music files from harddrive to music
    # dir_exist in python 3.8+
    shutil.copytree(SOURCE_DIR, DEST_DIR, dirs_exist_ok=True)

    # Extract zip files
    for root, dirs, files in os.walk(DEST_DIR):
        print(f"Root path: {root}, Dirs: {dirs}, filenames: {files}")
        for file in files:
            print(os.path.join(root, file))
            extract_zip(os.path.join(root, file), DEST_DIR)

    # Move extracted files - only mp3s
    for root, dirs, files in os.walk(EXTRACTED_SOURCE):
        if os.path.isdir(EXTRACTED_DEST) is False:
            os.mkdir(EXTRACTED_DEST)
        for file in files:
            if file.endswith("mp3"):
                shutil.move(os.path.join(root, file), EXTRACTED_DEST)
