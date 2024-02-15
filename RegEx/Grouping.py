import re

My_string = """
Mr Simpson
hello world
Mr Deepak
1223
2020-05-20
Mr. Brown
Ms Smith
Mr. T
deepakshetty1990@gmail.com
prabhu5686@gmail.com

"""

pattern = re.compile(r"([a-zA-Z0-9-]+)@([a-zA-Z-]+)\.([a-zA-Z]+)")
matches = pattern.finditer(My_string)
for match in matches:
    print(match)