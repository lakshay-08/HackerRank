"""
Mutations
"""

def mutate_string(string, position, character):
    n=string[:position]
    n2=string[position+1:]
    n=n+character
    t=n+n2
    return t

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)