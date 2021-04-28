a = {1, 2, 3, 4, 5, 2, 3, 6}
print(a)

for i in a:
    print(i)

print(10 in a)
print(1 in a)
b = {1}
print(a.isdisjoint({}))
print(b.issubset(a))
print(a > b)
print(a >= b)


s1 = {1, 2, 3, 5, 6, 7}
s2 = {5, 6, 2, 3}

print('s1', s1)
print('s2', s2)

print(s1 & s2)
print(s1 | s2)
print(s1 - s2)

print(s1)
s1.add(10)
print(s1)
s1.remove(5)
print(s1)