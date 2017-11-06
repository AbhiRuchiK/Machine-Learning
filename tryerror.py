l=[1,2,3,0,0,1]
i = 0
while i < len(l):
   if l[i] == 0:
       l.pop(i)
   else:
       i += 1

print(l)
