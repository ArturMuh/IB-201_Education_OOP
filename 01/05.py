class BigBell:
    def __init__(self):
        self.Sound = "ding"

    def sound(self):
        print(self.Sound)
        if self.Sound == "ding":
            self.Sound = "dong"
        else:
            self.Sound = "ding"

bell = BigBell()
bell.sound()
bell.sound()
bell.sound()