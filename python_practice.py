Python
j=int(input("enter num"))
cnt=0
for i in range(1,j+1):
    if(j%i==0):
        print(f"{i} is factor of {j}")
        cnt+=1
if cnt==2:
    print(f"{j} is a prime")
print(cnt)
for i in range(20,31):
    cnt=0
    for j in range(1,i+1):
        if(i%j==0):
            cnt+=1
    if cnt==2:
        print(f"{i} is prime")
# def add():
#     x=10
#     y=20
#     z=x+y
#     print(z)
# add()
# def add():
#     x=10
#     y=20
#     z=x+y
#     return z
# #a=add()
# print(add())
# def add(x,y):
#     z=x+y
#     return z
# #a=add()
# print(add(10,20))
def add(x,y):
    z=x+y
    print(z)
#a=add()
add(10,20)
ef iseven(x):
    if(x%2==0):
        return 1
    else:
        return 0
a=iseven(10)
if(a):
    print("even")
else:
    print("odd")


def iscnt(x):
    cnt=0
    for i in range(1,x+1):
        if(x%i==0):
            cnt+=1
    return cnt
a=iscnt(10)
print(a)

def isprime(x):
    cnt=0
    for i in range(1,x+1):
        if(x%i==0):
            cnt+=1
    if cnt==2:
        return 1
    else:
        return 0
a=isprime(10)
if a:
    print("prime")
else:
    print("not prime")
print(a)

def area(x,y):
    return x*y
a=int(input("enter length:"))
b=int(input("enter breadth:"))
print(area(a,b))
