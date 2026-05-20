with open("newtest.txt", "r+") as file:
    content = file.read()

    file.write("\n this is write and read file")

print(content)