'''
We are importing using from <filename> import *, this import all the modules
as the local modules of the current module.
Hence don't need to use the Utility as prefix for the utility functions.
'''

from Utility import  *

print ("Utility.pi : ", pi)


print("Enter Circle radius : ")
r = float(input().rstrip())

print("Circle Area with r as ", r, " : ", circle_area(r))

print_seperator()

print("Enter side of square : ")
s = float(input().rstrip())
print("Square Area with s as ", s, " : ", square_area(s)) #This should work

print_seperator()

print("Enter length of square : ")
l = float(input().rstrip())

print("Enter bredth/width of square : ")
b = float(input().rstrip())

print("Rectangle Area with l as ",l,", b as ",b," : ", recangle_area(l,b))

print_seperator()
