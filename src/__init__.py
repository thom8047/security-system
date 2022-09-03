# import RPIO.GPIO as gpio  # just incase I want to do it with the RPi.GPIO package
# import smtplib  # for connecting to gmail to send email and text
# from email.mime.text import MIMEText  # for creating an email format

from time import sleep
import asyncio
from RPLCD.i2c import CharLCD as LCD
import gpiozero as zero


# class Button(zero.Button):
#     """The `Button` class attached to the `gpiozero` package"""

#     pass


# class Buzzer(zero.Buzzer):
#     """The `Buzzer class attached to the `gpiozero` package"""

#     pass


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
        self.lcd.backlight_enabled = True

        self.toggle_lcd_button = zero.Button(17)
        self.toggle_lcd_button.hold_time = 3
        # This will automatically run as long as the python script is executing
        self.toggle_lcd_button.when_held = self.toggle_backlight
        self.toggle_lcd_button.when_pressed = self.test

    def wait(self, lapse):
        """Method for synchronously waiting

        Args:
            lapse (float): _description_

        Returns:
            None
        """
        return sleep(lapse)

    def test(self):
        """Test method for security object"""
        print("test")

    def enable_backlight(self):
        """__summary__"""
        if self.lcd:
            self.lcd.backlight_enabled = True

    def disable_backlight(self):
        """__summary__"""
        if self.lcd:
            self.lcd.backlight_enabled = False

    def toggle_backlight(self):
        """Toggles the backlight"""
        if self.lcd:
            self.toggle_lcd_button.when_pressed = self.undefined
            self.lcd.backlight_enabled = not self.lcd.backlight_enabled

    def write_output_to_lcd(self, output):
        """Write to the self.lcd

        Args:
            output (string): Output display
        """
        if self.lcd:
            self.lcd.write_string(output)

    def clear_lcd_display(self):
        """__summary__"""
        if self.lcd:
            self.lcd.clear()

    def undefined(self):
        """Undefined method

        Editor_Notes:
            Some of the `gpiozero` methods need to be set to None when no functionality
            is needed, and when other functionality prompts, they need action. This member
            will return none, so we can unify the type of `undefined` for methods and
            other attributes.
        """
        return None
