# Here in this lecture we are going to learn how to use conditional structures in python
# In this lecture we will learn simple if conditions, if else conditions, if else if conditions, nested if conditions

#--------------------------------------------------------------------------------------
# Simple If condition
print("----------Simple if Condition----------")
mobilePrice = 5000
if mobilePrice < 10000:                   # Indentation is required to be the part of if condition
    print("Purchase Mobile Phone")      # This line is part of if condition
    print("Purchase only one")          # This line is part of if condition

print("Phone is good")                  # This line outside the if condition

#--------------------------------------------------------------------------------------
# if else condition
print("----------If Else Condition----------")
studentMarks = 40
if studentMarks >= 40:
    print("Student is pass")                    # This line is part of if condition
    print("Student is eligible for degree")    # This line is part of if condition
else:
    print("Student is fail")                        # This line is part of else condition
    print("Student is not eligible for degree")   # This line is part of else condition

print("He/She was student of Superior University")  #This line outside of both if and else

#--------------------------------------------------------------------------------------
# if else if conditions
print("----------IF ELSE IF Condition----------")
carPrice = 300000

if carPrice <= 250000:
    print("Purchase 2 Cars")            #This line is part of if condition
elif carPrice <= 500000:
    print("Purchase One Car")           #This line is part of else if condition
    print("Purchase Suzuki Car")
else:
    print("Don't Purchase This Car")    #This line is part of else condition
    print("I don't like mango Car")

print("This is a mango Car")            #This line is outside of if, else if , else condition
#--------------------------------------------------------------------------------------
# Nested if Condition (If inside if or if inside else or if inside else if)
print("----------Nested if Condition----------")
num1 = 10
num2 = 20
num3 = 30
if num1 > num2:                                      # This is outer if condition
    print("Number 1 is greater then number 2")      # This is the line of outer if condition
    if num1 > num3:                                     # This is inner if condition
        print("Number 1 is greater then all numbers")   # This is the line of inner if condition
else:                                                   # This else if part of outer if condition
    print("Number 2 is greater then number 1")      # This is the line of else of outer if
print("We have studied all types of if's")         # This is not part of any kind of if, it is outside all of them
# --------------------------------------------------------------------------------------