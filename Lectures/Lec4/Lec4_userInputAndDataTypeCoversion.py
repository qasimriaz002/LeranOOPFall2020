# taking value form user at run time.
# The value we enter using the input() method is always of string type
# So if you want to perform any kind of mathematical operation then you will have to convert it into the interger using the int() function already present in the python
# The process of conversion of the data type is called the type casting

studenName = input("Enter your name: ")         # Takin value a runtime from user using input()
studenAge = input("Enter your age: ")
marksEng = int(input("Enter marks of English: "))       # Converting input value into integer type using int() keyword/function
marksUrdu = int(input("Enter marks of Urdu: "))
marksMath = int(input("Enter marks of Math: "))
totalMarks = marksEng + marksMath + marksUrdu
print("======================================")

print("My name is: ")
print(studenName)
print(type(studenName))
print("------------")
print("My age is: ")
print(studenAge)
print(type(studenAge))
print("------------")
print("My Total Marks: ")
print(totalMarks)
print(type(marksEng))
print(type(marksUrdu))
print(type(marksMath))
print(type(totalMarks))
print("------------")