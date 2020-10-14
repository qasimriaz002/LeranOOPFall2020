#   Here in this lecture we are going to see how we can insert or retrieve values from the list using the loops.

list_stdName = []
list_stdAge = []

numberOfRecords = int(input("How many records you want to enter: "))  # 3
print("---------------------------------------------------")

#   Using while loop to insert values in the list

# wantTo_InsertValue = True
listIndex = 0

# while wantTo_InsertValue == True:

while listIndex < numberOfRecords:  # 0<3, 1<3, 2<3, 3<3
    list_stdName.append(input("Enter the name of student: "))
    list_stdAge.append(input("Enter the age of student:"))
    print("---------------------------------------------------")
    print("Record Saved Successfully")
    print("---------------------------------------------------")
    listIndex = listIndex + 1  # 0+1=1, 1+1=2, 2+1=3
    # wantTo_InsertValue = False
    # print("Do you want to Enter Record of another student:")
    # print("Write 1 to enter new record or write 0 to exit:")
    # question = input("Enter number: ")
    # print("---------------------------------------------------")
    # if question == 1:
    #     print("Enter the details of next record")
    #     print("---------------------------------------------------")
    #     wantTo_InsertValue = True
    # else:
    #     print("---------------------------------------------------")
    #     print("Thanks for using our system")
    #     print("---------------------------------------------------")

#   Showing records with for loop
counter = 0
for name in list_stdName:
    print("The name of student = " + name)
    print("The age of student = " + list_stdAge[counter])
    counter = counter+1
    print("------------------------------")

print(list_stdName)
print(list_stdAge)
