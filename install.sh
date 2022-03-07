#!/bin/bash

set -o errexit
set -o nounset

SOURCE_DIR=$PWD
BIN_DIR="/usr/local/bin"
XSESSION_DIR="/usr/share/xsessions"

XSESSION_FILE="steam.desktop"
SESSION_SCRIPT_FILE="steam-session"

if [[ $EUID != 0 ]]; then
    echo "You need to have root privileges to run this script."
    echo "Please try again using 'sudo'. Exiting."

    exit 2
fi

if [[ -z $*  || $1 == "--help" ]]; then
    echo "Usage install.py [OPTION]"
    echo "OPTIONS:"
    printf "    %-4s%s\n" "-i," "--install"
    printf "    %-4s%s\n" "-r," "--remove"
    printf "    %-4s%s\n" "" "--help"

    exit 0

elif [[ $1 == "--install" || $1 == "-i" ]]; then

    if [[ ! -d ${XSESSION_DIR} ]]; then
        mkdir -v ${XSESSION_DIR}
    fi

    cp -v "${SOURCE_DIR}/${SESSION_SCRIPT_FILE}" "${BIN_DIR}/${SESSION_SCRIPT_FILE}"
    cp -v "${SOURCE_DIR}/${XSESSION_FILE}" "${XSESSION_DIR}/${XSESSION_FILE}"

    chmod -v +x "${BIN_DIR}/${SESSION_SCRIPT_FILE}"

    exit 0

elif [[ $1 == "--remove" || $1 == "-r" ]]; then

    rm -v "${BIN_DIR}/${SESSION_SCRIPT_FILE}"
    rm -v "${XSESSION_DIR}/${XSESSION_FILE}"

    exit 0

else
    echo "Unrecognized arguments: '$*'"
    echo "Try '$(basename "$0") --help' for more information"

    exit 1

fi