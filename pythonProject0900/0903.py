count = int(input())
strings = list()
res=""
for i in range(count):
    strings.append(input())
index = int(input())
for string in strings:
    if index <= len(string):
        res += string[index - 1]
print(res)