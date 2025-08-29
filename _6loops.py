# while loop

# n = int(input("Enter the number"))
# i = 1
# while i<=n:
#     print(i)
#     i += 1
# print("done")



# i=1
# while True:
#     if  i%9==0:
#         print("inside if")
#         break
#     else:
#         i += 1
#         print("inside else")
#         continue
    
# print("done")


# for loop

l =[]
for i in range(10):   #(1,10,2)=>here we are saying that print 1 to 10  with jump of 2
    print(i+1)
    l.append(i**2)
print(l)

y={"a":1,"b":2}
for i in y:
    print(i,y[i])

# nested loop

l = [1,2,3,5,4]
for j in range(len(l)):
    m = l[j]
    idx = j
    c = j 
    for i in range(j,len(l)): #this loop find the minimum number
        if l[i]<m:
            m=l[i]
            idx=c 
        c+=1
    temp =l[j]
    l[j]=m
    l[idx]=temp
print(l)