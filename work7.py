a=eval(input("enter the monthly saving amount"))
s=0
for i in range(6):
    b=a*(1+0.00417)
    a=b
    s=s+b        
    print(s)
