'''
list 是一種內建的資料型態
也就是說，安裝python的時候會給你這個物件去使用
不用在pip install其他的庫

list 有順序 可以增加、刪除、修改、查詢
'''
classmates = ['Micheal', 'Bob', 'Tracy']

print(classmates)

# len(list) len方法可以給你這個list的長度
print(len(classmates))

# 用for 把list中的元素取出來 這邊的 name 就是取出來的時候 暫時叫他的名字
# 換句話說 name = classmates[0]
# 每次都把classmates 的元素 叫做name 之後就能用name去做運用
for name in classmates:
    print(name)

# 這邊是把list的座號 用index 作為名字 取出來

# index   座標 : 0          1           2
# element 元素 : 'Micheal'  'Bob'       'Tracy'

# Micheal 現在坐在 0 號座位
# Bob 現在坐在 1 號座位
# Tracy 現在坐在 2 號座位


for index in range(len(classmates)):
    print(index)
    

print(classmates[len(classmates) - 1])
print(classmates[-1])

# 當然 我們可以在 list 後面增加東西
# 這邊在list的後面加上 Jordan這個元素
classmates.append('Jordan')
print(classmates)


# 我們也能夠刪除list的東西
# 這邊刪除了list最後面的元素
# 如果你想刪除其他座位的元素 那麼 pop(n) 會是你想要的方法 n 會決定你想要刪除的座位
# 但是 你刪除了第1000個座位的元素的時候 發現根本沒有這麼多座位啊 系統會提示你 :
# IndexError: pop index out of range
# 意思是說 注意! pop (刪除) 的座位超過了這個list的範圍了 
print(classmates.pop())
print(classmates)

classmates.pop(2)
print(classmates)

