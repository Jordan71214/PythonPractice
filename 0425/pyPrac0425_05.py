department = {'1':'會計資訊', '2':'財經', '3':'財稅', '4':'商務', '5':'企管'}
print(department)
print(type(department))

for key, value in department.items():
    print('K: ', key, ' V: ', value)

print(department['1'])
print(department['2'])

try:
    print(department['10'])
except KeyError:
    print('valid value')

print(department)

department['A'] = '厲害'
print(department)

for i in department:
    print(i)
for k, v in department.items():
    print(k, v)

for i in department:
    print(i, ": ", department[i])


print('是否有K 1', '1' in department)
print('是否有K A', 'A' in department)

del department['1']
print(department)