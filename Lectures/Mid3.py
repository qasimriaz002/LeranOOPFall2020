class person:
    name = ""
    age = 0
    def intro (self):
        print("Constructor")
    def __add__(self, other):
        temp = self.age + other.age
        return  temp
        # pass
    def mango(self):
        print("Mango Function")

p1 = person()
p1.age = 10
p2 = person()
p2.age = 29
p3 = p1 + p2
print(p3)



