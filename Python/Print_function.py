"""
Print Function

The included code stub will read an integer, , from STDIN.

Without using any string methods, try to print the following:


Note that "" represents the consecutive values in between.

Example

Print the string .

Input Format

The first line contains an integer .
"""
if __name__ == '__main__':
    n = int(input())
    s=""
    i=1
    while(i<=n):
        s=s+str(i)
        i=i+1
    print(s)
    
