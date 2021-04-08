"""
arctictern.py
A little script that does a big migration
"""

import os
import requests
import shutil
import sys

BASE_URL = "https://raw.githubusercontent.com/Code-Institute-Org/gitpod-full-template/master/"

BACKUP = False

FILE_LIST = [{"filename": ".theia/settings.json",
              "url": ".vscode/settings.json"},
             {"filename": ".gitpod.yml",
              "url": ".gitpod.yml"
              },
             {"filename": ".gitpod.dockerfile",
              "url": ".gitpod.dockerfile"
              }]


def process(file, suffix):
    """
    Replaces and optionally backs up the files that
    need to be changed.
    Arguments: file - a path and filename
               suffix - the suffix to the BASE_URL
    """

    if BACKUP:
        shutil.copyfile(file, f"{file}.bak")

    with open(file, "wb") as f:
        r = requests.get(BASE_URL + suffix)
        f.write(r.content)


def start_migration():
    """
    Calls the process function and
    renames the directory
    """
    if not os.path.isdir(".theia"):
        sys.exit("The .theia directory does not exist")
    
    for file in FILE_LIST:
        print(f"Processing: {file['filename']}")
        process(file["filename"], file["url"])
        
    print("Renaming directory")
    os.rename(".theia", ".vscode")
    print("Changes saved.")
    print("Please add, commit and push to GitHub.")
        

if __name__ == "__main__":
    print("CI Theia to VSCode Migration Utility")
    print(f"Usage: python3 {sys.argv[0]} [--nobackup]")
    print("If the --nobackup switch is provided, then changed files will not be backed up.")
    print()
    BACKUP = "--nobackup" in sys.argv
    if input("Start migration? Y/N ").lower() == "y":
        start_migration()
    else:
        sys.exit("Migration cancelled by the user")
