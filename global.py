
# 5
# global Defines variables as applicable to wider ranges
# the disadvantage in global is to Prevent the situation where in long scripts it will be difficult for us to understand why we get different results than expected.
# we will get an Error because of using x in def foo, Python assumes that x is local throughout the function because it’s assigned within the function.
# המשך: This causes a problem when print(x) is executed because x is referenced before it is assigned