people = list(map(str,input().split(","))) 
from_left = int(input())
from_right = (-1)*from_left
l = people[from_left:]
if '00' in l:
    a=l.index("00")
    l.insert(a,"0")
    l.remove("00")
r = people[:from_right]
if "00" in r:
    b=r.index("00")
    r.insert(b,"0")
    r.remove("00")
print(" ".join(l))
print(" ".join(r))
