import random
u=0
s=0
a=["stone","papper","scisser"]
for i in range(0,100):
    
        key=input("enter key word")
        b=random.choice(a)
        print(b)
        if key=="stone" and b=="scisser":
            u=u+1
        elif key=="stone" and b=="papper":
            s=s+1
        elif key=="papper" and b=="stone":
            u=u+1
        elif key=="papper" and b=="scisser":
            s=s+1
        elif key=="scisser" and b=="stone":
            s=s+1
        elif key=="scisser" and b=="papper":
            u=u+1
        print("user points",u)
        print("system points",s)
        c=input("do you want to continue yes or no")
        if c=="no":
            break

if u>s:
    print("the winner is user")
else:
    print("the winner is system")





      





















    
