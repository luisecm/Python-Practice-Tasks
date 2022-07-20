# Write your code here
import random

options = ['python', 'java', 'kotlin', 'javascript']
winner = ""
attempts = 0
winner_switch = False
hidden_word = ""
winner_set = set(winner)
guessed_letters = []
typed_letters = []
game_switch = False

def initial_load():
    print("H A N G M A N")
    ask_action()

def ask_action():
    global game_switch
    while(game_switch == False):
        game_status = input('Type "play" to play the game, "exit" to quit:')
        if game_status == 'play':
            clear_variables()
            go_game()
            result()
        elif game_status == 'exit':
            game_switch = True

def clear_variables():
    global options
    global winner
    global attempts
    global winner_switch
    global hidden_word
    global winner_set
    global guessed_letters
    global typed_letters
    global game_switch
    winner = random.choice(options)
    attempts = 0
    winner_switch = False
    hidden_word = ""
    winner_set = set(winner)
    guessed_letters = []
    typed_letters = []
    game_switch = False

def go_game():
    global winner
    global hidden_word
    global attempts
    global winner_switch
    global typed_letters
    global guessed_letters
    global winner_set
    print("")
    for i in range(len(winner)):
        hidden_word = hidden_word + "-"
    hidden_word_list = list(hidden_word)
    while(attempts < 8 and winner_switch == False):
        print("")
        print(hidden_word)
        user_guess = input("Input a letter: ")
        if user_guess.islower() == False and len(user_guess) == 1:
            print("It is not an ASCII lowercase letter")
        else:
            if len(user_guess) != 1:
                print("You should input a single letter")
            else:
                if user_guess in typed_letters:
                    print("You already typed this letter")
                else:
                    if user_guess not in winner_set:
                        print("No such letter in the word")
                        typed_letters.append(user_guess)
                        attempts += 1
                    else:
                        guessed_letters.append(user_guess)
                        typed_letters.append(user_guess)
                        for i in range(len(winner)):
                            if winner[i] == user_guess:
                                hidden_word_list[i] = winner[i]
                                hidden_word = "".join(hidden_word_list)
                        if guessed_letters == winner_set:
                            winner_switch = True

def result():
    global winner_switch
    if winner_switch == False:
        print("You are hanged!")
        ask_action()
    else:
        print("You survived!")
        ask_action()
        
initial_load()
