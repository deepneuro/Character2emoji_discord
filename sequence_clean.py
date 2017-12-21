import re
from num2words import num2words

def cx(text):

    text = re.sub('~-\W+^\s', '', text)
    text = re.sub(':', '', text)
    text = re.sub('~', '', text)

    result = ''

    for char in text:
        if char == ' ':
            result += '     '
        elif char == '\n':
            result += '\n'
        else:
            if char not in ['1','2','3','4','5','6','7','8','9']:
                regional = ':regional_indicator_' + char + ':' + ' '
                result += regional
            else:
                number = ':' + num2words(int(char)) + ':' + ' '
                result += number

    print('\n')
    print(result)

def multi_cx(txt):
    print(txt)
    for line in txt:
        result = ''
        line = re.sub('~-\W+^\s', '', line)
        line = re.sub(':', '', line)
        line = re.sub('~', '', line)

        for char in line:
            if char == ' ':
                result += '     '
            else:
                if char not in ['1','2','3','4','5','6','7','8','9']:
                    regional = ':regional_indicator_' + char + ':' + ' '
                    result += regional
                else:
                    number = ':' + num2words(int(char)) + ':' + ' '
                    result += number
        print('\n')
        print(result)


def flag(f):
    txt.append(f)
    f = input('Press Enter').lower()

    if flag == 'no' or f == '':
        count = 0
        for elem in txt:
            count += len(elem) + 3
        print('Discord limit is 2000.. You submited: ',count*23)
        if count+len(txt)+12 < int(2000/23):
            multi_cx(txt)
        else:
            print('Sentence too long for discord. Run the Code again...')
    else:
        flag(f)


txt = []

text = input("What's your sentence: ").lower()
if text == '':
    print('****************Terminated!****************')

if len(text) + 6 > int(2000/23):
    print(10*'*')
    text = input('Sentence too long for discord. Try again: ').lower()
else:
    f = input("More? Press 'No' to end: ").lower()

    if flag == 'no' or f == '':
        cx(text)
    else:
        txt.append(text)
        flag(f)
