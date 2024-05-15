m = 0
string = input()
for s in string:
    if string.count(s) > m:
        m = string.count(s)
print(m)