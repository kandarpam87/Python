
#Open a file in write mode
f = open("FirstTextFile.txt", 'w')

print(type(f))

#This gives available functions of f object
#print (dir(f))

#Writing data into file.
print("Current postion : ", f.tell())
f.write("This is the first line of the file.\n")
print("After writing first line, current postion : ", f.tell())

f.write("This is the second line of the file.\n")
print("After writing second line, current postion : ", f.tell())

#Close file
f.close()


#Reading data from file

#f = open("FirstTextFile.txt", 'r') #Can also be used
f = open("FirstTextFile.txt")

while True:
    str = f.read()
    print ("Current position : ", f.tell())
    if(str):
        print (str)
    else :
        break;

f.close();
