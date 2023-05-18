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

You can also check the status by running

`sudo systemctl status pi-gpio-pwm-fan`

## Configure the fan

The config file is located at `/usr/bin/pi-gpio-pwm-fan/config.json`.

The fields are:

  `curve`: It is a python function with the `td` variable which contains the temperature. If the temperature is at `min_temp`, it is 0. If it is at `max_temp`, it is 1.
  
  `min_temp`: Temperature when the fan starts spinning.
  
  `max_temp`: The maximum temperature that should be reached.
  
  `temp_threshold`: The temperature that has to be reached for the fan to start spinning.
  
  `temp_cmd`: The shell-command for fetching the temperature in °C.
  
  `refresh_time`: The minimum time between each speed change.
  
  `pwm_freq`: The pwm-frequency of the fan.
  
  `fan_pin`: The gpio pin the fan is connected to.
  
Once you have changed the config.json file, you have to run

`sudo systemctl restart pi-gpio-pwm-fan`

to restart the script.
