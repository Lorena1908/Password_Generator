from tkinter import *
import tkinter.font as font
import random

password = []
symbols = ['@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '!']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V',
'B','N','M']
ambiguous_characters = ['[', ']', '{', '}', '(', ')', '/', '\\', '"', '\'', '~', '<', '>']

root = Tk()
root.geometry('400x350')
root.title('Password Generator')
root.config(bg='pink')

def generate_password():
    try:
        l = include_length.get()
        if l.isnumeric():
            length_num = int(l)
            if length_num <= 50:
                password_entry.delete(0, END)
            else:
                password_entry.delete(0, END)
                password_entry.insert(0, 'Too large password!')
                include_length.delete(0, END)
                return
        else:
            password_entry.delete(0, END)
            password_entry.insert(0, 'Type a number!')
            include_length.delete(0, END)
            return
        
        s = symbol.get()
        n = num.get()
        l = lower.get()
        u = upper.get()
        a = amb_char.get()
        yes_num = [s, n, l, u, a]
        
        length1 = int(round(length_num / yes_num.count(1)))
        length_range = 0

        if 20 >= length1 > 10:
            length_range = 2
            length1 = int(round(length1 / length_range))
        elif 30 >= length1 > 20:
            length_range = 3
            length1 = int(round(length1 / length_range))
        elif 40 >= length1 > 30:
            length_range = 4
            length1 = int(round(length1 / length_range))
        elif 50 >= length1 > 40:
            length_range = 5
            length1 = int(round(length1 / length_range))
        
        if length_range != 0:
            add_characters(length_range, length1, yes_num)
        else:
            add_characters(1, length1, yes_num)
        
        if len(password) < length_num:
            add_characters(1, length_num - len(password), yes_num)

        random.shuffle(password)
        del password [0:len(password)-length_num]
        password_final = ''.join(password)
        password_entry.insert(0, password_final)
        password.clear()

    except ZeroDivisionError:
        password_entry.delete(0, END)
        password_entry.insert(0, 'Select one type of character!')

def add_characters(length_range, length, yes_num):
    for num in range(length_range):
        if yes_num[0]:
            password.extend(random.sample(symbols, length))
        if yes_num[1]:
            password.extend(random.sample(numbers, length))
        if yes_num[2]:
            password.extend(random.sample(lowercase, length))
        if yes_num[3]:
            password.extend(random.sample(uppercase, length))
        if yes_num[4]:
            password.extend(random.sample(ambiguous_characters, length))

# FONT
font = font.Font(size=15)

# VARIABLES
symbol = IntVar()
num = IntVar()
lower = IntVar()
upper = IntVar()
amb_char = IntVar()

# REQUIREMENTS
password_entry = Entry(root, width=40)
include_length = Entry(root, width=30)
include_symb = Checkbutton(root, variable=symbol, bg='pink')
include_num = Checkbutton(root, variable=num, bg='pink')
include_lower = Checkbutton(root, variable=lower, bg='pink')
include_upper = Checkbutton(root, variable=upper, bg='pink')
include_amb_char = Checkbutton(root, variable=amb_char, bg='pink')

# LABELS
title = Label(root, text='Password Generator', font='bold', bg='pink')
include_length_label = Label(root, text='Length:', bg='pink')
include_symb_label = Label(root, text='Include Symbols: (e.g. @#$%&*-_=+)', bg='pink')
include_num_label = Label(root, text='Include Numbers: (e.g. 1234567890)', bg='pink')
include_lower_label = Label(root, text='Include Lower: (e.g. abcde)', bg='pink')
include_upper_label = Label(root, text='Include Upper: (e.g. ABCDE)', bg='pink')
include_amb_char_label = Label(root, text='Include Ambiguous Characters: (e.g. {}[]()<>""\'\'/\~)', bg='pink')
password_label = Label(root, text='Password:', bg='pink')

# BUTTONS
submit_btn = Button(root, text='Generate Password', command=generate_password, width=30)

# DISPLAY ON SCREEN
title.grid(row=0, column=0, columnspan=2, padx=110, pady=15, sticky=W+E)
include_length_label.grid(row=1, column=0, padx=30, sticky=W)
include_symb_label.grid(row=2, column=0, padx=30, sticky=W)
include_num_label.grid(row=3, column=0, padx=30, sticky=W)
include_lower_label.grid(row=4, column=0, padx=30, sticky=W)
include_upper_label.grid(row=5, column=0, padx=30, sticky=W)
include_amb_char_label.grid(row=6, column=0, padx=30, sticky=W)
password_label.grid(row=7, column=0, padx=30, sticky=W)

include_length.grid(row=1, column=0, columnspan=2, padx=40, sticky=E)
include_symb.grid(row=2, column=0, columnspan=2, padx=30, sticky=E)
include_num.grid(row=3, column=0, columnspan=2, padx=30, sticky=E)
include_lower.grid(row=4, column=0, columnspan=2, padx=30, sticky=E)
include_upper.grid(row=5, column=0, columnspan=2, padx=30, sticky=E)
include_amb_char.grid(row=6, column=0, columnspan=2, padx=30, sticky=E)
password_entry.grid(row=7, column=0, columnspan=2, padx=40, pady=20, sticky=E)

submit_btn.grid(row=8, column=0, columnspan=2, ipady=3, pady=20)

root.mainloop()