from src import Security

if (__name__ == "__main__"):
    SECURITY_CLASS = Security()
    SECURITY_CLASS.button.wait_for_press()
    print("pressed")
    SECURITY_CLASS.button.when_pressed = SECURITY_CLASS.toggleBacklight


