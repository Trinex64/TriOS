import getpass,os
from tkinter import *

mainloop = True

########################################

class File:
    def __init__(self, name, end, ins):
        self.name = name
        self.end = end
        self.ins = ins
        self.full = f'{name}.{end}'

########################################

def login():
    print('Welcome to TriOS 1.2! Please login.\n')
    password = 'root'
    if getpass.getpass("Username: admin\nPassword: ") == password:
        print('Successfully logged in!')
    else:
        print('Incorrect! Try again.')
        login()
login()

########################################

readme = File('readme','txt','wassup bbg, this was made by Trinex\nyou can contact me on discord under the user trinex_\n')
environment = [readme]
display = [readme.full]

# -- // Functions \\ -- #

def expand(code):
    code = code.strip().split('\n')
    full = '\n '.join(code)
    return full

#def save_code(code, file):
#    file.ins = code

def tk_ide(file):
    def save_code():
        file.ins = txt.get("1.0", "end-1c")
        main.destroy()

    main = Tk()
    main.title('TriOS IDE')
    main.geometry('512x512')

    def indent_size(event):
        text = event.widget
        text.insert(INSERT,'    ')
        return 'break'

    txt = Text(main,width=60,height=30)
    txt.pack()
    txt.insert('1.0',file.ins)
    txt.bind('<Tab>', indent_size)

    save = Button(main,text="Save",width=30,command=save_code)
    save.pack()

    main.mainloop()

# -- // Commands \\ -- #

def help(_):
    print(
        'help/? : shows all commands\n'
        'ls : lists everything in the current environment\n'
        'cat : opens file\n'
        'read : reads file without opening\n'
        'cmd : run something like in cmd\n'
        'sd : shuts down the OS\n'
        'cls : clears console\n'
        'create : create a file - > filename.filetype\n'
        'delete : delete a file - > filename.filetype\n'
        'edit: edit a file - > filename.filtype -a/-w yourtext\n'
        'ide : opens the text editor for a file'
    )

def ls(_):
    print([i for i in display])

def cat(entry):
    for i in environment:
        if i.full == entry[1]:
            if i.end == 'txt':
                print(i.ins)
            if i.end == 'py':
                try:
                    exec(i.ins)
                except Exception as err:
                    print(err)

def read(entry):
    for i in environment:
        if i.full == entry[1]:
            print(i.ins)

def sd(_):
    global mainloop
    mainloop = False

def cls(_):
    os.system('cmd /c cls')

def create(entry):
    entry = entry[1].replace(' ', '').split('.')
    new_file = File(entry[0], entry[1], '')
    for i in environment:
        if i.full != new_file.full:
            environment.append(new_file)
            display.append(new_file.full)
            print(f'{new_file.full} Created!')
            return
        else:
            print('File already exists!')

def delete(entry):
    for i in environment:
        if i.full == entry[1]:
            environment.remove(i)
            display.remove(i.full)
            print(f'{i.full} Deleted!')
            return
    print('File Not Found!')
            
def edit(entry):
    entry = entry[1].split(' ', 2)
    for i in environment:
        if i.full == entry[0]:
            if entry[1].lower() == '-w':
                i.ins = entry[2]
                i.ins = i.ins.replace('¬>','\n')
                print(f'{i.full} Edited!')
            elif entry[1].lower() == '-a':
                i.ins += entry[2]
                i.ins = i.ins.replace('¬>','\n')
                print(f'{i.full} Edited!')
            else:
                print('Invalid flag!')

def ide(entry):
    for i in environment:
        if i.full == entry[1]:
            tk_ide(i)

def cmd(entry):
    os.system(f'cmd /c {entry[1]}')

def unfunny(_):
    print('That was not funny. Not amused. Not a laugh. Not a chuckle. Not a Haha or even a hehe. That was not funny at all. I would be embarrassed if i were you. You need a tutor on comedy and on humor cuz this just aint it. It was terrible. It was horrible. It was NOT Funny. If anything it was embarrassing. I would hate to be you right now. Because it was not even a little bit funny. The person who has the least sense of humor could come up with something way better than that. You are a disgrace to humor. You are a disgrace to comedy. I am VERY disappointed in you. I expected you to ACTUALLY be funny. But. NO. you are not. Do not even think for a millisecond that you are even the slightest bit funny, because you\'re NOT. It was not funny. It was not funny. Atleast read a "Dad jokes 101" book before you even start to think about tweeting a "joke" like this. This is Disrespectful to ALL people who laugh. And who make others laugh. The nerve of some people thinking that they are even just a LITTLE bit funny. This was not close to funny.')

cmds = {'help':help, '?':help, 'ls':ls, 'cat':cat, 'read':read, 'cmd':cmd, 'sd':sd, 'cls':cls, 'create':create, 'delete':delete, 'edit':edit,
        '69':unfunny, '420':unfunny, '42069':unfunny, '69420':unfunny, '6969':unfunny, '420420':unfunny, 'ide':ide}

# -- // Mainloop \\ -- #

while mainloop:
    try:
        entry = input('\n> ').split(' ', 1)
        cmds[entry[0].lower()](entry)
    except:
        print('didnt work lol')
