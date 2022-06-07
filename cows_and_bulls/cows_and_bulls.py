def get_cows_and_bulls(c_word, g_word):
    cows = 0
    bulls = 0
    return cows, bulls


print("The word that the computer is thinking of is a 4-letter word.")
word = "tent"

guess = input("Enter a 4-letter word: ")
while guess != word:
    cows, bulls = get_cows_and_bulls(word, guess)
    print("There are", cows, "cows and", bulls, "bulls.")
    guess = input("Enter a different 4-letter word: ")

print("Yay! You got the correct word!")