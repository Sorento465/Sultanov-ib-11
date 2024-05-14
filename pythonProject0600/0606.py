home_library = set()
home_library_M = int(input())
books_on_list = set()
books_on_list_N = int(input())
for i in range(home_library_M):
    book = input()
    home_library.add(book)
for i in range(books_on_list_N):
    book = input()
    books_on_list.add(book)
    if book in home_library:
        print('YES')
    else:
        print('NO')