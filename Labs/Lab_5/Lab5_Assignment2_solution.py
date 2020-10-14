# Creation of three classes

class animal:
    name = ""
    color = ""

    def introduceAnimal(self):
        print("The name of Animal: " + self.name)
        print("The color of Animal " + self.color)

    def speakAnimal(self, sound):
        print("The " + self.name + ": " + sound)

class landAnimal (animal):
    def walk(self):
        print("The " + self.name + " can walk")

class seaAnimal (animal):
    def swim(self):
        print("The " + self.name + " can swim")

dogAnimal = landAnimal()
catAnimal = landAnimal()

whaleAnimal = seaAnimal()
crocodileAnimal = seaAnimal()

dogAnimal.name = "Dog"
dogAnimal.color = "Black"
dogAnimal.introduceAnimal()
dogAnimal.speakAnimal("Bark")
dogAnimal.walk()

print("--------------------------")

catAnimal.name = "Tom-Cat"
catAnimal.color = "Black"
catAnimal.introduceAnimal()
catAnimal.speakAnimal("Meaon")
catAnimal.walk()

print("--------------------------")
whaleAnimal.name = "Whale"
whaleAnimal.color = "Gray"
whaleAnimal.introduceAnimal()
whaleAnimal.speakAnimal("No-Sound")
whaleAnimal.swim()
print("--------------------------")

crocodileAnimal.name = "Jerry-Crocodile"
crocodileAnimal.color = "Brown"
crocodileAnimal.introduceAnimal()
crocodileAnimal.speakAnimal("Distres")
crocodileAnimal.swim()
print("--------------------------")






