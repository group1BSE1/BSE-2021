try:
    location = str(input('Enter location: '))
    pay = int(input('Enter pay: '))
    if location == 'Kampala':
        if pay >= 10000000:
            print('Without doubt I\'ll take it')
        else :
            print('No way!')
    elif location == 'Mbarara':
        if pay > 4000000:
            print('Without doubt I\'ll take it')
        else :
            print('No thanks, I can find something better')
    elif location == 'Space':
        print('Without doubt I\'ll take it')
    else:
        if pay>=6000000 and location == '':
            print('Sure , I can work with this')
except:
    print('Error, Enter text for location and integer for pay')