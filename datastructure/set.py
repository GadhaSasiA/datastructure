a={1,2,3,1,4,5,}
b={2,9,3,7,6,10}
c=a.intersection(b)
print(c)
d=a.difference(b)
print(d)
e=a.symmetric_difference(b)
print(e)

a={1,2,3,1,4,5,3,6,5,7}
b=list(a)
print(a)

a={1,2,3,1,4,5,}
b={2,9,3,7,6,10}
c=a.union(b)
print(c)

a={1,2,3,1,4,5}
b={2,9,3,7,6,10}
c={3,5,7,9,2,8}
d=a.union(b)
print(d)
update_set=d.union(c)
print(update_set)

a={1,2,3,1,4,5}
c=a.clear()
print(c)
