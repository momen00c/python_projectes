from cryptography.fernet import Fernet
def write_key():
    key = Fernet.generate_key()
    with open('key.key','wb') as key_file:
        key_file.write(key)

def laod_key():
    file = open ('key.key','rb')
    key= file.read()
    file.close()
    return key
write_key()
key = laod_key()
fer = Fernet(key)

def view():
    with open('passowrd.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            user,passw = data.split('|')
            print('User:',user,'\nPassword:',fer.decrypt(passw.encode()).decode())

def add():
    name = input('Acconet Name: ')
    pasword = input('Password: ')
    with open('passowrd.txt','a') as f:
        f.write(name + '|' +fer.encrypt(pasword.encode()).decode() +'\n' )

while True:
    mode = input('would you like add password or view existing onces:')
    if mode =='q':
        break  
    if mode == 'view':
        view()    
    elif mode == 'add':
        add()
