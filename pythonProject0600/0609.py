ing_hmn = set()
ing_eat = set()
ing_h = int(input())
for i in range(ing_h):
    ing_hmn.add(input())
rec_name_N = int(input())
for i in range(rec_name_N):
    rec_name = input()
    ing_eat_M = int(input())
    flag = True
    for j in range(ing_eat_M):
        ing_eat.add(input())
    for i in ing_eat:
        if not i in ing_hmn:
            flag = False
    if flag:
        print(rec_name)
        ing_eat = set()