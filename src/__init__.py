# import RPIO.GPIO as gpio  # just incase I want to do it with the RPi.GPIO package
# import smtplib  # for connecting to gmail to send email and text
# from email.mime.text import MIMEText  # for creating an email format

from time import sleep
import asyncio
from RPLCD.i2c import CharLCD as LCD
import gpiozero as zero


class Security:
    """Security singleton class

    Args:
        defaultLcdButtonPin (int): The GPIO pin number representing the button

    Returns:
        The `Security` object that has various public and private methods that take advantage
        of multiple Raspberry Pi libraries for use of Buttons, Buzzers, LCD Displays, etc. Please
        refer to the documents file for instruction and documentation on this classes capabilities.

    Editor_Notes:
        May move in the direction of instantiating a Flask back-end for access via a
        front-end application (React, MUI5) and from that we'll be able to preform actions
        on the raspberry pi via these commands
    """

    def __init__(self, defaultLcdButtonPin=17):

        # The LCD connections are listed on the LCD, 5v is the red,
        self.lcd = LCD("PCF8574", 0x27, cols=16, rows=2)
        self.lcd.backlight_enabled = True

        # The LCD button pin number
        self.toggle_lcd_button = zero.Button(defaultLcdButtonPin)
        self.toggle_lcd_button.hold_time = 3
        # This will automatically run as long as the python script is executing
        self.toggle_lcd_button.when_held = self.enable_backlight
        # Starts as null
        self.toggle_lcd_button.when_released = self.click_menu_option

        # Set up the menu
        self.menu = {
            "menu": {
                "System settings": {
                    "Enable system": self.undefined,
                    "Disable system": self.undefined,
                },
                "Turn screen OFF": self.disable_backlight,
            },
            "selected": {
                # "item": None,
                "position": 0
            },
            "parent": {},
        }

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

    def hold_selected_menu_option(self):
        """Wrapper function to perform menu option action(s)

        Args:
            action (function): The action needing to be performed
        """
        if self.lcd.backlight_enabled:
            position = self.menu["selected"]["position"]
            selected_key = list(self.menu["parent"])[position]
            if type(self.menu["parent"][selected_key]) == type({}):
                # dive in
                self.menu["parent"] = self.menu["parent"][selected_key]
                self.menu["selected"] = {
                    # "item": list(self.menu["parent"])[0],
                    "position": 0,
                }
            else:
                # preform action
                self.menu["parent"][selected_key]()

    def click_menu_option(self):
        """Wrapper function to cycle through menu option action(s)

        Args:
            None
        """
        if self.lcd.backlight_enabled:
            parent_options = list(self.menu["parent"])
            current_position = self.menu["selected"]["position"]

            if len(parent_options) == current_position:
                # were at our last option
                self.menu["selected"]["position"] = 0
                return

            self.menu["selected"]["position"] = current_position + 1
            return

    def undefined(self):
        """Undefined method

        Editor_Notes:
            Some of the `gpiozero` methods need to be set to None when no functionality
            is needed, and when other functionality prompts, they need action. This member
            will return none, so we can unify the type of `undefined` for methods and
            other attributes.
        """
        return None
