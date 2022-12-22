
'''
ClassName.  -> this will gives the list of available attributes and functions for the class

Ex: str.
'''

s1 = "Welcome to PSL"

print(s1.decode())

print("s1 = ", s1, ", id(s1) = ", id(s1))

print("""s1.find("PSL") = """, s1.find("PSL")) #Retruns 11
print("""s1.find("123") = """, s1.find("123")) #Retruns -1

'''
print(s1.index("psl")) #Gives ValueError
'''

#Repeate operator 
# ""*number

print("-"*40)

    
s2 = s1.upper()
print("s1 = ", s1, ", id(s1) = ", id(s1))
print("s2 = ", s2)
