from flask import Flask, render_template, request, url_for, redirect
import random
import clipboard

app = Flask(__name__)

# LISTS
password = []
symbols = ['@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '!']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V',
'B','N','M']
ambiguous_characters = ['[', ']', '{', '}', '(', ')', '/', '\\', '"', '\'', '~', '<', '>']

# FUNCTIONS
def try_except(form):
    try:
        var = request.form[form]
        return var
    except:
        var = ''
        return var

def toggle_checked(checkbox, x, y):
    if checkbox.x <= x <= checkbox.x + 27 and checkbox.y <= y <= checkbox.y + 27:
        if checkbox.ticked:
            checkbox.ticked = False
        else:
            checkbox.ticked = True

def checked_num(checkbox_list):
    checked_num = 0
    for item in checkbox_list:
        if item.ticked:
            checked_num += 1
    return checked_num

def generate_password(length, true_num):
    length1 = int(round(length / true_num.count('on')))
    lentgh_range = 0
    if 20 >= length1 > 10:
        lentgh_range = 2
        length1 = int(round(length1 / lentgh_range))
    elif 30 >= length1 > 20:
        lentgh_range = 3
        length1 = int(round(length1 / lentgh_range))
    elif 40 >= length1 > 30:
        lentgh_range = 4
        length1 = int(round(length1 / lentgh_range))
    elif 50 >= length1 > 40:
        lentgh_range = 5
        length1 = int(round(length1 / lentgh_range))
    return length1, lentgh_range

def add_characters(lentgh_range, length, true_num):
    for num in range(lentgh_range):
        if true_num[0] == 'on': # Symbols
            password.extend(random.sample(symbols, length))
        if true_num[1] == 'on': # Numbers
            password.extend(random.sample(numbers, length))
        if true_num[2] == 'on': # Lowercase
            password.extend(random.sample(lowercase, length))
        if true_num[3] == 'on': # Uppercase
            password.extend(random.sample(uppercase, length))
        if true_num[4] == 'on': # Ambiguous Characters
            password.extend(random.sample(ambiguous_characters, length))

def check_password_length(password, length):
    if len(password) < length:
        add_characters(1, length - len(password))

    random.shuffle(password)
    del password [0:len(password)-length]
    password_final = ''.join(password)
    return password_final

@app.route('/')
def index():
    return render_template('index.html', password='')

@app.route('/main', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        length = try_except('length')
        sym = try_except('symbols')
        num = try_except('numbers')
        lower = try_except('lowercase')
        upper = try_except('uppercase')
        amb_char = try_except('amb_char')
        true_num = [sym, num, lower, upper, amb_char]
        copy_button = try_except('copy')
        
        if length.isnumeric():
            length = int(length)

        try:
            length1, length_range = generate_password(length, true_num)

            if length_range != 0:
                add_characters(length_range, length1, true_num)
            else:
                add_characters(1, length1, true_num)
            
            password_final = check_password_length(password, length)

            return render_template('index.html', password=password_final)
        except(ZeroDivisionError, TypeError):
            print('An exception was raised')
            pass
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='192.168.100.5')