a = input()
b = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
c = len(a)
for i in b:
    c -= a.count(i)
print(c)