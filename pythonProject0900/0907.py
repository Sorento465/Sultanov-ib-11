words = list()
for i in range(int(input())):
    words.append(input())
search = list()
for i in range(int(input())):
    search.append(input())
for word in words:
    for s in search:
        if s not in word:
            break
    else:
        print(word)