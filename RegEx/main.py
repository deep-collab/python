# Methods to search for matches
# import re
# test_string = "123abc456789abc123ABC"

# pattern = re.compile(r"abc")
# matches = pattern.finditer(test_string)

# for match in matches:
#     print(match.group())



# #meta characters
# import re

# test_string = "123abc456789abc123ABC"

# pattern = re.compile(r"ABC$")
# matches = pattern.finditer(test_string)


# for match in matches:
#     print(match)


import re

test_string = "hello 123_ heyho hohey"

pattern = re.compile(r"\Bhey")
matches = pattern.finditer(test_string)


for match in matches:
    print(match)