import random

def hangman():

    words = ['python', 'java_script', 'Kotlin', 'html', 'css']

    shuffle = random.randint(0, 4)

    word = words[shuffle]

    wrong = 0

    stages = ["",
              "_________        ",
              "|                ",
              "|        |       ",
              "|        0       ",
              "|       /|\      ",
              "|       / \      ",
              "|       `  '     ",
              "|                "
              ]

    remainig_letters = list(word)

    board = ['_'] * len(word)

    win = False

    print('Welcome to Hangman')


    while wrong < len(stages) - 1:
        print('\n')
        msg = 'guess a letter: '
        char = input(msg)

        if char in remainig_letters:
            cind = remainig_letters.index(char)
            board[cind] = char
            remaining_letters[cind] = '$'

        else:
            wrong += 1
            print(' '.join(board))
            e = wrong + 1
            print('\n'.join(stages[0: e + 1]))

        if '_' not in board:
            print('You win')
            print(' '.join(board))
            win = True
            break

        if not win:
            print('\n'.join(stages[0: wrong]))
            print('You lose! It was {}.'.format(word))
hangman()

