a=eval(input("a=>>"))
y=0
while a>0:
    b=a%10
    print(b)
    a=int( a/10) 
    y=y+b
print(y)

