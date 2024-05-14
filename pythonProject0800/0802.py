word1 = input()
word2 = input()
cow = 0
bull = 0
for i in range(len(word1)):
    if word1[i] == word2[i]:
        bull += 1
    elif word1[i] in word2:
        cow += 1
print(bull, cow)
