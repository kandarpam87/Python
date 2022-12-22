'''
Following keywords used for Exception Handling:
try
except -> similor to catch
finally
raise -> similar to throw
'''

# open('nonexistingfile.txt') #This trhows exception of type FileNotFound as there is no file

try:
    open('nonexistingfile.txt')
except FileNotFoundError as f:
    print("Observed Exception : ", f)

finally:
    print("End !!!")


def read_float():
    retval = None
    try:
        print("Please enter a float number : ")
        retval = float(input())
    except ValueError as e:
        print('Observed exception while converting : ', e)
        print('Returning 0.0')
        retval = 0.0
    finally:
        return retval


r = read_float()
print(r)



def finally_example():
    try:
        try:
            f = open("nonexistingfile.txt")
        finally:
            print("This finally is for the inner try block !!!")
    except TypeError as e:
        print("Error observed : ", e)
    finally:
        print("This finally is for outer try block !!!")

print("Calling finally_example method ...")
finally_example();
