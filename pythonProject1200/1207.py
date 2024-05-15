stack = []
for i in input().split(' '):
    try:
        stack.append(int(i))
    except ValueError:
        if i == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif i == '*':
            a, b = stack.pop(), stack.pop()
            stack.append(b * a)
        else:
            raise NotImplementedError
assert(len(stack) == 1)
print(stack[0])