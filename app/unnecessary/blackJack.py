# Test 1
# name = input("What is your name? \n")
# print("Hello,", name)
# a = 1
# b = 2
# print("a = ", a, ", b = ", b)
# if (a == 1) or (a != 2):
#     print("a != ", b)


# Blackjack game
import random

cardDeck = [6, 7, 8, 9, 10, 2, 3, 4, 11] * 4
random.shuffle(cardDeck)

game = input('Do you want a play? y/n\n')
count = 0

if game == 'y':
    while True:
        choice = input('Do you will take a card? y/n\n')
        if choice == 'y':
            current = cardDeck.pop()
            print('You have the card with value %d' % current)
            count += current

            if count > 21:
                print('Sorry, you lost')
                break
            elif count == 21:
                print('Congratulations! You win!')
                break
            else:
                print('You have %d points' % count)
        elif choice == 'n':
            print('You have %d points and you have end of the game' % count)
            break
        else:
            print('Please enter Y or N')

print('Good bye!')
