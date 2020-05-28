#To create a new list with existing list

l1 = [1,2,3,4,5,-4,-3,-2,-1]
newl1 = []

for i in l1:
    newl1.append(i * 2)

print("First list : ", l1)
print("Newlist : ", newl1)

print('-'*40)

#The same can be done by expressions (list comprehension)
newExprl1 = [x * 2 for x in l1]
print("newExprl1 : ", newExprl1)

#We can do with a condition as well
newExprl2 = [x ** 2 for x in l1 if x>0]
print("newExprl2 : ", newExprl2)
print('-'*40)


l2 = ['abc','bcd','cde','def','efg','123', 'ab123']
upprel2 = [s.upper() for s in l2 if s.isalpha()]

print("l2 : ", l2)
print("upprel2 : ", upprel2)


#Dictionary comprehesion
l3 = [1,2,3,4,5,6,7,8,9]
squareD = {x:x**2 for x in l3}
print("List l3 : ", l3)
print("Dictionary generated from l3 : ", squareD)
