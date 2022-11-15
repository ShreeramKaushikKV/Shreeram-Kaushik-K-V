import random
import sys
game = ['Rock', 'Paper', 'Scissor']
lost = 0
win = 0
tied = 0
while True:
    print("Enter your choice(e.g.,Rock,Paper,Scissor,quit=' ')")
    choice = input()
    if choice == '':
        sys.exit()
    print('Computer choice')
    comp = random.choice(game)
    print(comp)
    if comp == choice:
        print('Tied')
        tied = tied + 1
    elif choice == 'Rock' and comp == 'Paper':
        print('You lost')
        lost = lost + 1
    elif choice == 'Rock' and comp == 'Scissor':
        print('you Won')
        win = win + 1
    elif choice == 'Paper' and comp == 'Scissor':
        print('you lost')
        lost = lost + 1
    elif choice == 'Paper' and comp == 'Rock':
        print('you Won')
        win = win + 1
    elif choice == 'Scissor' and comp == 'Paper':
        print('you Won')
        win = win + 1
    elif choice == 'Scissor' and comp == 'Rock':
        print('you lost')
        lost = lost + 1
    print('The number of Wins are' + ' ' + str(win))
    print('The number of lost are' + ' ' + str(lost))
    print('The number of tied matches are' + ' ' + str(tied))
