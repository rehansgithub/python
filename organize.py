import os
from pathlib import Path
SUBDIRECTORIES = {
    "DOCUMENTS": ['.pdf', '.rtf', 'txt'],
    "AUDIO": ['.m4a', '.m4b', 'mp3'],
    "VIDEOS": ['.mov', '.avi', '.mp4'],
    "IMAGES": ['.jpg', '.jpeg', '.png']
}

def pickDirectory(value):
    for category, suffixes in SUBDIRECTORIES.items():
        for suffix in suffixes:
            if suffix == value:
                return category
print(pickDirectory('.pdf'))

def organizeDirectory():
    for items in os.scandir():
        filePath = Path(item)
        filetype = filePath.suffix.lower()
        directory - pickDirectory(filetype)
