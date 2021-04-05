guests = int(input('Enter number of guests: '))
if guests <= 50:
    print("Cost $4000")
elif guests <= 100:
    print('Cost $10000')
elif guests <= 200:
    print('Cost $15000')
else :
    print ('Cost $20000')