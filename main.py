from src import Security

def handleButton():
    SECURITY_CLASS = Security()
    def whenPressed():
        SECURITY_CLASS.toggleBacklight()
    SECURITY_CLASS.button.when_held = whenPressed

    SECURITY_CLASS.button.wait_for_press()
    print("pressed")
    SECURITY_CLASS.button.wait_for_release()
    print("done")

    # Repeat
    handleButton()

if (__name__ == "__main__"):
    handleButton()


