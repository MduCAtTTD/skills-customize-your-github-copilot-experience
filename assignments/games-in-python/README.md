# 📘 Assignment: Games in Python

## 🎯 Objective

Build a classic Hangman word-guessing game using Python to practice string manipulation, loops, conditionals, and random selection.

## 📝 Tasks

### 🛠️ Set Up the Game

#### Description
Create the foundation of the Hangman game by defining a word list and implementing random word selection and display logic.

#### Requirements
Completed program should:

- Define a predefined list of words to choose from
- Randomly select a word from the list using the `random` module
- Display the current guessed state of the word using underscores (e.g., `_ _ _ _`)


### 🛠️ Implement Game Logic

#### Description
Build the core gameplay loop that accepts player guesses, tracks progress, and determines the win or lose outcome.

#### Requirements
Completed program should:

- Accept a single letter guess from the player each turn
- Reveal correctly guessed letters in their proper positions
- Track and display the number of incorrect guesses remaining
- End the game when the word is fully guessed or attempts are exhausted
- Display an appropriate win or lose message at the end
