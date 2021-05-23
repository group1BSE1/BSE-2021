fhandle = open('mbox.txt')
count = 0
for line in fhandle:
    if line.startswith('From'):
        words = line.split()
        count += 1
print('There are',count,'lines in the file with From as the first word')