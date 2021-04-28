number = 'A001'
balance = 1000
bonus = 1

print('B4')
print('Number: %s, Balance: %d, Bonus: %d ' % (number, balance, bonus))

try:
    money = int(input('Enter store money: '))
    if money > 0:
        balance += money
        if money >= 1000:
            bonus += 1
        
    else :
        print('你這不是叫我扣你款嗎 兄弟')
except:
    print('Valid input value bro!!!')

print('After')
print('Number: %s, Balance: %d, Bonus: %d ' % (number, balance, bonus))

