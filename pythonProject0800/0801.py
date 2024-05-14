word = input()
long = ''
short = ''
while word != 'стоп':
    if len(word) > len(long):
        long = word
    if len(word) < len(short) or not short:
        short = word
    word = input()
f = True
for char in short:
    if char not in long:
        f = False
        break
if f:
    print('Да')
else:
    print('Нет')