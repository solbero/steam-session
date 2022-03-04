#!/usr/bin/env python3

# Imports
import logging
import psutil
import shlex
import shutil
import subprocess
import tempfile
from pathlib import Path
from io import StringIO
from time import sleep

# Globals
temp_dir = Path(tempfile.gettempdir())
log_file = "steam-session.log"

logger = logging.getLogger(__name__)
logging.basicConfig(filename=temp_dir / log_file,
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")


def is_program_running(name: str) -> bool:
    """Check if program is running.

    Args:
        name: Name of program to monitor.

    Returns: Boolean indicating whether the program is running or not.
    """
    pids = []

    # Iterate over the all the running process
    for proc in psutil.process_iter():
        try:
            # Check if process name contains the given name string.
            if name in proc.name().lower():
                pids.append(proc.pid)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

    # Return `True` if PIDs exists for process name
    if len(pids):
        return True
    else:
        return False


def run_executable(name: str, flags: str = "") -> None:
    """Locate and run a executable.

    Args:
        name: Name of executable to run.
        flags (optional): Flags to append to executable. Defaults to "".
    """
    if cmd := shutil.which(f"{name}"):
        run_shell_command(f"{cmd} {flags}")
    else:
        logger.error(f"Could not locate '{name}'")


def run_shell_command(cmd: str) -> None:
    """Run a command using subprocess.

    Args:
        cmd: Command to run.
    """
    # Parse command to list
    args = shlex.split(cmd)
    logger.info(f"Subprocess: '{cmd}'")

    try:
        # Run program
        process = subprocess.Popen(
            args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        process_output, _ = process.communicate()
        log_process_output(process_output)
    except (OSError, subprocess.CalledProcessError) as exception:
        logger.error(f"Exception occurred: {str(exception)}")
        logger.error("Subprocess failed!")
    else:
        logging.info("Subprocess finished")


def log_process_output(pipe: str) -> None:
    """Log the output of a subprocess call.

    Args:
        pipe: Subprocess output to log.
    """
    file = StringIO(pipe)
    # Read and log lines from subprocess pipe
    for line in file.readlines():
        logging.info(f"Got line from subprocess: {line}")


def main() -> None:
    # Start the window manager
    run_executable("xfwm4", "--replace")

    # Disable screen-saver and screen energy saving
    run_executable("xset", "s off -dpms")

    # Start steam
    run_executable("steam")

    # Monitor the steam process and restart if stopped
    while is_running := is_program_running("steam"):
        if not is_running:
            run_executable("steam")
            logger.info("Steam has stopped. Restarting")
        else:
            sleep(1)


if __name__ == "__main__":
    main()
