word = int(input())
for i in range(int(input())):
    text = input()
    if len(text) > word:
        text = text[:word - 3]+ '...'
    print(text)