with open("/Users/wooo_/OneDrive/Desktop/my_text.txt") as file:
    contents = file.read()
    print(contents)

# relative path
try:
    fp = open("my_text.txt", "r")
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print("Please check the path.")