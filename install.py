import os
import pathlib
import sys


def install():
    path = pathlib.Path(os.path.abspath(__file__)).parent
    cmd = f"{sys.executable} {os.path.join(path, 'main.py')}"
    with open("/etc/systemd/pi-gpio-pwm-fan.conf", "w") as f:
        f.write(f"""start on runlevel [2345]
stop on runlevel [!2345]

exec {cmd}""")
        os.system("service pi-gpio-pwm-fan start")


if __name__ == "__main__":
    install()
    print("Finished installing.")
