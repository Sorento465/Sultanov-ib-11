clients = []
for i in range(int(input())):
    clients.append(int(input()))
stonks = []
for client in clients:
    print(client)
    stonks.append(client * 3)
print()
for stonk in stonks:
    print(stonk)