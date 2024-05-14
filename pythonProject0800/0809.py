for i in range(int(input())):
    password = input()
    if password[:4] != '####' and password[:2] != '%%':
        print(password)
    elif password[:2] == '%%':
        print(password[2:])