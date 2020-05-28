
import copy
# List is an immutable object.
# it will be created using square brackets []

#Homogenious list
l1 = [1, 2, 3, 4]

print("type(l1) = ", type(l1))
print("l1 = ", l1)


#Hetrogenious list

l2 = [1,2,"str",3.0,4.0,'char']
print("type(l2) = ", type(l2))
print("l2 = ", l2)
print("id(l2) = ", id(l2))

l2.append(999)
l2.append("Appended string")
print("l2 = ", l2)
print("id(l2) = ", id(l2)) # this is same as the previous id of l2.

print("l2 length : ", len(l2))
l2[len(l2)-1] = "Updated value at the end of list"

print("l2 = ", l2)
print("id(l2) = ", id(l2)) # this is same as the previous id of l2.
print("l2 length : ", len(l2))

print("Before modification : l2[2] = ", l2[2])
l2[2] = "New Str"
print("After modification : l2[2] = ", l2[2])


print("After update l2 = ", l2)
print("id(l2) = ", id(l2)) # this is same as the previous id of l2.


newl2 = l2; #Shallow copy
print("id(newl2) = ", id(newl2)) # this is same as the previous id of l2.

l2.append(998)

print("l2 = ", l2)
print("newl2 = ", newl2)

#Deep copy from the copy module.
deepcopyl2 = copy.deepcopy(l2)
print("deepcopyl2 = ", deepcopyl2)
print("id(deepcopyl2) = ", id(deepcopyl2))

l2.append(997)

print("l2 = ", l2)
print("deepcopyl2 = ", deepcopyl2)

# Other copying way is
othercopyl2 = l2[:]
print("othercopyl2 = ", othercopyl2)
print("id(othercopyl2) = ", id(othercopyl2))

l2.append(996)

print("l2 = ", l2)
print("othercopyl2 = ", othercopyl2)


#---------------- Inner list----------------

t1=10,20,30,["this","is",'a','inner','list']
print(t1)

print(t1[3])

print(t1[3][4])

t1[3].append("Appended string")

print(t1[3])

print(t1[3][5])

t1[3][5] = t1[3][5].upper()

print(t1[3])


print('-'*40)

#Sorting the list sort & sorted
l1 = [23,45,2,32,12,665,100,443,234,643,55,77,879,78]
print("list l1 : ",l1)

l2 = sorted(l1)

print("l1 After sorted : ", l1)
print("l2 generated from l1.sorted() : ", l2)

l1.sort()
print("l1 after sort : ", l1)
