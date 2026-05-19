with open ("geek.txt","w") as file:
    file.write("hii world \n")
    file.write("writin to file by overwriting")
print("written to file")
with open ("geek.txt","r") as file:
    print(file.read())