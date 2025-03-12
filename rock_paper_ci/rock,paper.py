import random
def check(me,pc,pc_wins,me_wins):
    if me == 'r' and pc == 'p':
       print('pc win')
       pc_wins+=1
    elif me == 'p' and pc == 'c':
       print('pc win')
       pc_wins+=1
    elif me == 'c'  and pc == 'r':
       print('pc win')
       pc_wins+=1
    elif me == pc:
        print('tie')
    else:
        print('me win')
        me_wins+=1
    return pc_wins,me_wins

pc_wins = 0
me_wins =0
data = {'r':'rock','p':'paper', 'c':'clip'}
d=['g','p','r','c']
while True: 
    player = random.choice(['r','p','c'])
    me = input('enter your choice:')
    if me == 'q':
        break
    if me =='g':
        print(f"you win :{me_wins} times and pc wins {pc_wins} times")
    elif me not in d:
        print('invild choice')
        continue
    if me in data:
        print(f'Player choice: {data[me]} | PC choice: {data[player]}')
        pc_wins,me_wins= check(me,player,pc_wins,me_wins)
   

    
    
        
