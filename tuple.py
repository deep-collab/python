My_tuples = (1, 'string', 4.5, True)
print(My_tuples[1])
print(My_tuples.count('string'))


##sets
set_a = {1, 2, 3, 4, 5,}
set_a.add(6)
set_a.remove(6)
set_a.discard(6)
print(set_a)

set_b = { 4, 5, 6, 7, 8}

print(set_a.union(set_b))
print(set_a | set_b)

#inetrsection
print(set_a.intersection(set_b))
print(set_a & set_b)

#set-deiffference
print(set_a.difference(set_b))
print(set_a - set_b)

#symetrical difference
print(set_a.symmetric_difference(set_b))
print(set_a^set_b)


###dictitonary
#key: value pair
my_d = {1: 'test',}

print(type(my_d))