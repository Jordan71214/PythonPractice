# set跟dict一樣 是唯一的 就只是沒有value的key
# 所以不論給幾次重複的值 都只會有一個

# 這邊用set(list) 去建立一個set
s = set([1, 2, 3, 3])
print(type(s))
print(s)


# 增加元素的方法add(n)  當然 重複給予 在set中也只有一個
s.add(3)
s.add(4)

print(s)

# 刪除的方法 remove(n)
# 如果刪除的key 不再set中 系統會給你發消息
# KeyError: n
# 要避免因為刪除造成的中斷 可以先判斷set中 有沒有n
# 再去處理之後的步驟


n = 100
if n in s:
    s.remove(n)
else :
    print('set裡頭沒有這個key喔!!!')


if s.__contains__(n):
    s.remove(n)
else :
    print('set裡頭沒有這個key喔!!!')



s.remove(1)
print(s)


print('-' * 30)

# set 就像是集合 沒有順序, 不會重複 所以可以做集合運算
s1 = set([4, 2, 8])

print(s)
print(s1)

# 聯集
print('s & s1', s & s1)
# 交集
print('s | s1', s | s1)


nums = [1, 2, 3, 3, 4, 5, 5, 6, 7]

# 用來看看裡頭有沒有這個值 set.__contains__(n) 返回的是bool值
print(nums.__contains__(10))



