first_str = input()
n = int(first_str[:4])
summa = int(first_str[4:])
error = []
actual_sum = 0
for i in range(n):
    shop = input()
    actual_sum += int(shop[13:])
    if int(shop[0:7]) * int(shop[8:12]) != int(shop[13:18]):
        error.append(i + 1)
print(abs(summa - actual_sum))
for errors in error:
    print(errors, end=' ')