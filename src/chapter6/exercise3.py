print('This program finds the number of times a letter appears in a text')
word = input('Enter a text: ')
char = input('Enter letter to find its number of times: ')
def count(word,char):
    count = 0
    for letter in word:
        if letter == char:
            count = count + 1
    print(count)
count(word,char)