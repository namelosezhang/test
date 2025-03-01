l=input()
x=int(l)
a=x//1000000
b=(x-1000000*a)//1000
c=x-1000000*a-1000*b
print(a)
print(b)
print(c)