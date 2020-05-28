

#-------- INT -----------
x =10 #id could be 1793390656

print("x = ", x, "id(x) = ", id(x), "type(x) = ", type(x))

x = x + 10 #now of id(x) will not be 1793390656, this will get changed.

print("x = ", x, "id(x) = ", id(x), "type(x) = ", type(x))

#-------- STR -----------
s = "First string";
print("s = ", s, "id(s) = ", id(s), "type(s) = ", type(s))

s = s + " appending this string." # same as int, id of s will be updated.
print("s = ", s, "id(s) = ", id(s), "type(s) = ", type(s))


#-------- TUPLE -----------
t1 = (50,)

print("Type of t1 = ", type(t1), "id(t1) = ", id(t1))
print("t1[0] = ", t1[0], "id(t1[0]) = ", id(t1[0]), "type(t1[0]) = ", type(t1[0]))

'''
t1[1] = 100 #This causes TypeError, tuple does not support item assignment.
print("t1[1] : ", t1[1])
'''
