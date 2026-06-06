import csv
# f = open("store.txt", "r")
# content = f.read()
# print(type(content))
# print(content)
# f.close()

# f = open("C:/Users/Acer/Desktop/Python/Python_By_Komal_Sir")
# content = f.read()
# print(type(content))
# print(content)
# f.close()


# f = open(r"C:\Users\Acer\Desktop\Python\Python_By_Komal_Sir")
# content = f.read()
# print(type(content))
# print(content)
# f.close()

# f = open("C:\\Users\\Acer\\.openjfx\\Documents\\Python\\Python_By_Komal_Sir")
# content = f.read()
# print(type(content))
# print(content)
# f.close()

data = [["name", "age"],
        ["Ram", 18],
        ["Shyam", 19]
]

with open ("store.txt", "w", newline="") as file:
    write = csv.writer(file)
    write.writerows(data)
    

