import random
planets = ['Меркурий', 'Венера', 'Земля', 'Марс', 'Юпитер', 'Сатурн', 'Уран', 'Нептун']
planet = random.choice(planets)
print('Какую планету я загадал?')
answer = input()
if answer == planet:
    raise Exception('Пароль угадан до ввода. Теперь все ваши планетные секреты нам известны!')
if answer == 'Плутон':
    raise Exception('Пароль угадан до ввода. Теперь все ваши планетные секреты нам известны!')
elif answer not in planets:
    print('Да это же вообще не название планеты Солнечной системы.')
elif answer == planet:
    print('* Верно! * Это', answer)
else:
    print('Неверно!')
input()