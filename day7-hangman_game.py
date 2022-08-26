# Hangman game
import random
from hangman_art import stages, logo
from english_words import english_words_set as set

list = list(set)
chosen_word = random.choice(list).lower()

#print(word)

lives = 6
display = []
for x in range(len(chosen_word)):
    display += ('_')
print(f"{' '.join(display)}")

l = []
end_of_game = False
while  not end_of_game:
    guess = input("Guess a letter: ").lower()
   
    if guess in l:
        print(f"You've already guessed {guess}")
        
    else:
        for position in range(len(chosen_word)):
            letter = chosen_word[position]
            if guess == letter:
                display[position] = letter
                
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed '{guess}' that is not in word. You lose a life.")
            if lives == 0:
                end_of_game = True
                print("You lose")

    print(f"{' '.join(display)}")
            
    if "_" not in display:
        end_of_game = True
        print('you win')
    print(stages[lives])
    l.append(guess)

print("GAME ENDS!!")
print("Word is : ", chosen_word)








        
