"""
If we are importing our own modules then, those modules file should be available for the execution.
There are 3 ways to make module available.
1. Keep the module file in the path of the file in which we are importing.
2. Import it using fully qualified path
3. Add the directory of the module to the "sys.path" list.
"""

#import sys
#sys.path.append('D:\Learning\Python\MyOwnPackage')

from MyOwnPackage import *

print(pi)


print_error("This is error message generated from " + __file__)
