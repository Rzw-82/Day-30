#FileNotFound

try:
    file= open("text.txt")
    print(file.read())
except:
    file = open(file="text.txt","w")
    file.write("something")
    