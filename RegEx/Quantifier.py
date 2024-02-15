import re

test_string = "hello 123_"


pattern = re.compile(r"\d{1,3}")
matches = pattern.finditer(test_string)
for match in  matches:
    print(match)