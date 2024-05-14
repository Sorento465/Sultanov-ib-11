word = int(input())
result = word
value = int(str(result)[0])
while value and value != 1 and result < 1000000000000:
    result *= value
    value = int(str(result)[0])
print(result)