# Here in today's lab we are going to learn about other data types like list, dictionaries and etc

markslist = [40, 44, 39, 55, 22, 88, 91, 33]        #Creating a list python
print(type(markslist))                              #Checking the type of list in python
print(type(markslist[3]))                           #Checking the type of element of list
markslist[0] = 10                                   #Changing the value at specific index
print(markslist[0])                                 #Print the value at specific index in list
print(markslist)

print("-------------------------------")

orangelist = markslist*2                            #Multiplying list with any number will repeat the values
print(orangelist)

print("-------------------------------")

# Creating list of different data types
print("Showing list with values of different data types")
mangoList = ["Bilal", 40, "BSEM-1-2019"]
print(mangoList)
print(type(mangoList))
print(mangoList[0])
print(type(mangoList[0]))
print(mangoList[1])
print(type(mangoList[1]))
print(mangoList[2])
print(type(mangoList[2]))

print("-------------------------------")

print("Difference b/w string and int")
# Working as int
n1 = 10
n2 = n1 + n1
print(n2)
print("Type of n1:")
print(type(n1))
print("Type of n2:")
print(type(n2))
# Working as string
n3 = "10"
n4 = n3 + n3
print(n2)
print("Type of n1:")
print(type(n1))
print("Type of n2:")
print(type(n2))
