try:
    age = int(input('Enter your age: '))
    if age >= 18:
        print('You can vote')
    elif age > 0 and age <= 17:
        print('Too young to vote')
    else :
        print("Your a time traveller")
except:
    print('Please enter age as an integer')