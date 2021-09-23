![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# Arctic Tern 0.2

## What?

It's a migration tool for Gitpod. When students change their default editor in account settings to VSCode instead of Theia, certain parts of their older repositories may stop working.

Additionally, and now (possibly) primarily, the tool allows students to upgrade their workspace to the current version of the template.

This tool can be provided to students. They will need to run it from their project directory. See the usage section below.

## How?

In earlier versions, the default action was to migrate from Theia to VSCode. In this version, the default action is to upgrade. Now, migration must be specified with the `--migrate` switch.

In migrate mode, the tool simply downloads the latest settings files from our Gitpod Full Template repo, overwrites the existing ones and then renames the directory from `.theia` to `.vscode`.

In upgrade mode, it assumes that the `.vscode` directory already exists and upgrades a repo based on an older template to the latest version. It creates a `post_upgrade.sh` file that runs from `.gitpod.yml` to add necessary changes.

It also backs up the changed files by giving them a `.bak` suffix, though this can be switched off by running it with the `--nobackup` switch.

## Usage

`python3 arctictern.py [--nobackup --migrate]`

The `--nobackup` switch will prevent backup files from being created.

The `--migrate` switch performs a migration on a Theia repo.

To use it:

1. Open the old repo in Gitpod
2. Download this script
3. Run it from the project directory

### Important Note!

**You must have changed your default Gitpod editor from Theia to VSCode in your account settings before running this script**

## Arctic Tern?

It's a little bird that makes a big migration.

I'll get my coat.

------

Matt Rudge<br/>
April, 2021