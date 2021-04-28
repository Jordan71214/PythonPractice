'''
如果你有兩個表單 分別是:
名字['A', 'B', 'C']
成績[90, 100, 22]

在你想要知道 A 同學的成績時 你需要 ->
在名字表單裡面找到 A 同學
知道他是坐在 index = 0 (0 號 座位的朋友)
現在知道她坐在0號 
趕緊到成績單上查看
[90, 100, 22]
  0,   1,  2
他是0號 所以他這次考了 90分 還不錯
但是同學們 這種方法會不會有點花時間啊
我們把兩個數值連在一起怎麼樣 
'A' --- 90分
'B' --- 100分
'C' --- 22分
這樣是不是輕鬆多了
知道要問誰的成績 可以直接知道他考了幾分
我們接下來實作看看這種資料型態:dict
'''

names = ['Micheal', 'Bob', 'Tracy']
scores = [95, 75, 85]

# 做一個dict {}
# key:value 的方式放東西進去
d = {'Micheal':95, 'Bob':75, 'Tracy':85}
print(d)
print(type(d))

# 要找 Micheal d[key]
print(d['Micheal'])

# 把 Apple:100 放入 d 
d['Apple'] = 100

print(d)

# 因為dict key是唯一的 放再多次的value給那她 他只會改value 不會給新的key
d['Apple'] = 0

print(d)

# print('我也不認識 反正他不在裡面')
# 如果我告訴他說 : 我要找一個我不認識的人 d[我也不認識 反正他不在裡面]
# 的話 系統會告訴你說 :
# keyError '我也不認識 反正他不在裡面'
# 找不到這個人 
# 避免 亂找人造成的錯誤 這邊有兩個方法事先處理

# 1. 看看dict裡面有沒有 'name' name這個人 有的話在執行
if 'Micheal000' in d:
    print(True)
else:
    print(False)

# 2. 用dict的get()方法 
# 找到了 就給你Value
print(d.get("Micheal"))

# 找不到 會給你 None
print(d.get('Michal'))

# 或者是你不想要 None 想要其他回傳值 可以在get(name, n) 第二個參數的地方 加入想要的回傳值
print(d.get('Michal', -1))

# 當然 你可以刪除裡面的東西 用key去做刪除
d.pop('Micheal')

# 如果你怕亂刪除到裡面沒有的資料 可以參考前面的方法 
# 先看看裡面到底有沒有資料 再決定要不要去刪除
print(d)
x = str(input("Enter the Key u want to del: "))
if x in d:
    d.pop(x)
else :
    print('Input envalid')

print(d)