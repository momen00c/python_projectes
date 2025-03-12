import random
choice=['r','p','c']
def lists():
    user=input("enter your choice:")
    
    if user not in choice:
        print('note vild ')
        return None
    return user
def strucher(user,computer):
    if (user=='r' and computer =='c')or\
       (user=='p' and computer =='r')or\
       (user=='c' and computer =='p'):
        print('you win') 
    elif user==computer:
          return('it is tie')
      
    else:
        return('i win')

def playing():
    while True:
        user=lists()
        if user is None:
            continue
        computer=random.choice(choice)
        result=strucher(user,computer)
        print(f'user chouce:{user}')
        print(f'compuyter choice:{computer}')
        print(result)
        playe_agin=input('do you want play agin')
        if playe_agin.lower() !='y':
            break
playing()       