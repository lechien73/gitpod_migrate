"""
arctictern.py
A little script that does a big migration
"""

import os
import requests
import shutil
import subprocess
import sys

BASE_URL = "https://raw.githubusercontent.com/Code-Institute-Org/gitpod-full-template/master/"

BACKUP = False
UPGRADE = False

MIGRATE_FILE_LIST = [{"filename": ".theia/settings.json",
                      "url": ".vscode/settings.json"
                      },
                     {"filename": ".gitpod.yml",
                      "url": ".gitpod.yml"
                      },
                     {"filename": ".gitpod.dockerfile",
                      "url": ".gitpod.dockerfile"
                      },
                     {"filename": ".theia/heroku_config.sh",
                      "url": ".vscode/heroku_config.sh"
                      },
                     {"filename": ".theia/init_tasks.sh",
                      "url": ".vscode/init_tasks.sh"
                      }]

UPGRADE_FILE_LIST = [{"filename": ".vscode/settings.json",
                      "url": ".vscode/settings.json"
                      },
                     {"filename": ".gitpod.yml",
                      "url": ".gitpod.yml"
                      },
                     {"filename": ".gitpod.dockerfile",
                      "url": ".gitpod.dockerfile"
                      },
                     {"filename": ".vscode/heroku_config.sh",
                      "url": ".vscode/heroku_config.sh"
                      },
                     {"filename": ".vscode/init_tasks.sh",
                      "url": ".vscode/init_tasks.sh"
                      },
                     {"filename": ".vscode/since_update.sh",
                      "url": ".vscode/since_update.sh"
                      }]


def process(file, suffix):
    """
    Replaces and optionally backs up the files that
    need to be changed.
    Arguments: file - a path and filename
               suffix - the suffix to the BASE_URL
    """

    if BACKUP:
        try:
            shutil.copyfile(file, f"{file}.bak")
        except FileNotFoundError:
            print(f"{file} not found, a new one will be created")

    with open(file, "wb") as f:
        r = requests.get(BASE_URL + suffix)
        f.write(r.content)


def start_migration():
    """
    Calls the process function and
    renames the directory
    """
    if not os.path.isdir(".theia") and not UPGRADE:
        sys.exit("The .theia directory does not exist")

    FILE_LIST = UPGRADE_FILE_LIST if UPGRADE else MIGRATE_FILE_LIST

    if UPGRADE and not os.path.isdir(".vscode"):
        print("Creating .vscode directory")
        os.mkdir(".vscode")

    for file in FILE_LIST:
        print(f"Processing: {file['filename']}")
        process(file["filename"], file["url"])

    if not UPGRADE:
        print("Renaming directory")
        os.rename(".theia", ".vscode")
    else:
        os.chmod(".vscode/since_update.sh", 0o777)
        subprocess.run(".vscode/since_update.sh")

    print("Changes saved.")
    print("Please add, commit and push to GitHub.")
    
    if UPGRADE:
        print("You may need to stop and restart your workspace for")
        print("the changes to take effect.")


if __name__ == "__main__":
    print("CI Template Migration Utility")
    print(f"Usage: python3 {sys.argv[0]} [--nobackup --upgrade]")
    print("If the --nobackup switch is provided, then changed files will not be backed up.")
    print("If the --upgrade switch is provided, the repo will be updated to the latest version of the template")
    print()
    BACKUP = "--nobackup" in sys.argv
    UPGRADE = "--upgrade" in sys.argv
    if input("Start? Y/N ").lower() == "y":
        start_migration()
    else:
        sys.exit("Migration cancelled by the user")
