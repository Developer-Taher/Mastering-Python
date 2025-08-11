# -----------------------------------------
# -- variables --
# ---------------
# syntax => [varable name ] [assifnment operator] [value]
# example => x = 5
# syntax => [varable name ] [assifnment operator] [expression]
# example => x = 5 + 3
# syntax => [varable name ] [assifnment operator] [list]
# example => x = [1, 2, 3, 4, 5]
# syntax => [varable name ] [assifnment operator] [dictionary]
# example => x = {"name": "John", "age": 30}
# syntax => [varable name ] [assifnment operator] [set]
# example => x = {1, 2, 3, 4, 5}
# syntax => [varable name ] [assifnment operator] [tuple]
# example => x = (1, 2, 3, 4, 5)
# syntax => [varable name ] [assifnment operator] [string]
# example => x = "Hello, World!"
# syntax => [varable name ] [assifnment operator] [boolean]
# example => x = True
# syntax => [varable name ] [assifnment operator] [None]
# example => x = None
# syntax => [varable name ] [assifnment operator] [function]
# example => x = len
# syntax => [varable name ] [assifnment operator] [lambda function]
# example => x = lambda x: x * x
# syntax => [varable name ] [assifnment operator] [class]
# example => x = MyClass
# syntax => [varable name ] [assifnment operator] [object]
# example => x = MyClass()
# syntax => [varable name ] [assifnment operator] [module]
# example => x = math
# syntax => [varable name ] [assifnment operator] [package]
# example => x = math
# syntax => [varable name ] [assifnment operator] [import]
# example => x = from math import sin
# syntax => [varable name ] [assifnment operator] [import from]
# example => x = from math import sin
# syntax => [varable name ] [assifnment operator] [import all]
# example => x = from math import *
# syntax => [varable name ] [assifnment operator] [import specific]
# example => x = from math import sin, cos
# syntax => [varable name ] [assifnment operator] [import from specific]
# example => x = from math import sin, cos
# syntax => [varable name ] [assifnment operator] [import from package]
# example => x = from math import sin, cos
# syntax => [varable name ] [assifnment operator] [import from package specific
# example => x = from math import sin, cos
# syntax => [varable name ] [assifnment operator] [import from package all
# example => x = from math import *

# -----------------------------------------
# name convention and rules
# -----------------------------------------
# variable names should be descriptive and follow the snake_case convention
# [1]variable names should not start with a number 1 2 3 4 
# [2]variable names should not contain special characters except for underscores @ - = 
# [3]variable names should not be too long
# [4]variable names should be consistent throughout the code
# variable names should be in lowercase
# variable names should not be a reserved keyword
# variable names should not be a built-in function
# variable names should not be a class name
# variable names should not be a module name
# variable names should not be a package name
# variable names should not be a function name
# variable names should not be a lambda function

myvariable = 'normal'
myVariable = 'camel case'
my_variable = 'snake_case'
print(myvariable)
print(myVariable)
print(my_variable)

#reserved words
help("keywords")

a,b,c = 1,2,3

print(a)
print(b)
print(c)