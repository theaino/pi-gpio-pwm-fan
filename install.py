import os
import pathlib
import sys


def install():
    path = pathlib.Path(os.path.abspath(__file__)).parent
    cmd = f"{sys.executable} {os.path.join(path, 'main.py')}"
    with open("/etc/rc.local", "r+") as f:
        original_data = f.read()
        f.write(original_data.replace("exit 0", f"{cmd} & exit 0"))


if __name__ == "__main__":
    install()
