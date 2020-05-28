# USING THE VARIABLE PARAMETER FUNCTIONS, WE ACHIEVE 'OVERLOADING'

#Define a function with default parameters this returns nothing (None)
def print_seperator(char = '-', repeat_count = 40) :
    print(char*repeat_count)

def get_len(s):
    return len(s)

def func_with_one_default_parameter(first, second = "Second") :
    print (first, " - ", second)

def func_with_variable_parameter_using_tuple(arg1, arg2 = "Second", *x) :
    ''' This can catch the extra variable, but it cannot catch the parameters with the keywords. '''
    print("arg 1 : ", arg1)
    print("arg 2 : ", arg2)
    print("Rest of the variables : ", x)

    for i in x :
        print (i)

def func_with_variable_parameter_using_dictionary(arg1, arg2 = "Second", **x) :
    print("arg 1 : ", arg1)
    print("arg 2 : ", arg2)
    print("Rest of the variables : ", x)

    for i in x :
        print (i, " : ", x[i])

def func_with_variable_parameters(arg1, arg2 = 'Second', *x, **y) :
    print("arg 1 : ", arg1)
    print("arg 2 : ", arg2)
    print("Rest of the non-keyword variables : ", x)
    for i in x :
        print (i)

    print("Rest of the keyword variables : ", y)
    for i in y :
        print (i, " : ", y[i])


##############################
# Execution starts from here
##############################
print("First line")
print_seperator()
print("Second line")
print_seperator('=', 50)


#print_fun() # This gives Name Error as we don't have print_fun

#print_seperator('-',40,50) #This will give Type Error.


#Calling a function with a return value
print("""" Lenght of "ABCDEFGHIJKLMNOPQRSTUVWXYZ" """, get_len("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

#Calling a function with keyword parameters
print_seperator (repeat_count = 60, char = '*')

print_seperator()

#Calling a default parameter function
func_with_one_default_parameter("First", "Second") # Works
func_with_one_default_parameter("First") # Works

func_with_one_default_parameter(first="Second", second='First') # Works
#func_with_one_default_parameter('First', first='Second') # Type error got multiple values for same parameter

print_seperator()

#Calling function with variable parameter without keywords
func_with_variable_parameter_using_tuple ("First", "Second", "Third", "Fourth", "Firth")
print_seperator('*', 10)
func_with_variable_parameter_using_tuple (1, 2, 3, 4, 5)
print_seperator('*', 10)
func_with_variable_parameter_using_tuple ("One")

print_seperator()

#Calling function with variable parameters with keywords
func_with_variable_parameter_using_dictionary('First', 'Second', arg3='Arg3', arg4='Arg4')
print_seperator('*', 10)
func_with_variable_parameter_using_dictionary('One')


print_seperator()
#Calling functions with varialbe parameters with and without keywords
func_with_variable_parameters("First", "Second", "Third", "Fourth", "Firth", arg6='Arg6', arg7='Arg7')
print_seperator('*', 10)
func_with_variable_parameters("One")

#func_with_variable_parameters("First", "Second", "Third", arg6='Arg6', "Fourth", arg7='Arg7', "Firth") #This will generates the Syntax error

print_seperator('*', 10)
d1 = {'Key' : 'Value'}
# Here d1 will be catch by tuple argument (i.e., x)
func_with_variable_parameters("One", "Two", d1)

print_seperator('*', 10)
# Here d1 will be catch by dictionary argument (i.e., y)
func_with_variable_parameters("One", "Two", **d1)

