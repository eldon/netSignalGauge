#!/usr/bin/python
import CHIP_IO.GPIO as GPIO

try:
    GPIO.setup("CSID7", GPIO.OUT)
    GPIO.output("CSID7", GPIO.HIGH)
    raw_input()
    GPIO.output("CSID7", GPIO.LOW)
finally:
    GPIO.cleanup()
