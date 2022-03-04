#!/usr/bin/env python3

import os
import sys
import shutil
from pathlib import Path

source_dir = Path.cwd()
bin_dir = Path("/usr/local/bin/")
xsession_dir = Path("/usr/share/xsessions/")


if os.geteuid() != 0:
    sys.exit("You need to have root privileges to run this script.\nPlease try again using 'sudo'. Exiting.")

if len(sys.argv) == 1:
    print(f"Usage {__file__} [OPTION]")
    print()
    print("OPTIONS:")
    print("\t-i, --install")
    print("\t-r, --remove")

else:
    if sys.argv[1] == ("-i" or "--install"):
        print("Installing steam-session")

        shutil.copyfile(source_dir / "/steam-session.py",
                        bin_dir / "steam-session.py")
        print(f"Copied file to {bin_dir / 'steam-session.py'}")

        shutil.copyfile(source_dir / "steam.desktop",
                        xsession_dir / "steam.desktop")
        print(f"Copied file to {xsession_dir / 'steam.desktop'}")

    elif sys.argv[1] == ("-r" or "--remove"):
        print("Removing steam-session")
        try:
            (bin_dir / "steam-session.py").unlink()
            print(f"Removed file from {bin_dir / 'steam-session.py'}")
        except FileNotFoundError:
            print(f"{bin_dir / 'steam-session.py'} does not exist")

        try:
            (xsession_dir / "steam.desktop").unlink()
            print(f"Removed file from {xsession_dir / 'steam.desktop'}")
        except FileNotFoundError:
            print(f"{xsession_dir / 'steam.desktop'} does not exist")

    else:
        print("Invalid flag")
