file = input('Enter the file name: ')
fhandle = open(file, 'r')
count = 0
total = 0
for line in fhandle:
    if line.startswith('X-DSPAM-Confidence:'):
        line = line.lstrip('X-DSPAM-Confidence:')
        line = float(line)
        count = count + 1
        total = total + line
print('Average spam confidence',total/count)