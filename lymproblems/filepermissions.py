# Create a file hello.txt in the /tmp directory which can only
# be 1. read by the owner and the group
#    2. written to by the user.

import os
import stat
from .utils import system, success, fail, find_path_data


def setup():
    pass


def verify():
    file = "/tmp/hello.txt"

    # check if the file exists
    if not os.path.exists(file):
        fail("hello.txt is missing from /tmp")

    file_stat = os.stat(file)
    if stat.S_IMODE(file_stat.st_mode) != 0o640:
        fail("hello.txt does not have the correct permissions")

    success()
