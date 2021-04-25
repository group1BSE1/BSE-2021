nickels = 25
dimes = 25
quarters = 25
ones = 0
fives =0

def change():
    chang = amountpaid - cents
    print('change:',chang)
while True:
    print('Welcome to the vending machine change maker program')
    print('Change maker initialized')
    print('Stock contains:\n',nickels,'nickels\n',dimes,'dimes\n',quarters,'quarters\n',ones,'ones\n',fives,'fives')
    value = input('Enter the purchase price(xx.xx) or ''\'q\' to quit: ')
    if value == 'q':
        break
    else:
        print(value)
#Menu of selections  
    value1 = float(value)
    #legal value
    if value1 >0 and value1*100%5==0:
        print(value1)
        print('Menu of deposits:')
        print('\'n\' - deposit a nickel')
        print('\'d\' - deposit for dime')
        print('\'q\' - for quarter')
        print('\'o\' - for one dollar bill')
        print('\'f\' - for five dollar bill')
        print('\'c\' -for cancel purchase')
        #dollar = round(value1//1)
        cents = value1*100
        #print(cents)
        '''dollar1 = 100
        nickel = 5
        quarter = 25
        dime = 10
        dime = 10'''
        #deposit and full collection
        if True:
            amountpaid = 0
            while cents>0:
                deposit = input('Indicate your deposit: ')
                if deposit == 'n':
                    cents = cents - 5
                    amountpaid = amountpaid + 5
                elif deposit == 'd':
                    cents  = cents - 10
                    amountpaid = amountpaid + 10
                elif deposit == 'q':
                    cents = cents - 25
                    amountpaid = amountpaid + 25
                elif deposit == 'o':
                    cents = cents -100
                    amountpaid = amountpaid + 100
                elif deposit == 'f':
                    cents = cents - 500
                    amountpaid = amountpaid + 500
                elif deposit == 'c':
                    break
                dollars = cents //100
                if dollars >0:
                    print('Payment due',dollars,'dollars',cents%100,'cents')
                #print('pay',pay)
                else:
                    print('Payment due',cents%100,'cents')
                
                print('amountpaid',amountpaid)

            #print(value,value1)
                    
        else:
                if cents<0:
                    print('cha')
        change = amountpaid - cents
        print('Please take your change below\n',round(abs(cents)))
        continue
        
    
    else :
        print('Enter a legal value')
#d = dollar + cents
#print(d)
