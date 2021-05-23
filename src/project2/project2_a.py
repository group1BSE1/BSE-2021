handle = open('measles.txt','r')
inp = input('Enter the year: ')
list =['1','2','3','4','5','6','7','8','9', '0','all','ALL','']
if not inp in list and inp in range(0,2020):
    print('Please enter valid input')
    exit()
else:
    if len(inp) <=4:
        pass
file = input('Enter output file: ')
if not '.txt' in file:
    print('please file should be in txt format ,should have .txt')
    exit()
fsave = open(file ,'w')
for line in handle:
    if inp in line[88:93] and line[88:93].startswith(inp):
        fsave.write(line)
    else:
        if inp =='' or inp =='all' or inp =='ALL':
            fsave.write(line)
fsave.close()
handle.close()