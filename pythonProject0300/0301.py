number1= 15.5
number2= 28
number3 = (float(input()))
if number3 <= number1:
    print("Холодно")
elif number1 < number3 <= number2:
    print("Нормально")
elif number3 > number2:
    print("Жарко")
