import getpass,os

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
    print('Welcome to TriOS 1.0! Please login.\n')
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
        'create : create a file - usage:> filename.filetype\n'
        'delete : delete a file - usage:> filename.filetype\n'
        'edit: edit a file - usage:> filename.filtype -a/-w yourtext'
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
                except Exception as e:
                    print(e)

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

def cmd(entry):
    os.system(f'cmd /c {entry[1]}')


cmds = {'help':help, '?':help, 'ls':ls, 'cat':cat, 'read':read, 'cmd':cmd, 'sd':sd, 'cls':cls, 'create':create, 'delete':delete, 'edit':edit}

# -- // Mainloop \\ -- #

while mainloop:
    entry = input('\n> ').split(' ', 1)
    try:
        cmds[entry[0].lower()](entry)
    except:
        print('didnt work lol')
