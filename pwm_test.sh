#!/bin/bash

# error on unset vars, print line by line
set -ux

# request device- must be done before any of the following settings can be changed
echo 0 > /sys/class/pwm/pwmchip0/export
sleep 1

# uncomment to debug
# cat /sys/kernel/debug/pwm

# set the polarity to active HIGH (echo normal) or active LOW (echo inversed)- must be done before enabled
echo normal > /sys/class/pwm/pwmchip0/pwm0/polarity

# enable PWM channel using set- must be done before period or duty_cycle are set)
echo 1 > /sys/class/pwm/pwmchip0/pwm0/enable

# set the period to 1000 us (adjust as needed in nanoseconds)
echo 1000000 > /sys/class/pwm/pwmchip0/pwm0/period
# set the duty cycle to 100 us (adjust as needed in nanoseconds)
echo 100000 > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

echo auto > /sys/class/pwm/pwmchip0/pwm0/power/control

sleep 5

echo 0 > /sys/class/pwm/pwmchip0/pwm0/enable
echo 0 > /sys/class/pwm/pwmchip0/unexport

echo "done..."
