import numpy as n
#a= [int(x) for x in input("Enter values : ").split("")]
a=list(map(int,input().split()))

i=1
j=0
s= n.size(a)
    
while i != (n.size(a)):
    j=i
    while j!=0:
        if a[j-1] > a[j]:
            t=a[j-1]
            a[j-1] = a[j]
            a[j] = t
            j=j-1
        else:
            break
    i=i+1
    
print("sorted values is: {}".format(a))




