import random

# Predefined list of words
words = ["python", "apple", "computer", "engineer", "college"]

# Select a random word
word = random.choice(words)

# Create blanks for the word
guessed_word = ["_"] * len(word)

# Store guessed letters
guessed_letters = []

# Maximum incorrect guesses
attempts = 6

print("🎮 Welcome to Hangman Game!")
print("Guess the word one letter at a time.")

while attempts > 0 and "_" in guessed_word:

    print("\nWord:", " ".join(guessed_word))
    print("Incorrect guesses left:", attempts)

    guess = input("Enter a letter: ").lower()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single alphabet letter.")
        continue

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check if letter is in word
    if guess in word:
        print("✅ Correct Guess!")

        for i in range(len(word)):
            if word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong Guess!")
        attempts -= 1

# Final result
if "_" not in guessed_word:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n💀 Game Over!")
    print("The word was:", word)