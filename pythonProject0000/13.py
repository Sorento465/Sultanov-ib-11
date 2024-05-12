import random
planets = ['Меркурий', 'Венера', 'Земля', 'Марс','Юпитер', 'Сатурн', 'Уран', 'Нептун']
planet = random.choice(planets)
warning = 'Присутствует защита от взлома!'
print(warning)
riddle = 'Какую планету я загадал?'
print(riddle)
answer = input()
if answer == 'Плутон':
    raise Exception('Ха-ха, это был загаданный ответ...')
elif answer not in planets:
    print('Да это же вообще не название планеты Солнечной системы.')
elif answer == planet:
    print('* Верно! * Это', answer)
else:
    print('Неверно!')
input()