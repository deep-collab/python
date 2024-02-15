import re

test_string = '123abc467abc123'
pattern = re.compile(r"abc")
matches = pattern.finditer(test_string)
match =  pattern.match(test_string)
match2 = pattern.findall(test_string)
match3 = pattern.search(test_string)
#            #OR
# matches = re.finditer(r"abc", test_string) 

# for match in matches:
    #match(), search(), findall() 
print(match)
print(match2)
print(match3)

 
# # a = r"\tHello"
# # print(a)
