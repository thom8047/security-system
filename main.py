"""Module Security provides the singleton object for security operations."""
from src import Security


def handle_button(button):
    """Handles when the button is pressed"""
    button.wait_for_press()
    print("pressed")
    button.wait_for_release()
    print("done")

    # Repeat
    handle_button(button)


if __name__ == "__main__":
    SECURITY_CLASS = Security()

    def when_pressed():
        """in-scope method"""

        # pylint: disable=no-member
        SECURITY_CLASS.toggle_backlight()

    SECURITY_CLASS.button.when_held = when_pressed
    handle_button(SECURITY_CLASS.button)
