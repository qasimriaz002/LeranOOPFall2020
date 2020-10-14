# Here in this part of lab 3 we are going to see how we can use dictionaries with the loops and lists

# Creating dictionary containing the student record

counter = 1
# Inserting items (keys, values) in dictionary using the loop.
dict_std_1 = {'Name': 'Bilal', 'Age': 20, 'Marks': 25}
# while counter < 3:
#     key = input("Enter the key # " + str(counter) + ": ")           #Enter the key # 1: Name
#     value = input("Enter the value of Key: "+ str(key) + ": " )     #Enter the value for Name: Qasim
#     dict_std_1[key] = value;
#     counter = counter + 1
# Getting items (keys, values) from dictionary using the loop.
for keys in dict_std_1.values():
    # print()
    print(keys)


