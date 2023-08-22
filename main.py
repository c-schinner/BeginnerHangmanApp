import random

logo = ''' 
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/    '''

print(logo)


my_list = ['aardvark', 'camel', 'baboon']
display = []
unused_letters = []
chosen_word = random.choice(my_list)
game_over = False
lives = 6

print(f"HINT... the chosen word is {chosen_word}")

for letter in chosen_word:
    display.append("_")
print([' '.join(display)])

while not game_over:
    guess = input("Pick a letter: ").lower()

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print([' '.join(display)])
    print("\n")

    if guess in display:
        print(f"You've already guessed {guess}, try another letter.")

    elif guess not in display:
        unused_letters.append(guess)
        lives -= 1
        if lives == 0:
            print("Game Over, You Lose.")
            print(f"The hidden word was {chosen_word}")
            break
    print(f"Lives Remaining = {lives}")
    print(f"Letters not in the word\n{' '.join(unused_letters)}")
    print("\n")

    if "_" not in display:
        print("Congratulations you've WON!")
        break

print("Thanks for playing!")
