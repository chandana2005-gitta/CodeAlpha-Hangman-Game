import random

words = ["python", "apple", "coding", "laptop", "future"]

word = random.choice(words)
guessed = ["_"] * len(word)

attempts = 6

print("🎮 Welcome to Hangman!")

while attempts > 0 and "_" in guessed:

    print("\nWord:", " ".join(guessed))
    print("Attempts Left:", attempts)

    letter = input("Guess a letter: ").lower()

    if letter in word:
        for i in range(len(word)):
            if word[i] == letter:
                guessed[i] = letter
    else:
        attempts -= 1
        print("Wrong Guess!")

if "_" not in guessed:
    print("\n🎉 Congratulations! You guessed the word:", word)
else:
    print("\n❌ Game Over!")
    print("The word was:", word)