class person:
    pname = ""
    page = ""

    def __init__(self,name, age):
        self.pname = name
        self.page = age

    def introduce(self):
        print("My name is " + str(self.pname))
        print("My age is " + str(self.page))

class student(person):
    def __init__(self):

        print("This is constructor of child class")
    def stdIntro(self):
        print("I am a student")


s1 = student()
s1.introduce()
s1.stdIntro()

p1 = person("Usman" , 20)
p1.introduce()
