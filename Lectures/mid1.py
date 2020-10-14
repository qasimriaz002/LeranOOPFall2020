# Constructors in Python


class operatingSystem:
    OS_NAME = ""
    def __init__(self,osName):
        print("Desktop Icons are shown at " + osName)
        self.OS_NAME = osName

    def playMusic(self):
        print("OS is playing Music in " + self.OS_NAME)

    def __del__(self):
        print("Object of " + self.OS_NAME +" is destroyed")


xp = operatingSystem("XP")
xp.playMusic()

del xp

win7 = operatingSystem("Windows 7")
win7.playMusic()



