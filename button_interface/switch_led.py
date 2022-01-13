import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

switch = 16
led = 8

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led, GPIO.OUT, initial=GPIO.LOW) # Set pin 8 to be an output pin and>
GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:
 button_state = GPIO.input(switch)
 if  button_state == False:
    GPIO.output(led, True)
    print('Button Pressed...')
    while GPIO.input(switch) == False:
        time.sleep(0.2)
    else:
      GPIO.output(led, False)
