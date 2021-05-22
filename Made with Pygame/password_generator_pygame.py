import pygame
import pygame_textinput
import random
import clipboard

# VARIABLES AND LISTS
font = pygame.font.SysFont('comicsans', 35)
width, height = 760, 650
text_input = pygame_textinput.TextInput('  ')
win = pygame.display.set_mode((width, height))
pygame.display.set_caption('Password Generator')
clock = pygame.time.Clock()
password = []
symbols = ['@', '#', '$', '%', '&', '*', '-', '_', '=', '+', '!']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
lowercase = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p', 'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 
'ç', 'z', 'x', 'c', 'v', 'b', 'n', 'm']
uppercase = ['Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Ç','Z','X','C','V',
'B','N','M']
ambiguous_characters = ['[', ']', '{', '}', '(', ')', '/', '\\', '"', '\'', '~', '<', '>']
run = True
error = False
right_length = False

class CheckBox:
    def __init__(self, x, y, ticked=False):
        self.color = (128,128,128)
        self.x = x
        self.y = y
        self.ticked = ticked
    
    def draw(self):
        if self.ticked:
            pygame.draw.rect(win, self.color, (self.x, self.y, 27,27), 0, 2)
        else:
            pygame.draw.rect(win, self.color, (self.x, self.y, 27,27), 3, 2)

# CHECKBOXES
symb_checkbox = CheckBox(688,158)
numb_checkbox = CheckBox(688, 208)
upper_checkbox = CheckBox(688, 258)
lower_checkbox = CheckBox(688, 308)
amb_char_checkbox = CheckBox(688, 358)
checkbox_list = [symb_checkbox, numb_checkbox, upper_checkbox, lower_checkbox, amb_char_checkbox]

def draw_window(error, final_password):
    # FONTS AND TEXT
    title_font = pygame.font.SysFont('comicsans', 50)
    title = title_font.render('Password Generator', 1, (0,0,0))
    length_ = font.render('Length: ', 1, (0,0,0))
    symbols = font.render('Symbols (e.g. @#$%&*-_=+): ', 1, (0,0,0))
    numbers = font.render('Numbers (e.g. 1234567890): ', 1, (0,0,0))
    lowercase = font.render('Lowercase (e.g. abcde): ', 1, (0,0,0))
    uppercase = font.render('Uppercase (e.g. ABCDE): ', 1, (0,0,0))
    ambiguous_characters = font.render('Ambiguous Characters (e.g. {}[]()<>/\~): ', 1, (0,0,0))
    password_prompt = font.render('Password: ', 1, (0,255,0))
    password = font.render(final_password, 1, (0,255,0))
    enter = font.render('Press enter to generate the password!', 1, (0,0,0))

    # SHAPES AND CHECKBOX
    pygame.draw.rect(win, (128,128,128), (135,97, 580, 45), 0, 2) # First rectangle
    pygame.draw.rect(win, (0,255,0), (25,476, 720, 50), 2, 2)
    symb_checkbox.draw()
    numb_checkbox.draw()
    upper_checkbox.draw()
    lower_checkbox.draw()
    amb_char_checkbox.draw()
    win.blit(title, (width/2 - title.get_width()/2,30))
    win.blit(length_, (40,108))
    win.blit(symbols, (40,158))
    win.blit(numbers, (40,208))
    win.blit(uppercase, (40,258))
    win.blit(lowercase, (40,308))
    win.blit(ambiguous_characters, (40,358))
    win.blit(password_prompt, (30,438))
    win.blit(password, (30,490))

    if not error:
        win.blit(enter, (25, 558))

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

def generate_password(length):
    length1 = int(round(length / checked_num(checkbox_list)))
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

def add_characters(lentgh_range, length):
    for num in range(lentgh_range):
        if symb_checkbox.ticked:
            password.extend(random.sample(symbols, length))
        if numb_checkbox.ticked:
            password.extend(random.sample(numbers, length))
        if upper_checkbox.ticked:
            password.extend(random.sample(lowercase, length))
        if lower_checkbox.ticked:
            password.extend(random.sample(uppercase, length))
        if amb_char_checkbox.ticked:
            password.extend(random.sample(ambiguous_characters, length))

def check_password_length(password, length):
    if len(password) < length:
        add_characters(1, length - len(password))

    random.shuffle(password)
    del password [0:len(password)-length]
    password_final = ''.join(password)
    return password_final

def create_error(text):
    type = font.render(text, 1, (255,0,0))
    width = type.get_width() + 20
    win.blit(type, (25, 558))

while run:
    win.fill((255,255,255))
    events = pygame.event.get()
    
    if text_input.update(events):
        length = text_input.get_text()[2:]
        if length.isnumeric():
            length = int(length)
            if length <= 50:
                right_length = True
            else:
                error = True
                create_error('Large password!')
        else:
            error = True
            create_error('Your answer is not a number!')
        
        if right_length:
            try:
                length1, lentgh_range = generate_password(length)

                if lentgh_range != 0:
                    add_characters(lentgh_range, length1)
                else:
                    add_characters(1, length1)
                
                password_final = check_password_length(password, length)

                if password_final:
                    t = font.render('Password Copied to Clipboard!', 1, (255,0,0))
                    draw_window(error, password_final)
                    pygame.draw.rect(win, (255,255,255), (25, 558, width, 200))
                    win.blit(t, (25, 558))
                    pygame.display.update()
                    clipboard.copy(password_final)
                    pygame.time.wait(2000)
            except(ZeroDivisionError, TypeError):
                pass

    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            toggle_checked(symb_checkbox, x, y)
            toggle_checked(numb_checkbox, x, y)
            toggle_checked(upper_checkbox, x, y)
            toggle_checked(lower_checkbox, x, y)
            toggle_checked(amb_char_checkbox, x, y)

    draw_window(error, 'Here will be your password')
    win.blit(text_input.get_surface(), (135,108))
    pygame.display.update()
    
    if error:
        error = False
        pygame.time.wait(1500)