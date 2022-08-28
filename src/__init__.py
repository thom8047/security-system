import RPIO.GPIO as gpio  # just incase I want to do it with the RPi.GPIO package
import gpiozero as zero  # for easily using input and output GPIO's
import smtplib  # for connecting to gmail to send email and text
from email.mime.text import MIMEText  # for creating an email format
from RPLCD.i2c import CharLCD as LCD  # for LCD to display text and info to user
from time import sleep


class Button(zero.Button):
    pass

class Buzzer(zero.Buzzer):
    pass

class Security:
    """
    May move in the direction of instantiating a Flask back-end for access via a
    front-end application (React, MUI5) and from that we'll be able to preform actions
    on the raspberry pi via these commands
    """
    def __init__(self):
        # Add a note about where exactly the LCD connections on the Raspberry PI need to go
        self.lcd = LCD("PCF8574", 0x27, cols=16, rows=2)
        self.input_button = Button(26)
        self.alarm = Buzzer(24)

    def wait(self, lapse: float) -> None:
        """_summary_

        Args:
            lapse (float): _description_

        Returns:
            None
        """
        return sleep(lapse)

    def enable(self):
        pass  # meant for enabling the security-sys

    def disable(self):
        pass  # meant for disabling the security-sys

    def checkForBreach(self):
        pass  # checking for opened door, and or other stuff, such as gas

    def turnOnBeep(self):
        pass  # turning on beeper

    def idleUserInput(self):
        pass

    def acceptUserInput(self):
        pass

    def writeUserInput(self):
        pass

    def answerUserInput(self):
        pass
