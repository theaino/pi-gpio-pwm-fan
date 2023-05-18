#!/usr/bin/env sh
cp -R . /usr/bin/pi-gpio-pwm-fan
chmod +x /usr/bin/pi-gpio-pwm-fan/main.py
printf "[Unit]\nDescription=GPIO PWM fan temperature control.\n\n[Service]\nType=simple\nExecStart=python3 /usr/bin/pi-gpio-pwm-fan/main.py\n\n[Install]\nWantedBy=multi-user.target" > /lib/systemd/system/pi-gpio-pwm-fan.service
sudo cp /lib/systemd/system/pi-gpio-pwm-fan.service /etc/systemd/system/pi-gpio-pwm-fan.service
sudo chmod 644 /etc/systemd/system/pi-gpio-pwm-fan.service
systemctl start pi-gpio-pwm-fan