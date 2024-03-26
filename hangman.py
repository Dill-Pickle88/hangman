import random

def hangman():
    my_list = ["cat", "dog",
               "parrot", "goldfish",
               "horse", "snake"]

    word = my_list[random.randint(0,5)]
    
    wrong = 0
    stages = ["",
             "_______           ",
             "|                 ",
             "|        |        ",
             "|        0        ",
             "|       /|\       ",
             "|       / \       ",
             "|                 "
             ]

    rletters = list(word)
    board = ["__"] * len(word)
    win = False
    print("welcome to Hangman")

    while wrong < len(stages) - 1:
        print("\n")
        msg = "Guess a letter"
        char = input(msg).lower()
        if char in rletters:
            cind = rletters.index(char)
            board[cind] = char
            rletters[cind] = '$'
        else:
            wrong += 1
        print((" ".join(board)))
        e = wrong + 1
        print("\n".join(stages[0:e]))
        if "__" not in board:
            print("You win!")
            print(" ".join(board))
            with open("win.txt", "w+") as f:
                f.write("Player 2 has won")
            win = True
            break
    if not win:
        print("\n".join(stages[0: wrong]))
        print("You lose! It was {}.".format(word))

hangman()
        

