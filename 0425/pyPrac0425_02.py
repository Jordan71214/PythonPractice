a = range(10)
print(a)
for i in a:
    print(i)

name = (1, 2, 3, 5, 4, 6)
for i in range(len(name)):
    print('第%s個資料是:%s' % (i, name[i]))

for i in range(1, 10, 2):
    print(i)

b = list(range(10))
print(b)
print(type(b))

c = [1, 2]
print(type(c))
