def hangman():
    
    def empty_board():
        print('_____  ')
        print('|    | ')
        print('|      ')
        print('|      ')
        print('|      ')
        print('|      ')

    def strike_one():
        print('_____  ')
        print('|    | ')
        print('|    O ')
        print('|      ')
        print('|      ')
        print('|      ')

    def strike_two():
        print('_____   ')
        print('|    |  ')
        print('|    O  ')
        print('|    |  ')
        print('|       ')
        print('|       ')

    def strike_three():
        print('_____  ')
        print('|    |  ')
        print('|    O  ')
        print('|   /|  ')
        print('|       ')
        print('|       ')

    def strike_four():
        print('_____   ')
        print('|    |  ')
        print('|    O  ')
        print('|   /|\ ')
        print('|       ')
        print('|       ')

    def strike_five():
        print('_____   ')
        print('|    |  ')
        print('|    O  ')
        print('|   /|\ ')
        print('|   /   ')
        print('|       ')

    def strike_six():
        print('_____   ')
        print('|    |  ')
        print('|    O  ')
        print('|   /|\ ')
        print('|   / \ ')
        print('|       ')
        
        
    #IMPORTING RANDOM WORD LIBRARY ???
    words = []
    with open('/usr/share/dict/words') as f:
        for line in f:
            words.append(line.strip())

    import random
    #GENERATED_WORD IS THE RANDOM WORD TO GUESS
    generated_word = str(random.choice(words).lower())

    display = (['-'] * len(generated_word))
    #Display is a list, needs joined

    incorrect_guesses = []

    strikes = 0

    #INITIAL DISPLAY
    print("Welcome to Hangman")
    print(' ')
    empty_board()
    print(' ')
    print(''.join(display))

    while True:
        
        def round_summary():
            if strikes == 0:
                empty_board()
            elif strikes == 1:
                strike_one()
            elif strikes == 2:
                strike_two()
            elif strikes == 3:
                strike_three()
            elif strikes == 4:
                strike_four()
            elif strikes == 5:
                strike_five()
            elif strikes == 6:
                strike_six()
            print(' ')
            print(' ')
            print(''.join(display))
            print(f'Incorrect guesses: {incorrect_guesses}')
            print('_' * 25)
            print(' ' * 25)
    
        #WIN check
        if '-' not in display:
            print('Congratulaions! You Win')
            return
        #LOSE check
        elif strikes == 6:
            print(f'GAME OVER. The word is {generated_word}')
            return
            
        letter_guess = input('Please guess a letter: ').lower()
        
        def find_all(letter_guess, generated_word):
            """Return array of indices where letter appears in word"""
            return [i for i, letter in enumerate(generated_word) if letter == letter_guess]
            
        if letter_guess in incorrect_guesses or letter_guess in display:
            print('Already guessed, try again.')
            
        elif letter_guess in generated_word:
            matches = find_all(letter_guess, generated_word)
            for i in matches:
                display[i] = letter_guess
            round_summary()
        
        else:
            strikes += 1
            incorrect_guesses.append(letter_guess)
            round_summary()
