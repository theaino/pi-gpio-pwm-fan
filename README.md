# pi-gpio-pwm-fan
A simple python script for automatic temperate control on the raspberry pi.

## Installation

Please note this was only tested on a raspberry pi 4 running the 64 bit ubuntu server image.
This should also work on raspbian.

### 1. Clone the git repository

In any directory, clone the git repository by running

`git clone https://github.com/AinoSpring/pi-gpio-pwm-fan`

### 2. Run the install script

In the repository directory, run the install.sh file.

`cd pi-gpio-pwm-fan`

`sudo sh install.sh`

> **_NOTE:_**  You have to run the command as root, else it won't work.

### 3. Finished!

You can now delete the cloned repository.

The config file is located at `/usr/bin/pi-gpio-pwm-fan/config.json`.

You can also check the status by running

`sudo systemctl status pi-gpio-pwm-fan`
