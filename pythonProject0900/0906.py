numbers = list()
summary = list()
count = int(input())
for num in range(count):
    numbers.append(num)
for ix in range(len(numbers) - 1):
    summary.append(numbers[ix] + numbers[ix + 1])
for a in summary:
    print(a)