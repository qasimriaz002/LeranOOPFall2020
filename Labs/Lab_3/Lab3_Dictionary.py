#   Here in this lecture we are going to work on different built-in methods for dictionaries in python

#   Parts of a dictionary with respect to the example of dictionary given below "dict_std_1"
#       Item ----> 'Name': 'Bilal'
#       Key ---->   'Name'
#       Value ---->  'Bilal'

dict_std_1 = {'Name': 'Bilal', 'Age': 20, 'Semester': '1st'}
# Printing the dictionary directly
print("----------Printing the dictionary----------")
print(dict_std_1)
# Creating a copy of  the dictionary dict_std_1
print("----------Creating a copy of  the dictionary dict_std_1----------")
dict_copy = dict_std_1.copy()
# Printing the a copy "dict_copy" of  the dictionary dict_std_1
print("----------Printing the a copy \"dict_copy\" of  the dictionary dict_std_1----------")
print(dict_copy)
# Length of Dictionray
print("----------Finding length of dictionary----------")
print(len(dict_std_1))
# Getting values from dictionary
print("----------Getting values of dictionary----------")
print(dict_std_1['Name'])
print(dict_std_1['Age'])
print(dict_std_1['Semester'])
# Changing the values in dictionary
print("----------Changing the values in dictionary----------")
dict_std_1['Name'] = 'Hassan'
# Getting changed values from dictionary
print("----------Getting changed values of dictionary----------")
print(dict_std_1['Name'])
print(dict_std_1['Age'])
print(dict_std_1['Semester'])
# Getting all the values in form of a list from dictionary
print("----------Getting all the values in form of a list from dictionary----------")
print(dict_std_1.values())
# Inserting new Item (key and value) in dictionary
print("----------Inserting new Item (key and value) in dictionary----------")
dict_std_1["Marks"] = 50
# Printing the dictionary directly after adding the new item of "Marks"
print("----------Printing the dictionary directly after adding the new item of \"Marks\"----------")
print(dict_std_1)
# Removing a value from the dictionary using pop() method
print("----------Removing a value from the dictionary----------")
dict_std_1.pop("Age")
# Printing the dictionary directly after deleting the item using pop() method
print("----------Printing the dictionary directly after deleting the item using pop method----------")
print(dict_std_1)
# Removing a value from the dictionary using popitem() method
print("----------Removing a value from the dictionary----------")
dict_std_1.popitem()
# Printing the dictionary directly after deleting the item using popitem() method
print("----------Printing the dictionary directly after deleting the item using pop method----------")
print(dict_std_1)
# deleting the item from dictionary using del keyword
print("----------Removing an item from the dictionary using del keyword----------")
del dict_std_1["Semester"]
# Printing the dictionary directly after deleting the item using del keyword
print("----------Printing the dictionary directly after deleting the item using del keyword----------")
print(dict_std_1)
# deleting the whole dictionary even from memory using del keyword
print("----------Deleting the whole dictionary even from memory using del keyword----------")
del dict_std_1




