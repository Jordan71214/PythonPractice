import math

try:
    height = float(input('Enter ur Height(Centemeter) :'))
    weight = float(input('Enter ur Weight(Kilogram) :'))
except:
    print('invaild input value!!! Please input integer value')
    exit()

if height <= 0 or weight <= 0:
    print('input of value can\'t lower then zero!!!')
    exit()
BMI = weight / math.pow(height / 100, 2)
BMI = round()
print('%.2f' % BMI)
print(type(BMI))