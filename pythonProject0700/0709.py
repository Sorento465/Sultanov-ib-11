word = input()
index = int(input())
if index - 1 < len(word):
    print(word[index - 1])
else:
    print('ОШИБКА')