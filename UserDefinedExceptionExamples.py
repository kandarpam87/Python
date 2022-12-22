
class MyException (Exception): #inheritance 
    pass;


agelist = [18, 22, 30]

for i in agelist:
    try:
        if(i < 21):
            raise MyException("Age is less than expected, Not allowed :( ")
        print("Allowed :) ")
    except MyException as e:
        print(e)


