"""
Lists
"""

if __name__ == '__main__':
    n = int(input())
    l=[]
    for i in range(n):
      s=input()
      if s[0]=="i":
        in1,i,v=s.split()
        l.insert(int(i),int(v))
      elif s[0:3]=="rem":
        r,v=s.split()
        l.remove(int(v))
      elif s[0]=="a":
        a,v=s.split()
        l.append(int(v))
      elif s=="pop":
        l.pop()
      elif s=="reverse":
        l=l[::-1]
      elif s=="print":
        print(l)
      elif s=="sort":
        l.sort()