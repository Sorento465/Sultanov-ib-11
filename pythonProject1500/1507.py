def find_mountain(heightsMap):
    t = []
    for i in heightsMap:
        t.append(max(i))
    s = max(t)
    for i in range(len(heightsMap)):
        if s in heightsMap[i]:
            row = i
    for i in heightsMap:
        for j in range(len(i)):
            if s == i[j]:
                col = j
    return (row, col)