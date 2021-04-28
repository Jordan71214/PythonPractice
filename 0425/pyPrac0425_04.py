a = frozenset([1, 2])
b = {1, 2}
for i in a:
    print(i)
print(type(a))

print(b)
b.add(3)
print(b)

print(len(a))
print(b[0])
for i in round(len(a)):
    print(i, a[i])
