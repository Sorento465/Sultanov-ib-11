from random import randint

x = randint(1, 8)
user_num = 0
attempt = 0

while True:
    user_num = int(input())
    attempt +=1
    if user_num == x:
        break
    elif user_num > x:
        print("<")
    elif user_num < x:
        print(">")