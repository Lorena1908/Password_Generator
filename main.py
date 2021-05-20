import random
import clipboard

# LISTS
password = []
symbols = ['@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '!']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V',
'B','N','M']
ambiguous_characters = ['[', ']', '{', '}', '(', ')', '/', '\\', '"', '\'', '~', '<', '>']

print('Welcome to Password Generator!')
print('Answer "y" for Yes and "n" for No')

while True:
    length = input('What is the length of your password? ')
    if length.isnumeric():
        length = int(length)
        if length <= 50:
            break
        else:
            print('Password is too large. Try Again.')
    else:
        print('Invalid answer, try again. ')

length1 = length

while True:
    include_symbols = input('Do you want it to include symbols? (e.g. @#$%&*-_=+) ')
    include_numbers = input('Do you want it to include numbers? (e.g. 1234567890) ')
    include_lowercase = input('Do you want it to include lowercase characters? (e.g. abcde) ')
    include_uppercase = input('Do you want it to include uppercase characters? (e.g. ABCDE) ')
    include_ambiguous_characters = input('Do you want it to include ambiguous characters? (e.g. {}[]()<>""\'\'/\~) ')
    yes_num = [include_symbols, include_numbers, include_uppercase, include_lowercase, include_ambiguous_characters]
    length /= round(yes_num.count('y'))
    length = int(length)
    lentgh_range = 0
    if 20 >= length > 10:
        lentgh_range = 2
        length /= lentgh_range
        length = int(round(length))
        break
    elif 30 >= length > 20:
        lentgh_range = 3
        length /= lentgh_range
        length = int(round(length))
        break
    elif 40 >= length > 30:
        lentgh_range = 4
        length /= lentgh_range
        length = int(round(length))
        break
    elif 50 >= length > 40:
        lentgh_range = 5
        length /= lentgh_range
        length = int(round(length))
        break
    else:
        break

def add_characters(lentgh_range, length):
    for num in range(lentgh_range):
        if include_symbols == 'y':
            password.extend(random.sample(symbols, length))
        if include_numbers == 'y':
            password.extend(random.sample(numbers, length))
        if include_lowercase == 'y':
            password.extend(random.sample(lowercase, length))
        if include_uppercase == 'y':
            password.extend(random.sample(uppercase, length))
        if include_ambiguous_characters == 'y':
            password.extend(random.sample(ambiguous_characters, length))

if lentgh_range != 0:
    add_characters(lentgh_range, length)
else:
    add_characters(1, length)

if len(password) < length1:
    add_characters(1, length1 - len(password))

random.shuffle(password)
del password [0:len(password)-length1]
print(len(password))
password_final = ''.join(password)
clipboard.copy(password_final)

print('Password Copied!')
print('Here is your password:', password_final)