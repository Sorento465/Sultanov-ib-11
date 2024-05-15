soups = ['щи', 'борщ', 'щавелевый суп', 'суп по-чабански']
for i in range(int(input())):
    print(soups[i % len(soups)])