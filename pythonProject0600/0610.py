menu = set()
u_menu = set()
menu_nu = set()
menu_N = int(input())
for i in range(menu_N):
    menu.add(input())
menu_true = int(input())
for i in range(menu_true):
    menu_in_N = int(input())
    for j in range(menu_in_N):
        u_menu.add(input())
menu_nu = menu - u_menu
print(menu_nu)