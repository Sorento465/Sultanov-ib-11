a = float(input()) or int(input())
b = float(input()) or int(input())
c = input()
d = "888888"
if '+' in c and '-' not in c:
    print(a + b)
elif '-' in c and '+' not in c:
    print(a - b)
elif "/" in c:
    print(a / b)
elif '*' in c:
    print(a * b)
elif '0' in a or b and '/' in c:
    print(d)
else:
    print(d)