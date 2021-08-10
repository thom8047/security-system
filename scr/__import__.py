import RPIO.GPIO as gpio                # just incase I want to do it with the RPi.GPIO package
import gpiozero as zero                 # for easily using input and output GPIO's
import smtplib                          # for connecting to gmail to send email and text
from email.mime.text import MIMEText    # for creating an email format
from RPLCD.i2c import CharLCD as LCD    # for LCD to display text and info to user
from time import sleep as wait          # because I like lua


class security:
  def __init__:
    lcd = LCD("PCF8574", 0x27, cols=16, rows=2)
    input_button = zero.Button()    #config later  // For user input to enter keys
    user_button = zero.Button()     #config later  // For disbaling alarm, 
    alarm = zero.Buzzer()           #config later  // For the alarm, will work for now as an active buzzer
    # possibly add led's for armed or not-armed, for cool colorful display and for whatever else.
    
