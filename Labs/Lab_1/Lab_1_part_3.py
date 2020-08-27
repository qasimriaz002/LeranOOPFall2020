# Here we will use the dictionaries with the list
# We will create the record of 5 students in the different 5 dictionaries
# Then we will add all of the these three dictionaries in the list containing the record of all student

# Creating the dictionaries
stdDict_1 = {"name": "Bilal", "age": 21, "rollno": "BSDS-001-2020"}
stdDict_2 = {"name": "Ahsan", "age": 19, "rollno": "BSDS-002-2020"}
stdDict_3 = {"name": "Hassan", "age": 22, "rollno": "BSDS-003-2020"}
stdDict_4 = {"name": "Kashif", "age": 24, "rollno": "BSDS-004-2020"}
stdDict_5 = {"name": "Talha", "age": 18, "rollno": "BSDS-005-2020"}

# Creating the list
listStudent_Record = [stdDict_1, stdDict_2, stdDict_3, stdDict_4, stdDict_5]

# Getting the data from the list
print(listStudent_Record)

print("-----------------------------")
# Getting the record of first dictionary from list
print(listStudent_Record[0])

print("-----------------------------")
# Getting the name of student from 1 dictionary from list
print(listStudent_Record[0]["name"])

print("-----------------------------")
# Getting the names of all the students present in all the dictionaries in the list
print(listStudent_Record[0]["name"])
print(listStudent_Record[1]["name"])
print(listStudent_Record[2]["name"])
print(listStudent_Record[3]["name"])
print(listStudent_Record[4]["name"])


