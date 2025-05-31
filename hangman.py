import random

words = ["bola", "kolapo", "bisi", "drug"]
secret_word = random.choice(words)

def player_word():
  return ["__" for _ in secret_word]

def guess_word():
 return input("Enter a letter for the word: ")

def play_game():
  guessed_word = player_word()
  guessed_letter = []

  lives = 6

  while lives > 0 and "__" in guessed_word:
    secret_word = random.choice(words)
    print(f"Curent word: " + " ".join(guessed_word))
    guess = guess_word()

    if guess in guessed_letter:
      print("Letter have already been guessed, try again!")
      continue

    guessed_letter.append(guess)

    if guess in secret_word:
      for i, letter in enumerate(secret_word):
        if letter == guess:
          guessed_word[i] = guess
          print("Good guess!")
    else:
      lives -= 1
      print(f"Guessed wrong! Your remaining lives: {lives}")

  if "__" not in guessed_word:
    print("Congratulations! You won the Game")
    print(f"The Current word: " + " ".join(secret_word))
  else:
    print(f"Game Over! The secret word is {secret_word}")

  

while True:
  play_game()
  replay = input("Play Again(P)?: ")

  if replay.lower().strip() != "p":
    break