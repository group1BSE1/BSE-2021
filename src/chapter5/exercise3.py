nickels = 25
dimes = 25
quarters = 25
ones = 0
fives =0
print('Welcome to the vending machine change maker program')
print('Change maker initialized')
print('Stock contains:\n',nickels,'nickels\n',dimes,'dimes\n',quarters,'quarters\n',ones,'ones\n',fives,'fives')
while True:
    value = input('Enter the purchase price(xx.xx) or ''\'q\' to quit: ')
    if value == 'q':
        break
    else:
        print(value)
    
