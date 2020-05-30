

#basic function
def function1():
    print("my first function")

#function with arguments
def function2(arg1,arg2):
    print(arg1," ", arg2)

#function with return
def cube(x):
    return x*x

#function with default argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

#function1()
#print(function1())
#print(function1)

#function2("arg1","arg2")
#print(function2(2,3))

#print(cube(3))

#print(power(3))
print(power(2,3))
#print(power(x=3,num=2))

#print(multi_add(4, 5, 10, 4))