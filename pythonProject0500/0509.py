n = int(input())
catflag = False
for i in range(n):
    phrase = input()
    if 'Кот' in phrase or 'кот' in phrase:
        catflag = True
    elif 'Пёс' in phrase or 'пёс' in phrase:
        catflag = False
if catflag is True:
    print('МЯУ')
elif catflag is False:
    print('НЕТ')