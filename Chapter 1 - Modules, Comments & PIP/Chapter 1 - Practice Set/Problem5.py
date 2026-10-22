import os

# Here, . means current directory
directory = "." 

# Fetch the content of the directory using listdir function
contents = os.listdir(directory)

# print the content using for loop
for item in contents:
    print(item)