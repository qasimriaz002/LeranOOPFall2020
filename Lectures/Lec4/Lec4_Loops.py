# Loops in python
# Loops are the repetitive structures which are used for repeated execution of line of code.
# There are three type of loops in python
#       1. Counter Loop --- Also known as For Loop
#       2. Non Counter Loop --- Also known as While Loop
#       3. Nested Loop --- Also known as loop inside Loop

# While Loop
# Printing first ten natural numbers

counter = 1

while counter <= 10:            # Indentation is required to be the part of while loop
    print(counter)              # This line is part of while loop
    print("Allah")            # This line is part of while loop
    counter = counter + 1      # This line is part of while loop
print("Allah is great")      # This line is outside (not a part) of while loop

print("=================================")

x = range(1,10)

for number in x:
    ans = number + 1
    print(ans)

print("=================================")

stdNames = ["Qasim", "Bilal", "Aslam", "Usman", "Sarmad"]
for eachstudent in stdNames:
    print(eachstudent + " is my student.")


print("=================================")

i = 1
while i <= 10:
    print("----")
    print(i)
    print("----")
    j = 15
    while j <= 20:
        print(j)
        j = j + 1
    i = i + 1


