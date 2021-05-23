def open_file():
    while True:
        file_name = input('Enter filename: ')
        try:
            fhandle = open(file_name)
            return fhandle
        except FileNotFoundError:
            print('enter correct file name')
def process(file):
    while True:
        try:
            year = input('Enter year or q to exit: ')
            years = int(year)
            if years>1000 and years < 2020:
                break
            else:
                print('Please enter valid year')
        except:
            if year =='q':
                exit()
            else:
                print('enter valid input')
                continue
    while True:
        try:
            list = ['1','2','3','4']
            income_level =input('Enter income level: ')
            if income_level in list:
                break
            else:
                print('Enter valid input')
        except:
            print('Income level should be 1 to 4')
    percentage = 0
    total_percentage = 0
    count = 0
    lowest_percentage = None
    highest_percentage =None
    if income_level =='1':
        text ='WB_LI'
    elif income_level =='2':
        text = 'WB_LMI'
    elif income_level =='3':
        text = 'WB_UMI'
    elif income_level == '4':
        text = 'WB_HI'
    else:
        print('Please enter valid input')
    for line in file:
        percentage = int(line[59:61])
        if year in (line[88:93]) and text in line[51:58]:
            count += 1
            total_percentage += percentage
            country = line[0:49]
            if lowest_percentage is None or percentage<lowest_percentage:
                lowest_percentage = percentage
                lcountry = country
            if highest_percentage is None or percentage> highest_percentage:
                highest_percentage = percentage
                hcountry = country

    print('Number of records',count)
    print('Average percentage',round(total_percentage/count,1))
    print('Country with lowest percentage: ',lcountry.strip() ,'and lowest percentage: ',lowest_percentage)
    print('Country with highest percentage: ',hcountry.strip(), 'and highest percentage: ', highest_percentage)
    
def main():
    process(open_file())
main()