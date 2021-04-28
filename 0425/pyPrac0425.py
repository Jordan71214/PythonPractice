a = ()
print(a)
print(type(a))
print('-' * 30)

b = (1)
print(b)
print(type(b))
print('-' * 30)

c = (1,)
print(c)
print(type(c))
print('-' * 30)

d = [1, 2, 3, 4]
print(d)
print(type(d))
print('-' * 30)

for i in d:
    print(i)

for j in range(len(d)):
    print(j, ': ', d[j])

print(3 in d)
print(d[:2])
print(len(d))
print(max(d))
print(min(d))
d.append(4)
print(d)
print(d.count(4))

e = d[:]
print(e)
print(d)

e = e.reverse()
print(e)