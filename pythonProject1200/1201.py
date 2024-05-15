for i in range(int(input())):
    word = input()
    if 'кот' in word:
        print((f'{i + 1}{word.index('кот') + 1}'))