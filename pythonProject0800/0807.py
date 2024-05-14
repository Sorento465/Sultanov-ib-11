for i in range(int(input())):
    word = input()
    if 'кот' in word:
        for j in range(len(word)):
            if word[j:j+3] == 'кот':
                print(i+1, j+1)