items = []
while True:
    inp = input('Enter list items: ')
    if inp =='done':
        break
    items.append(inp)
print('Maximum',max(items))
print('Minimum',min(items))