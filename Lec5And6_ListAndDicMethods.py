# Here in this lecture we are going to see what the important built in methods for lists in python

list1 = [11, 12, 13]
list2 = list1.copy()





list1.append(14)    #[11, 12, 13, 14]
list1.append(12)
# list1.append(100)
print(list1)
print(list2)

list1.insert(1,56)
list1.sort()

print(list1)

print(len(list1))
print(len(list2))

list1.pop()
print(list1)

# list1.remove(12)
# print(list1)

print(list1.index(12))

print(list1[1])
list1[1] = 99
print(list1)





# stud_marks = []