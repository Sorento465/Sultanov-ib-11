s = input().lower()
string = s.replace(" ", "")
k = 0
m = 0
for i in s:
    if string.count(i) > k:
        k = string.count(i)
        m = i
print(m)