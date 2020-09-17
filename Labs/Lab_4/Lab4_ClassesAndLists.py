# Here in this we will see how can we create list of objects of the classes
# How can we get values or store values in them
# What are the benefits of using the list's of the objects of classes.
# What is difference between the list in class or list of objects of class outside the class\

#   Creating a class human
class human:
    name = ""  # Attributes / variables
    age = ""

    def introduction(self):  # Behaviour / functions
        print("My name is: " + self.name)
        print("My age is: " + str(self.age) + " years")
        print("-------------------------------------")


#   Creating a class student --- Which include a list of Student Marks
class student:
    stdName = ""
    stdAge = ""
    stdMarks = []

    def introduction(self):
        print("My name is: " + self.stdName)
        print("My age is: " + str(self.stdAge) + " years")
        print("My marks in English are: " + str(self.stdMarks[0]))
        print("My marks in Urdu are: " + str(self.stdMarks[1]))
        print("My marks in Math are: " + str(self.stdMarks[2]))
        print("-------------------------------------")


#   Creating objects of class human
h1 = human()
h1.name = "Ali"
h1.age = 20
h1.introduction()

h2 = human()
h2.name = "Hassan"
h2.age = 22
h2.introduction()

#   Creating the objects of student class
std1 = student()
std1.stdName = "Jamil"
std1.stdAge = 12
std1.stdMarks = [39, 35, 46]
# std1.introduction()

std2 = student()
std2.stdName = "Usman"
std2.stdAge = 14
std2.stdMarks = [41, 25, 42]
# std2.introduction()

std3 = student()
std3.stdName = "Umer"
std3.stdAge = 11
std3.stdMarks = [19, 43, 32]
# std3.introduction()

std4 = student()
std4.stdName = "Kamran"
std4.stdAge = 15
std4.stdMarks = [41, 49, 45]
# std4.introduction()

#   Creating list of objects of the student class.
#                0     1     2     3
studentsList = [std1, std2, std3, std4]
# studentsList[0].introduction()
# studentsList[1].introduction()
# studentsList[2].introduction()
# studentsList[3].introduction()

for eachStudent in studentsList:
    eachStudent.introduction()
