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

    FILE_LIST = UPGRADE_FILE_LIST if do_upgrade else MIGRATE_FILE_LIST

    for file in FILE_LIST:
        print(f"Processing: {file['filename']}")
        process(file["filename"], file["url"])

    if not UPGRADE:
        print("Renaming directory")
        os.rename(".theia", ".vscode")

    print("Changes saved.")
    print("Please add, commit and push to GitHub.")


if __name__ == "__main__":
    print("CI Theia to VSCode Migration Utility")
    print(f"Usage: python3 {sys.argv[0]} [--nobackup --upgrade]")
    print("If the --nobackup switch is provided, then changed files will not be backed up.")
    print("If the --upgrade switch is provided, the repo will be updated to the latest version of the template")
    print()
    BACKUP = "--nobackup" in sys.argv
    UPGRADE = "--upgrade" in sys.argv
    if input("Start migration? Y/N ").lower() == "y":
        start_migration()
    else:
        sys.exit("Migration cancelled by the user")
