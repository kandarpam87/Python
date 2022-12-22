'''
import urllib.request

with urllib.request.urlopen('http://google.in') as response:
    html = response.read()

print(html)
'''
import os
import glob
#print(dir(os))
#print (glob.glob('*.py'))

p = input("eNTER SOMETHING : ")

print(p)

