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
        #print('Please enter valid input')
        break
    
    print('Customer code:', code)
    print('Initial reading: ',iread)
    print('Final reading: ',fread)
    