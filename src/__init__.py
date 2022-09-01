# import RPIO.GPIO as gpio  # just incase I want to do it with the RPi.GPIO package


# import smtplib  # for connecting to gmail to send email and text
# from email.mime.text import MIMEText  # for creating an email format


from RPLCD.i2c import CharLCD as LCD
from time import sleep
import gpiozero as zero


class Button(zero.Button):
    """The `Button` class attached to the `gpiozero` package"""

    pass


class Buzzer(zero.Buzzer):
    """The `Buzzer class attached to the `gpiozero` package"""

    pass


class Security:
    """Security singleton class

    Args:
        None

    Returns:
        The `Security` object that has various public and private methods that take advantage
        of multiple Raspberry Pi libraries for use of Buttons, Buzzers, LCD Displays, etc. Please
        refer to the documents file for instruction and documentation on this classes capabilities.

    Editor_Notes:
        May move in the direction of instantiating a Flask back-end for access via a
        front-end application (React, MUI5) and from that we'll be able to preform actions
        on the raspberry pi via these commands
    """

    def __init__(self):
        # The LCD connections are listed on the LCD, 5v is the red,
        self.lcd = LCD("PCF8574", 0x27, cols=16, rows=2)
        self.lcd.backlight_enabled = False
        self.button = Button(17)
        self.button.hold_time = 3
        # self.alarm = Buzzer(24)

    def wait(self, lapse):
        """Method for synchronously waiting

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

    def enableBacklight(self):
        if self.lcd:
            self.lcd.backlight_enabled = True

    def disableBacklight(self):
        if self.lcd:
            self.lcd.backlight_enabled = False

    def toggleBacklight(self):
        if self.lcd:
            self.lcd.backlight_enabled = not self.lcd.backlight_enabled

    def writeOutputToLCD(self, output):
        """Write to the self.lcd

        Args:
            output (string): Output display
        """
        if self.lcd:
            self.lcd.write_string(output)

    def clearLCDDisplay(self):
        if self.lcd:
            self.lcd.clear()
