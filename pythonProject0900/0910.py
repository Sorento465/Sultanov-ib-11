nums = []
for i in range(int(input())):
    nums.append(int(input()))
summa = 0
for i in range(int(input()) - 1, int(input())):
    summa += nums[i]
print(summa)