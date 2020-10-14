# Inheritance ---> It is one of the main parts of Object Oriented Programming
# --->  How do we implement or code or create inheritance in python
# --->  What are the benefits of using inheritance
# --->  Types of inheritance
#               (i)     Simple/Single Inheritance
#               (ii)    Multiple Inheritance
#               (iii)   Multilevel Inheritance
#               (iv)    Hybrid Inheritance

class person:                     # Muhammad Riaz Ahmad ---- Parent Class
    name = ""
    age = ""

    def introduce(self):
        print("My name is: " + self.name)
        print("My age is: " + str(self.age) + " years")
        print("--------------------------")

class student(person):              # Muhammad Qasim Riaz(Muhammad Riaz Ahmad) ----- Child Class
    name = ""
    age = ""

p1 = person()
p1.name = "Ali"
p1.age = 20

p2 = person()
p2.name = "Bilal"
p2.age = 21

s1 = student()
s1.name = "Kamran"
s1.age = 10

s2 = student()
s2.name = "Jamil"
s2.age = 12

p1.introduce()
p2.introduce()

s1.introduce()
s2.introduce()



