x=3
print(type(x))

#variables
#1,2,3,4,..... => int
#2.3,3.4,.... => float
# "abcd" ..=> string

k=4
c=2+ 4* k
print(type(c))
print(c)

for var_name, val in list(globals().items()):  # <-- make a list copy
     if not var_name.startswith("c"):
        print(f"{var_name} ({type(val)}): {val}")


#operators

#+,-,*./,% etc

a=2
b=3
print(a+b)

a,b=2,3
x=a+b
print(x)
print(type(x))

y=2**9
print(y)