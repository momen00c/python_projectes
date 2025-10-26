import random
def roll():
    min_value =1
    max_value = 6
    roll = random.randint(min_value,max_value)
    return roll

while True:
    player = input('inter number of player (2-4)')
    if player.isdigit():
        player = int(player)
        if 2<= player <= 4:
            break
        else:
            print('must be between 2-4 players')
    else:
        print('inveld value')

max_score = 50
player_score = [0 for _ in range(player)]
while max(player_score) < max_score:
    for player_index in range(player):
        print('player:',player_index +1)
        curent_score = 0
        while True:
            should_role = input('would you like roll press y')
            if should_role !='y':
                break

            value = roll()
            if value == 1:
                print('you rolled 1 turn done') 
                curent_score = 0
                break
            else:
                curent_score += value
                print('you rolle ',value)
        player_score[player_index] += curent_score
        print('your totla score:',player_score[player_index])