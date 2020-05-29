
"""
If we are importing our own modules then, those modules file should be available for the execution.
There are 3 ways to make module available.
1. Keep the module file in the path of the file in which we are importing.
2. Import it using fully qualified path
3. Add the directory of the module to the "sys.path" list.
"""


'''
We are importing using import module as m, instead of using while Utility name,
we can use U to access the utility methods.
'''

import Utility as U

print ("Utility.pi : ", U.pi)


print("Enter Circle radius : ")
r = float(input().rstrip())

#print("Circle Area with r as ", r, " : ", circle_area(r)) # This generates type error, as circle_area is not defined in this context
print("Circle Area with r as ", r, " : ", U.circle_area(r)) #This should work

U.print_seperator()

print("Enter side of square : ")
s = float(input().rstrip())
print("Square Area with s as ", s, " : ", U.square_area(s)) #This should work

U.print_seperator()

print("Enter length of square : ")
l = float(input().rstrip())

print("Enter bredth/width of square : ")
b = float(input().rstrip())

print("Rectangle Area with l as ",l,", b as ",b," : ", U.recangle_area(l,b))

U.print_seperator()
