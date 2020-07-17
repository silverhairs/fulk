#!/usr/bin/env python3

import click
import os
import time

BOLD_TEXT = "\033[1m"


@click.command()
@click.option("--prefix", "-p", help="Prefix of your files", prompt=True, required=True)
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
                new_f = f"{prefix}_0{count}{ext}"
                dst = f"{os.getcwd()}/{new_f}"

                time.sleep(
                    # just to make it print smoother and look cool 😎️
                    # //TODO: When you have >= 1000 files I'd suggest to remove this function
                    0.001
                )
                os.rename(src=src, dst=dst)
                click.secho(f"{BOLD_TEXT}{f}  ==>  {new_f}")
            click.secho(f"\n{BOLD_TEXT}⚡️⚡️ {count+1} files renamed ⚡️⚡️", fg="blue")

        except Exception as e:
            click.secho(f"{BOLD_TEXT}{repr(e)}", fg="red")
