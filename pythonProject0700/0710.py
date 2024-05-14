index = int(input())
word = input()
answer = str()
for i in range(len(word)):
    answer += (chr(ord(word[i]) + index))
print(answer)