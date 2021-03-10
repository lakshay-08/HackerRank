"""
Text Wrap
"""
import textwrap

def wrap(string, max_width):
    n=len(string)
    s=""
    e=n%max_width
    for i in range(0,n-e,max_width):
        s=s+string[i:i+max_width]+"\n"
    s=s+string[n-e:n]
    return(s)

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)