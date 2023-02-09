import random
words = "baboon beehive loop electric bumble saliva jumper wrench tamper follow jade halves saunter return doorknob center candidate develop garden generation hundred opportunity organization political prepare president score scientist significant world staff republic performance".split()
word_array = []
word = random.choice(words)
for char in word:
    word_array.append(char)
    
blank_word_array = ["_"] * len(word_array)
wrong_letters = []
correct_letters = []
guesses = len(word) + 3
game_finished = False
letter_guessed = ''

def display_array(blank_word_array):
    for letter in blank_word_array:
        i = blank_word_array.index(letter)
        if letter in correct_letters:
            blank_word_array = blank_word_array[:i] + [letter] + blank_word_array[i+1:]
    print (blank_word_array)

def check_letter(letterInput):
    if len(letterInput) > 1:
        print ("Enter only one letter please")
        return False
    elif len(letterInput) < 1:
        print ("Please enter a letter")
        return False
    elif letterInput in wrong_letters or letterInput in correct_letters:
        print ("You already guessed this letter")
        return False
    elif not letterInput.isalpha():
        print ("Enter a letter please")
        return False
    else:
        return True    

def play_game(letter):
    global guesses
    if letter in word_array:
        index = 0
        for x in word_array:
            if x == letter:
                blank_word_array[index] = letter
            index = index + 1
        correct_letters.append(letter)
    else:
        wrong_letters.append(letter)
        guesses = guesses - 1

print ("Welcome to Hangman!")
while guesses > 0:
    print ("-----------------------------")
    display_array(blank_word_array)
    print ("You have " + str(guesses) + " guesses left")
    print ("Wrong letters: " + ", ".join(wrong_letters))
    
    letter_guessed = input("Please guess a letter: ")
    letter_guessed = letter_guessed.lower()
    if check_letter(letter_guessed):
        play_game(letter_guessed)

    if word_array == blank_word_array:
        game_finished = True
        break

if game_finished == True:
    print("You guessed the word!\nThe word is: " + word)
else:
    print("Sorry you didn't get the word!\nThe word is: " + word)






    
    
    
