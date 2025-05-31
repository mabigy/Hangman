# Hangman Game in Python 🎮

This is a simple command-line implementation of the classic **Hangman** word-guessing game, written in Python.

## 🧠 About the Game

Hangman is a word-guessing game where the player tries to guess a secret word one letter at a time. Each incorrect guess reduces the player's number of lives. The game ends when the word is guessed correctly or when the player runs out of lives.

## 🕹️ How to Play

- The game chooses a random word from a list.
- You have 6 lives.
- Each time you guess a letter:
  - If it's correct, it fills in the blanks.
  - If it's wrong, you lose a life.
- The game ends when:
  - You guess the full word correctly.
  - You run out of lives.

## 📦 Features

- Random word selection
- Input validation
- Tracks letters you've already guessed
- Supports multiple playthroughs

## 💻 Requirements

- Python 3.x

## 🚀 How to Run

1. Open your terminal or command prompt
2. Navigate to the folder containing `hangman.py`
3. Run the script:

```bash
python hangman.py
