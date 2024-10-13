import random

hangman = """ _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _' | '_ \ / _' | '_ ' _ \ / _' | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/"""

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)

print(hangman)

placeholder = ""
for letter in chosen_word:
    placeholder += "_"
print(f"Word to guess: {placeholder}")
lives = 6
letters = []

while lives > 0:
    guess = input("Guess a letter:\n").lower()
    display = ""

    for letter in chosen_word:
        if guess == letter:
            display += letter
            letters.append(guess)
        elif letter in letters:
            display += letter
        else:
            display += "_"

    if guess not in chosen_word:
        lives -= 1
        print(stages[lives])
        print(f"{lives}/6 LIVES LEFT")
        print(display)
        print(f"You guessed {guess}, that's not in the word, you lose a life!")
        if lives == 0:
            print(f"GAME OVER! The word was {chosen_word}")
    else:
        print(display)
        print(f"{lives}/6 LIVES LEFT")
        if "_" not in display:
            print("You have won!")

            break
