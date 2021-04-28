sum = 0

for i in range(101):
    sum += i

print('1 ~ 100 的和')
print(sum)

odd = 0
even = 0
for i in range(101):
    if i % 2 == 0:
        even += i
    elif i % 2 == 1:
        odd += i

print('1~100 的奇數和: ')
print(odd)
print('1~100 的偶數和: ')
print(even)