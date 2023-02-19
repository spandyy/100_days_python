# #Hangman

from hangman_words import word_list
from hangman_art import stages,logo
print(logo)

import random
# l1=["dog", "pussycat", "dukkar"]

word=random.choice(word_list)

#empty list with blanks of the chosen word
l2=[]
for i in range(len(word)):
    l2.append("_")

print(l2)

lives=6

end_of_game=True
while end_of_game:
    #letter gussing
    guess=input("Enter the letter: \n").lower()

    #the letter matched is replaced with the blank
    for i in range(len(word)):
        if word[i]==guess:
            l2[i]=word[i]
            

    print(l2)

    #lives are 6 if guessed wrong then decreased by 1 each time when zero then you lose 
    if guess not in word:
        lives =lives-1
        if lives == 0:
            end_of_game = False
            print("You lose.")
            
    # if guessed wrong then decrement else same index of stages print
    print(stages[lives])

    #to get out of loop when no blank left to fill
    if "_" not in l2:
        end_of_game=False
        print("you win")
        print(f"with {lives} attempts left to death")
        break

print("The word was: ",word )
