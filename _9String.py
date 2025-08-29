s = "a b c"
t = "d e f"
v = s+" "+t
print(v)

multiLineString = """hello how are you ok 
what are you doing today
is today is sepacial"""

print(multiLineString)

print("""hello how are you ok 
what are you doing today
is today is sepacial"""
)

a = "this is string"
print(a[0]) #access the very first word
print(a[5:8]) #here 5 is include and 8 is not include
print(a[-1]) #negative indexing

#reverse string
print(a[::-1])

b= "ABC"

print(b.lower())
print(a.upper())

x = "a..b"
print(x.replace(".","*"))

print("abc\ndef")