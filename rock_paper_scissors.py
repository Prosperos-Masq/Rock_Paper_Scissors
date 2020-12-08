import random
pick = ['rock', 'paper', 'scissors']
while True:
    tick = random.choice(pick)
    choice = input('Ready? rock, paper, scissors shoot! ')
    if choice == tick:
        print('Its a tie!')
    elif choice == 'rock':
        if tick == 'paper':
            print(f'Uh oh! {tick} beats {choice}, you lose!')
        else:
            print(f'Yes! {choice} beats {tick}, you win!')
    elif choice == 'paper':
        if tick == 'scissors':
            print(f'Uh oh! {tick} beats {choice}, you lose!')
        else:
            print(f'Yes! {choice} beats {tick}, you win!')
    elif choice == 'scissors':
        if tick == 'rock':
            print(f'Uh oh! {tick} beats {choice}, you lose!')
        else:
            print(f'Yes! {choice} beats {tick}, you win!')
    else:
        print('That input was invalid, please try again!')

print(random.choice(pick))
print(tick)