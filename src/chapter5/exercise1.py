count = 0
total = 0
while True:
    inp = input('Enter a number:')
    try:
        if inp == 'done':
            break
        else:
            #convert str to int into intt
            inpp = int(inp)
            total = total +inpp
            count = count + 1
            average = total/count
    except:
        print('invalid input')
print(total,count,average)