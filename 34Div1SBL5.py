# Write function
f = open('myfile.txt', 'w')
str = input("Enter text : ")
f.write(str)
f.close()

# Append Function
f = open('myfile.txt', 'a')
str = input("Enter text : ")
f.write(str)
f.close()

# Read Function
f = open('myfile.txt', 'r')
str1 = f.read()
print("The text in the file is : ", str1)
f.close()

# Accessign string from a specific position
f = open('myfile.txt', 'r')
f.seek(4)
print("The seeked string from 4th byte is ", f.read())
f.close()

#ReadLine
f = open('myfile.txt', 'r')
print("The first line is : ", f.readline())
f.close()
