largest = None
smallest = None
while True:
    num = input('Enter a number: ')
    if num =='done':
        break
    elif largest is None or num > largest:
        largest = num
    elif smallest is None or num < num:
        smallest = num
print('maximum',largest)
print('minimum',smallest)