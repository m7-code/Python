def printSuccess():
    """
    this function print the message
    """
    print("task is successful")

printSuccess()

help(printSuccess)

def message(msg):
    if isinstance(msg,str):
        print(msg)
    else:
        print("this is not string")

message(2)

def mypow(a,b):
    c=a**b 
    print(c)

mypow(2,3)


def mypow(a,b): # due to return we access them outside the function
    c=a**b 
    return c

d = mypow(2,3)
print(d)

# we can return multiple values

def ret():
    a = 2
    b = 3
    c = "something"
    return a,b,c 

print(ret())

# for geting many arguments

def add(*args): #this *arg allow that we give multiple arguments that we want
    sum =0
    for i in range(len(args)):
        sum +=args[i]
    return sum

print(add(2,3,4,5,6,7,8,9))  

# printing Dictionaries and taking many arguments

def f(**c): # here we use double * instead of single
    for x in c:
        print("name = ",x,"and value = ",c[x])
        
f(a = 3, b="b",c = "yes" )

#defalt falue
 
def defalt(sum=0):
    print(sum)

defalt()

