"""
String Validators
"""
if __name__ == '__main__':
    s = input()
    x1,x2,x3,x4,x5=False, False,False,False,False
    for i in s:
        if i.isalnum():
                x1=True
        if i.isalpha():
                x2=True
        if i.isdigit():
                x3=True
        if i.islower():
                x4=True
        if i.isupper():
                x5=True
    print(x1)
    print(x2)
    print(x3)
    print(x4)
    print(x5)