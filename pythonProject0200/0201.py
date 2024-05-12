city1 = input()
city2 = input()
if city1 == city2:
    print("Нет")
elif city1 == 'Тула' and city2 == 'Пенза' or city2 == 'Тула' and city1 == 'Пенза':
    print("Нет")
elif city1 == 'Тула' and city2 != 'Пенза' or city1 != 'Тула' and city2 == 'Пенза':
    print("Да")
else:
    print("Нет")