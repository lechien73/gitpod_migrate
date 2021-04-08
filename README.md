![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)
# Arctic Tern

## What?

It's a migration tool for Gitpod. When students change their default editor in account settings to VSCode instead of Theia, certain parts of their older repositories may stop working.

This tool can be provided to students. They will need to run it from their project directory.

## How?

Effectively, the tool simply downloads the latest settings files from our Gitpod Full Template repo, overwrites the existing ones and then renames the directory from `.theia` to `.vscode`.

It also backs up the changed files by giving them a `.bak` suffix, though this can be switched off by running it with the `--nobackup` switch.

## Usage

`python3 arctictern.py [--nobackup]`

The `--nobackup` switch will prevent backup files from being created.

## Arctic Tern?

It's a little bird that makes a big migration.

I'll get my coat.

------

Matt Rudge<br/>
April, 2021