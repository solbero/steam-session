#!/usr/bin/env python3

import os
import shutil
import sys
import stat
from pathlib import Path

src_dir = Path.cwd()
bin_dir = Path("/usr/local/bin/")
xsession_dir = Path("/usr/share/xsessions/")

print(sys.argv)


def help() -> None:
    """Help message"""
    print()
    print("Usage install.py [OPTION]")
    print("OPTIONS:")
    print("\t-i, --install")
    print("\t-r, --remove")
    print()


def install(file: str, source: Path, destination: Path, executable: bool = False) -> None:
    source_file = source / file

    if not destination.exists():
        print(f"Folder '{destination}' does not exist")
        destination.mkdir()
        print(f"Created folder '{destination}'")

    shutil.copy(source_file, destination)
    print(f"Copied '{file}' to '{destination / file}'")

    if executable is True:
        mode = stat.S_IRWXU | stat.S_IRGRP | stat.S_IXGRP | stat.S_IROTH | stat.S_IXOTH
        os.chmod(destination / file, mode)
        print(f"Mode of '{destination / file}' set to {oct(mode)[2:]}")



def remove(file: str, path: Path) -> None:
    file_path = path / file

    try:
        file_path.unlink()
        print(f"Removed file '{file_path}'")
    except FileNotFoundError:
        print(f"'{file_path}' does not exist")


if __name__ == "__main__":

    if os.geteuid() != 0:
        sys.exit("You need to have root privileges to run this script.\n \
            Please try again using 'sudo'. Exiting.")

    if len(sys.argv) == 1:
        # Print help message if called without arguments
        help()

    else:
        if sys.argv[1] == "-i" or sys.argv[1] == "--install":
            print("Installing steam-session")

            # Install session files
            install("steam-session", src_dir, bin_dir, executable=True)
            install("steam.desktop", src_dir, xsession_dir)

        elif sys.argv[1] == "-r" or sys.argv[1] == "--remove":
            print("Removing steam-session")

            # Remove session files
            remove("steam-session", bin_dir)
            remove("steam.desktop", xsession_dir)

        else:
            print(f"Unrecognized argument: {' '.join(sys.argv[1:])}")
