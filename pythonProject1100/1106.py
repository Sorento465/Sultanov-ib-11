book = []
for i in range(int(input())):
    recipe = input()
    if 'лук' not in recipe:
        book.append(recipe)
for rec in book:
    print(rec, end=' ')