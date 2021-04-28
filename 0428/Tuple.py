# t = () tuple
# 當 tuple 定義後 內容指針無法改變

t = (1, 2)
print(t)
print(type(t))
print(t[1])

# tuple 也可以是空的 
t=()
print(t)
print(type(t))

# 當 tuple 只定義一個元素時 因為自動裝箱的原因
# (1) 會被認定是一個int
t = (1)
print(type(t))
print(t)

# 所以 tuple 只定義一個元素，需要加上 ',' 來消歧義
t = (1,)
print(type(t))
print(t)


# 不是說明定義後的元素無法改變嗎
# 為何以下程式碼會改變元素

t = ('a', 'b', ['c', 'd'])


print(type(t))
print(t)

t[2][0] = 'A'
t[2][1] = 'B'

print(type(t))
print(t)

# 當 t 定義的時候 是鎖定區塊的指針
# 也就是說 t[0] 永遠指向記憶體中的特定位置 無法更動
# 以上程式碼的 t 可以看成是
c = ['c', 'd']
t1 = ('a', 'b', c)

# t[0] 指向 'a'
# t[1] 指向 'b'
# t[2] 指向 c['c', 'd'] 這個list
# 確實改動的時候沒有更改到指針的位置 指針還是指向 c 這個list
# 只有改變list 的內容
print(t[1])