#This is a utility file with having some common functions.

import math

pi = math.pi

def print_seperator(char = '-', count = 40):
    print(char * count)


def circle_area(r = 1):
    return pi * r**2

def square_area(s = 1):
    return s**2

def recangle_area(l =1, b = 1) :
    return l * b

def print_module_name() :
    print ("Current Module Name : ", __name__)



def get_fibonocci_list(num):
    retlist = [1, 2]
    for i in range(1, num-1):
        retlist.append(retlist[len(retlist) - 1] + retlist[len(retlist) - 2])
    return retlist

def fib(n):
    if(n==0):
        return 1
    if(n==1):
        return 2
    else:
        return fib(n-1) + fib(n-2)

def get_fibonocci_list_using_recursion(num):
    retlist = []
    for i in range(num):
        retlist.append(fib(i))
    return retlist
    
    

print_seperator()
print_module_name()
print("Fibonocci : ", get_fibonocci_list(10))
print("Fibonocci using recursion: ", get_fibonocci_list_using_recursion(10))
print_seperator()

if(__name__ == "__main__"):
    print("Circle Area with r as 5 : ", circle_area(5))
    print("Square Area with s as 5 : ", square_area(5))
    print("Rectangle Area with l as 5, b as 6 : ", recangle_area(5,6))

print("---------- End of Utility ----------")

