"""
Designer Door Mat
"""
x,y=input().split()
for j in range(1,int(x)-1,2):
    print('-'*int((int(y)-(3*j))/2)+".|."*(j)+'-'*int((int(y)-(3*j))/2))
print('-'*int((int(y)-7)/2)+'WELCOME'+'-'*int((int(y)-7)/2))
for j in range(int(x)-2,0,-2):
    print('-'*int((int(y)-(3*j))/2)+".|."*(j)+'-'*int((int(y)-(3*j))/2))