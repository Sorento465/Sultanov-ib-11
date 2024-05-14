word = input()
aplhabet = 'qwertyuiopasdfghjklzxcvbnm_1234567890'
for char in word:
    if char not in aplhabet:
        print(f'Неверный символ: {char}')
        break
else:
    print('ОК')