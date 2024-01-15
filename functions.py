list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(*list1)
print(list1, sep=" ")

#insert function
list1.insert(len(list1), 10)
print(list1, sep=" ")

#Append function
list1.append(11)
print(list1, sep=" ")

#extend function
list1.extend([12, 13, 14, 15])
print(list1, sep=" ")

#remove1
#1. pop
list1.pop(13)
print(list1, sep=" ")

#2. del
del list1[2]
print(list1, sep=" ")

#to iterate
