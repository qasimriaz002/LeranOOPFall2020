from dateutil.tz import win


class Fruit:
    name = ""
    color = ""
    def showFruit(self):
        print("The name of fruit " + self.name)
        print("The color of fruit " + self.color)
    def tasteFruit(self, taste):
        print("The Fruit is " + taste + " in taste ")

class winterFruit(Fruit):
    def tasteFruit(self):
        print("The " + self.name + " is bitter")
    def fruitType(self):
        print("This is winter fruit")

class summerFruit(Fruit):
    def fruitType(self):
        print("This is summer fruit")

mango = Fruit()
mango.name = "Mango"
mango.color = "Yellow"
mango.showFruit()
mango.tasteFruit("Sweet")
print("------------------------------")

orange = winterFruit()
orange.name = "Orange"
orange.color = "Orange"
orange.showFruit()
orange.fruitType()
orange.tasteFruit()
print("------------------------------")

apple = summerFruit()
apple.name = "Apple"
apple.color = "Red"
apple.showFruit()
apple.tasteFruit("Sweetish")

