str=list(map(str,input("enter the string").split()))
c=[]
c.append(str[0])
for i in range(0,len(str)):
   if str[i] in c:
      continue
   else:
      c.append(str[i])
print(c)
c.sort()
for j in range(0,len(c)):
   count=0
   for k in range(0,len(str)):
      if c[j]==str[k]:
         count=count+1
      else:
         continue
   print("frequency of",c[j],"is:",count)