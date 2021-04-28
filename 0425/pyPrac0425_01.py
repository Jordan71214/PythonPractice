a = (1, 2, 3, 4, 5)
for i in a:
    print(i)
print('-' * 30)

for i in range(len(a)):
    print(i, ': ' , a[i])

print(10 in a)
print(5 in a)

print(a.count(2))
print(a.count(3))
print(max(a))
print(min(a))
print(a + a)
