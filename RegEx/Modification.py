#split, sub
import re

My_string = 'hello world, you are the best world'

pattern = re.compile(r"world")
matches = pattern.sub("planet", My_string)
print(matches)