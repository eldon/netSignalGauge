set -eux

PERCDUTY=`expr $1 * 1000`

# set the period to 1000 us (adjust as needed in nanoseconds)
echo 1000000 > /sys/class/pwm/pwmchip0/pwm0/period
# set the duty cycle to 100 us (adjust as needed in nanoseconds)
echo $PERCDUTY > /sys/class/pwm/pwmchip0/pwm0/duty_cycle

echo on > /sys/class/pwm/pwmchip0/pwm0/power/control
