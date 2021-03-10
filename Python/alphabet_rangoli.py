"""
Alphabet Rangoli
"""
def print_rangoli(size):
    size-=1
    s="abcdefghijklmnopqrstuvwxyz"
    for i in range(size+1):
        s1=s[size-i:size+1]
        print(("-".join(s1[i+1:0:-1]+s1[0]+s1[1:])).center((size*4)+1,"-"))
    for i in range(size-1,0,-1):
        s1=s[size-i:size+1]
        print(("-".join(s1[i+1:0:-1]+s1[0]+s1[1:])).center((size*4)+1,"-"))
    if size!=0:
     print(("-".join(s[size]).center((size*4)+1,"-")))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)