for i in range(int(input())):
    text = input()
    if 'Не ' == text[:3] or 'не ' == text[:3]:
        print()
    else:
        print(text)