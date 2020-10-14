# Encapsulation ---- Not Complete
# Inheritance
# Polymorphism
# Abstraction

# Creation of a class in python
class human:
    name = ""
    age = ""
    gender = ""

hassan = human()
hassan.name = "Hassan Rauf"
hassan.age = 20
hassan.gender = "Male"

usman = human()
usman.name = "Usman Ijaz"
usman.age = 30
usman.gender = "Male"

print("----Showing all details of hassan object----")
print(hassan.name)
print(hassan.age)
print(hassan.gender)
print("----Showing all details of usman object----")
print(usman.name)
print(usman.age)
print(usman.gender)
print("----Showing all details types of object----")
print(type(usman))
print(type(hassan))

x = 10
print(type(x))

