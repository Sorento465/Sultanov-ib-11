password = input()
password1 = input()
while len(password) < 8:
    print("Короткий")
    password = input()
    password1 = input()
    while "123" in password:
        print("Простой")
        password = input()
        password1 = input()
        while password1 != password:
            print("Различаются")
            password = input()
            password1 = input()
        else:
            print("OK")
            break