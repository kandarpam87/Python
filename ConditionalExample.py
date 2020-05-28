# if <condition> :
#elif <condition> :
#else:

print("START !!!")
x = 10
idOfX = id(x)
if type(x) == int :
    print ("x is an integer.", " : x = ", x)
    x = '*'*40 # this is repeat operator, this repeats the sequence.

if idOfX == id(x):
    print("Nothing changed...")
else:
    print("x is updated")
        

if type(x) == int:
    print ("Some issue")
elif type(x) == str:
    print("x is now string", " : x = ", x)
else :
    pass; #This will continue the control, if u wanted to implement empty block, just say 'pass'

print("END !!!")
