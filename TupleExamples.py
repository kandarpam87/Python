
x=10
y=20
z=30
s="string"
f=10.3
dynamictuple = x,y,z,s,f
print("dynamictuple : ", dynamictuple)
print("dynamictuple type: ", type(dynamictuple[0]), type(dynamictuple[1]), type(dynamictuple[2]), type(dynamictuple[3]), type(dynamictuple[4]))



#-------- EMPTY TUPLE -----------
emptyTuple = (None,)
print("type(emptyTuple) = ", type(emptyTuple))
print("emptyTuple = ", emptyTuple)

et = None,

print("type(et) = ", type(et))
print("(et) = ", et)


et1 = ()
print("type(et1) = ", type(et1))
print("(et1) = ", et1)


t1 = 123,"text",123,12.4,'t',123

print("t1 : ", t1)
print("type(t1[4]) = ",  type(t1[4])) # Its a str
print("t1.count(123) : ", t1.count(123)) # Return the repeated time of a value in tuple

print("t1.count(12345) : ", t1.count(12345)) # Returns 0

print("t1.index(123) : ", t1.index(123)) # Returns 0

print("t1.index(123) : ", t1.index(123, 0))  # Returns 0

print("t1.index(123) : ", t1.index(123, 1))  # Returns 2
print("t1.index(123) : ", t1.index(123, 3))  # Returns 5
