#Set created using {}
#It support only unique values
#Storage is random

s = {"abc",9,8,7,4,5,3,5,6,9,8,7,1,3,2,"bbc", "Abc", "Bbc"} # it removes duplicates and print in sorted order.

print("Set s : ", s) 

print('-'*40)
'''
print("Value at Index 1 : ", s[1]) # This gives TypeError 
'''

#Iterate and print set values
for n in s:
    print(n)


#Set cannot have a list as an element.
'''
s1 = {2,1,4,2, [2,3,4,5]} #TypeError, Hashvalue for list cannot be added to set. Throws unhashable type list
print(s1)
'''
print('-'*40)

# List can have set as an element.
l1 = [1,2,3, {1,2,3}]
print(l1)
print('-'*40)

#Set union
s1 = {1,2,3}
s2 = {2,3,4}

print("First set : ", s1)
print("Second set : ", s2)

s3 = s1|s2
print("Set union : ", s3)

#Set intersection
s4 = s1&s2
print("Set Intersection : ", s4)


#Update
#set.update -> is Union


s1 = {1,3,5}
print(s1)

s1.add(2)
s1.add(4)

print(s1)

s1.clear()
print(s1)

#None is kind of null in other languages
s1 = {None, None}
print(s1)



del s1
print(s1) #Name error as s1 is delete and cannot reference it.

