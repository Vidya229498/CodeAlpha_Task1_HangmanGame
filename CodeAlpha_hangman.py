import random
words = ["apple", "banana", "grapes", "orange", "mango"]
word = random.choice(words)
display = ["_" for _ in word]
guessed_letters = []
max_wrong = 6
wrong = 0

print("(DEBUG) the chosen word is",word)
print("Welcome to Hangman Game!")
print("Guess the fruit name.\n")

while wrong < max_wrong and "_" in display:
    print("Word:", " ".join(display))
    print("Guessed letters:", " ".join(guessed_letters))
    print("Chances left:", max_wrong - wrong)
    
    guess = input("Enter a letter: ").lower()

    if guess =="":
        print("Please type a letter,not empty!\n")
        continue
    
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter one alphabet letter.\n")
        continue
    if guess in guessed_letters:
        print("You already guessed that letter!\n")
        continue
    
    guessed_letters.append(guess)
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct guess!\n")
    else:
        wrong += 1
        print("Wrong guess!\n")

if "_" not in display:
    print("You won! The word was:", word)
else:
    print("You lost! The word was:", word)