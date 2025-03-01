a=input()
a=int(a)
x=a//525600
y=(a-x*525600)//1440
z=(a-x*525600-y*1440)//60
w=a-x*525600-y*1440-z*60
print('{}years {}days {}hours {}mins'.format(x,y,z,w))