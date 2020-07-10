#!/usr/bin/env python3

import click
import os
from click_spinner import spinner

BOLD_TEXT = "\033[1m"


@click.command()
@click.option("-p", "--prefix", "prefix", help="Prefix of your files", required=True)
@click.version_option(version="0.0.1")
def main(prefix):
    """A tool to rename all the files contained in a folder with the same convention."""

    files = [f for f in os.listdir(".") if os.path.isfile(f)]
    if files == []:
        click.secho(f"{BOLD_TEXT}There is no file in this directory", fg="red")
    else:
        try:
            for count, f in enumerate(files):
                filename, ext = os.path.splitext(f"{os.getcwd()}/{f}")
                src = f"{os.getcwd()}/{f}"
                dst = f"{os.getcwd()}/{prefix}_0{count}{ext}"

                with spinner():
                    os.rename(src=src, dst=dst)
            click.secho(f"{BOLD_TEXT}{count+1} files renamed", fg="blue")

        except Exception as e:
            click.secho(f"{BOLD_TEXT}{repr(e)}", fg="red")
