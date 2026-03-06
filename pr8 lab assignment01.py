source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

f1 = open(source, "r")
data = f1.read()
f1.close()

data = data.upper()

f2 = open(destination, "w")
f2.write(data)
f2.close()

print("Content copied in uppercase successfully")