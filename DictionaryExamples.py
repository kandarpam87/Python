#Dictionary is a key value pair


d = {}

print("type(d) : ", type(d)) #class<dict>

d1 = {'name' : 'ABC', 'id' : 1, 'name' : 'PQR', 'id' : 2} # overwrite the first entry for the 'name'
print(d1)

print('-'*40)

d1 = {'name' : 'string', (1,2,3) : [9,8,7,6,5], 1 : 'integer', 3.4 : 'float'}

#Get the values using keys
print(d1['name'])
print(d1[(1,2,3)][3])

d1[(1,2,3)][3] = 4444
print(d1)
print('-'*40)


#Check the existnace
print('name' in d1) #True
print('-'*40)

#Gettig the Items, Keys and Values in seperately
print("Items : ", d1.items()) #dict_items([('name', 'string'), ((1, 2, 3), [9, 8, 7, 4444, 5]), (1, 'integer'), (3.4, 'float')])
print("Keys : ", d1.keys()) #Keys :  dict_keys(['name', (1, 2, 3), 1, 3.4])
print("Values : ", d1.values()) #Values :  dict_values(['string', [9, 8, 7, 4444, 5], 'integer', 'float'])

#Following lines gives error
'''
print("Keys : ", d1.keys()[0]) # TypeError: 'dict_keys' object is not subscriptable
print("Values : ", d1.values()[0])
'''
print('-'*40)


#Get the keys and sort them and save in a list
d1 = {'name' : 'ABC', 'id' : 1, 'desc' : 'Test data', 'misc' : "Relly misc.."}
keysList = list(d1.keys())
print("keysList before sorting : ", keysList)
keysList.sort()
print("keysList after sorting : ", keysList)

print('-'*40)

#Get the dictionary elements using keys list
for i in range(len(keysList)):
    print(d1[keysList[i]])

print('-'*40)

#Update the dictionary using keys
for i in range(len(keysList)):
    if(type(d1[keysList[i]]) == str) :
        d1[keysList[i]] = d1[keysList[i]].upper()

print(d1)
print('-'*40)


#Using for loop
# it iterates on keys of dictionary
for i in d1:
    print(i)
print('-'*40)
