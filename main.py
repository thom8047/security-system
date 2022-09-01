from src import Security

def handleButton(button):
    button.wait_for_press()
    print("pressed")
    button.wait_for_release()
    print("done")

    # Repeat
    handleButton(button)

if (__name__ == "__main__"):
    SECURITY_CLASS = Security()
    def whenPressed():
        SECURITY_CLASS.toggleBacklight()
    SECURITY_CLASS.button.when_held = whenPressed
    handleButton(SECURITY_CLASS.button)


