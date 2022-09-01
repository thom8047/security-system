from src import Security

if (__name__ == "__main__"):
    SECURITY_CLASS = Security()
    def whenPressed():
        SECURITY_CLASS.toggleBacklight()

    SECURITY_CLASS.button.wait_for_press()
    print("pressed")
    SECURITY_CLASS.button.when_pressed = whenPressed
    SECURITY_CLASS.button.wait_for_released()
    print("done")


