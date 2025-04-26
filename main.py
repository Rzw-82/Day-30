#FileNotFound

try:
    file= open("text.txt")
    print(file.read())
except:
    