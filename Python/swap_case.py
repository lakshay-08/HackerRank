"""
sWAP cASE

You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.
"""


def swap_case(s):
    n=""
    for i in s:
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
                n=n+i.lower()
        elif i in "abcdefghijklmnopqrstuvwxyz":
                n=n+i.upper()
        else:
            n=n+i
    return(n)  


if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
