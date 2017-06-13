#!/usr/bin/python

import re
import requests
import subprocess
import sys

def main(address, password):
    signal_quality = get_signal_quality(address, password)
    set_pwm(signal_quality)
    return signal_quality


def get_signal_quality(address, password):
    r = requests.get('http://{}/Info.live.htm'.format(address), auth=('admin', password))
    c = r.content

    try:
        c = re.search('(\'ath1.*)(?:}{active_wds)', c).group(1).split(',')
        c = [re.sub('\'', '', x) for x in c]
    except AttributeError as e:
        print e
        return 0  # something wrong with API or connection, quality is 0.

    signal_quality = c[-1]
    signal_quality_perc = int(signal_quality[:-1])

    return signal_quality_perc

def init_pwm():
    if subprocess.check_call(('bash', './bin/pwm_init.sh')) != 0:
        raise IOError('PWM could not be initialized. Aborting.')

def close_pwm():
    if subprocess.check_call(('bash', './bin/pwm_close.sh')) != 0:
        raise IOError('PWM could not be closed. Aborting.')

def set_pwm(duty_cycle):
    if subprocess.check_call(('bash', './bin/pwm_set.sh', str(duty_cycle))) != 0:
        raise IOError('PWM could not be set. Aborting.')


if __name__ == '__main__':
    address, password = sys.argv[1], sys.argv[2]
    print main(address, password)