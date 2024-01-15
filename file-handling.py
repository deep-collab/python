# #file handling
# with open('hello.txt', mode='r') as file:
#     data = file.readline()

# print(data)

# #creating-files
# with open('newfile.txt', mode='a') as file:
#     file.writelines("this is the new file created")

# #read
import random

f = open('newfile.txt',mode="r")
f_content_ = f.read();
# print(f_content_);
f_content_list = f_content_.split('\n')
print(random.choice(f_content_list))
f.close()