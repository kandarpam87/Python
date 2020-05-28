def square(x):
    return x**2

squarefun = lambda x : x ** 2

for i in range(1,10):
    print(square(i))

print('-'*40)

print(squarefun(5))

def str_upper(s):
    if(type(s) == str):
        return s.upper()
    else:
        return s


# See how braces () makes the change
print(lambda s : str_upper(s)("these are lower case letters")) # This prints function pointer details
print((lambda s : str_upper(s))("these are lower case letters")) # This prints the output string


s = lambda s : str_upper(s) ("upper case letters")
print(s) # This prints the function pointer

s = (lambda s : str_upper(s)) ("upper case letters")
print(s) # This executes the function and prints the output string
