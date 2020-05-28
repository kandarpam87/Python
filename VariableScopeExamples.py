def func_with_variable_scope() :
    var1 = 1
    var2 = 2

def func_with_global_var() :
    global var3
    var3 = 3
    var4 = 4


var1 = "One"

global var2
var2 = "Two"
# This is the global varialbe and updated in func_with_global_var()
var3 = "Three"

var4 = "Four"

func_with_variable_scope()
print ("var1 = ", var1, " var2 = ", var2)

func_with_global_var()
print ("var3 = ", var3, " var4 = ", var4)
