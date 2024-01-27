import random

def green(text):
    '''Letter in word, letter in right place'''
    return f"\u001b[42m\u001b[37;1m{text}\u001b[0m"

def yellow(text):
    '''Letter in word, letter in wrong place'''
    return f"\u001b[43m\u001b[37;1m{text}\u001b[0m"

def gray(text):
    '''Letter not in word'''
    return f"\u001b[42m\u001b[1;47m{text}\u001b[0m"

with open('Miscellaneous\Wordle\wordle-answers.txt', 'r') as file_answers, open('Miscellaneous\Wordle\wordle-guesses.txt', 'r') as file_guesses: 
    answers_data = file_answers.readlines()
    word = random.choice(answers_data).upper().strip()
    guesses_data = [line.strip().upper() for line in file_guesses]

alphabet = {chr(n):chr(n) for n in range(65, 91)}
valid_guess, correct = False, False
guesses_history, temp_list = [], []
while (len(guesses_history) < 6) and not correct:
    for previous_guesses in guesses_history:
        print(' '.join(previous_guesses))
    for _ in range(6-len(guesses_history)):
        print('_ _ _ _ _')
    print('\n' + ' '.join(alphabet.values()))
    while not valid_guess:
        guess = input('Input your guess: ').upper()
        print()
        if len(guess) != 5:
            print('Your guess should be 5 letters')
        elif guess not in guesses_data:
            print('Not a valid guess')
        else:
            valid_guess = True
    valid_guess = False
    for index, letter in enumerate(list(guess)):
        if (letter not in word):
            temp_list.append(gray(letter))
            alphabet[letter] = gray(letter)
        elif (letter in word) and (letter == word[index]):
            temp_list.append(green(letter))
            alphabet[letter] = green(letter)
        elif (letter in word) and (letter != word[index]):
            if word.count(letter) >= guess.count(letter):
                temp_list.append(yellow(letter))
                alphabet[letter] = yellow(letter)
            elif (guess.count(letter) in [2, 3]) and (word.count(letter) == 1):
                if index == guess.index(letter):
                    temp_list.append(yellow(letter))
                    alphabet[letter] = yellow(letter)
                else:
                    temp_list.append(gray(letter))
                    alphabet[letter] = gray(letter)
            elif (guess.count(letter) == 3) and (word.count(letter) == 2):
                if index == guess.index(letter):
                    temp_list.append(yellow(letter))
                    alphabet[letter] = yellow(letter)
                elif index == guess.rindex(letter):
                    temp_list.append(gray(letter))
                    alphabet[letter] = gray(letter)
                else:
                    temp_list.append(yellow(letter))
                    alphabet[letter] = yellow(letter)

    guesses_history.append(temp_list[:])
    if guess == word:
        correct = True
        for previous_guesses in guesses_history:
            print(' '.join(previous_guesses))
        for _ in range(6-len(guesses_history)):
            print('_ _ _ _ _')
    temp_list.clear()
if correct:
    print('Congrats, you guessed the word!')
    print(f'You were able to guess it in {len(guesses_history)} guesses')
else:
    for previous_guesses in guesses_history:
        print(' '.join(previous_guesses))
    print(f'You ran out of guesses! The correct word was {word}')