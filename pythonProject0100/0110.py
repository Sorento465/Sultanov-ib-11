print("Вы находитесь в загадочном лабиринте. Вы стоите перед развилкой...")
print("Вы можете пойти: ")
print("1. Налево")
print("2. Направо")
print("3. Прямо")
choice1 = input("Выберите куда пойти (введите номер действия): ")
if choice1 == "1":
    print("Вы свернули налево и увидели огромную дверь...")
    choice2 = input("Открыть дверь или вернуться? (напишите 'открыть' или 'вернуться'): ")
    if choice2.lower() == "открыть":
        print("Вы открыли дверь и обнаружили сокровища! Поздравляем, вы победили!")
    else:
        print("Вы решили вернуться и потерялись в лабиринте. Конец.")
elif choice1 == "2":
    print("Вы направились направо и встретили огромное паукообразное существо...")
    print("После долгой борьбы с ним, вы...")
    print("1. Побежали прочь")
    print("2. Сразились насмерть")
    choice3 = input("Что вы выберете? (введите номер действия): ")
    if choice3 == "1":
        print("Вы сбежали, но потеряли важный артефакт. Конец.")
    elif choice3 == "2":
        print("Вы смогли победить чудовище и продолжили свой путь. Поздравляем!")
    else:
        print("Вы приняли неправильное решение. Конец.")
elif choice1 == "3":
    print("Вы отправились прямо и наткнулись на древний механизм...")
    print("1. Постучать по механизму")
    print("2. Пройти мимо")
    choice4 = input("Что вы сделаете? (введите номер действия): ")
    if choice4 == "1":
        print("Механизм заработал и открыл секретную дверь! Вы выходите из лабиринта. Поздравляем!")
    elif choice4 == "2":
        print("Вы упустили свой шанс. Конец.")
    else:
        print("Вы застряли в лабиринте. Конец.")
else:
    print("Вы ввели неверное действие. Конец.")
