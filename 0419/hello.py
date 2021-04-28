import math

r = 15
print('半徑 %.0f 的圓面積= %.4f' % (r, r * r * math.pi))

print('半徑15的圓面積=', math.ceil(15 * 15 * math.pi))
print('半徑15的圓面積=', math.floor(15 * 15 * math.pi))

#math.ceil() -> 向上取整 換言之 >= 的最小整數
print(math.ceil(10.5))

#math.floor() -> 向下取整 換言之 <= 的最大整數
print(math.floor(10.5))