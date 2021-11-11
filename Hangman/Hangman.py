# First import pakage termcolor

import random
from termcolor import colored
import figure

print(colored('All the word are related to computer','red',attrs=['reverse', 'blink']))
# Warning : please don't enter the words which have repeated character example 'seek' 'Peek' etc..
letters_list = ['keys','mouse', 'desktop', 'keyboard', 'pixel']
random_word = random.choice(letters_list)


empty_list = []
for i in range(0, len(random_word)):
    empty_list.append("_")
# print(empty_list)
# print(random_word)

end_of_game = False
lives = 6
while not end_of_game:
    if lives == 0:
        print('You lose the game')
        end_of_game = True
    else:
        if '_' in empty_list:
            entered_chr = input('Enter any character').lower()
            if entered_chr in random_word:
                get_index = random_word.index(entered_chr)
                empty_list[get_index] = entered_chr
                print(*empty_list,sep='')
            else:
                print(figure.HANGMANPICS[lives - 1])
                lives -= 1
                # print(f'lives remaining = {lives}')
                print(colored(f'lives remaining  {lives}','red'))
        else:
            print('you win')
            end_of_game = True
            print(colored('The word is ', 'green'),end='')
            print(*empty_list,sep='')
