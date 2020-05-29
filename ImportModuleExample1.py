
"""
If we are importing our own modules then, those modules file should be available for the execution.
There are 3 ways to make module available.
1. Keep the module file in the path of the file in which we are importing.
2. Import it using fully qualified path
3. Add the directory of the module to the "sys.path" list.
"""



import Utility

print ("Utility.pi : ", Utility.pi)


print("Enter Circle radius : ")
r = float(input().rstrip())

#print("Circle Area with r as ", r, " : ", circle_area(r)) # This generates type error, as circle_area is not defined in this context
print("Circle Area with r as ", r, " : ", Utility.circle_area(r)) #This should work

Utility.print_seperator()

print("Enter side of square : ")
s = float(input().rstrip())
print("Square Area with s as ", s, " : ", Utility.square_area(s)) #This should work

Utility.print_seperator()

print("Enter length of square : ")
l = float(input().rstrip())

print("Enter bredth/width of square : ")
b = float(input().rstrip())

print("Rectangle Area with l as ",l,", b as ",b," : ", Utility.recangle_area(l,b))

Utility.print_seperator()
