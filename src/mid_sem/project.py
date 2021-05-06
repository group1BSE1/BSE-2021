while True:
    try:
        code = input("Enter customer code: ")
        if code == 'r' or code=='R' or code =='c' or code=='C' or code =='i' or code == 'I':
            tcode = 'ok'
        else:
            break
        iread = float(input("Enter init read: "))
        fread = float(input('Enter final reading: '))
    except:
        print('Please enter valid input')
        continue
    
    if iread>0 and fread<999999999:
        if iread<fread:
            gallons = (fread-iread)/10
        else:
            gallons = ((1000000000-iread)+fread)/10
        #print(gallons)
    if code =='r' or code == 'R':
        amount = 5 + (0.0005*gallons)
    elif code =="c" or code == 'C':
        if gallons <= 4000000:
            amount = 1000
        else:
            ngallons = gallons - 4000000
            amount = 1000 + (0.00025 *ngallons)
    else:
        if code =='i' or code =='I':
            if gallons<=4000000:
                amount =  1000
            elif gallons >4000000 and gallons < 10000000:
                ngallons = gallons - 10000000
                amount = 2000 + (0.00025*ngallons)
    
    print('Customer code:', code)
    print('Initial reading: ',iread)
    print('Final reading: ',fread)
    print('Gallons used: ',gallons)
    print('Amount used: ', '$'+str(round(amount,2)))