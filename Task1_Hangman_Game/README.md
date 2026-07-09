Hangman Game
Overview
The Hangman Game is a command-line Python application developed as part of the CodeAlpha Python Programming Internship. It is a classic word-guessing game where the player tries to identify a hidden word by guessing one letter at a time.

The player has a limited number of incorrect attempts. Each correct guess reveals the letter's position(s) in the word, while each incorrect guess reduces the remaining attempts. The game ends when the player successfully guesses the entire word or runs out of attempts.

This project demonstrates the use of Python fundamentals such as loops, conditional statements, functions, lists, strings, and user input handling.

Objective
The objective of this project is to build an interactive command-line game that allows users to:

Guess a randomly selected word letter by letter.
Receive immediate feedback for each guess.
Track remaining attempts.
Win by correctly guessing the complete word before exhausting all attempts.
Features
Randomly selects a word from a predefined word list.
Accepts one-letter guesses from the user.
Reveals correctly guessed letters in their correct positions.
Reduces the number of attempts for incorrect guesses.
Prevents duplicate letter guesses.
Displays the current progress after every guess.
Announces whether the player wins or loses.
Simple and user-friendly command-line interface.
Technologies Used
Programming Language: Python
Python Module: random
Project Structure
Hangman_Game/ │── hangman.py └── README.md

Sample Output
Welcome to Hangman!

Word: _ _ _ _ _

Attempts Remaining: 6

Enter a letter: a

Correct Guess!

Word: A _ _ _ _

Attempts Remaining: 6

Enter a letter: e

Wrong Guess!

Attempts Remaining: 5

Concepts Used
Variables and Data Types
Lists and Strings
Conditional Statements (if, elif, else)
Loops (while, for)
Functions
Random Module
User Input Handling
Basic Game Logic
Problem Solving
Future Enhancements
Add difficulty levels (Easy, Medium, Hard).
Read words from an external text file.
Display ASCII art for the hangman.
Add score tracking.
Allow multiple rounds without restarting the program.
Create a graphical user interface (GUI) using Tkinter or Pygame.
Learning Outcomes
Through this project, I gained practical experience in:

Building an interactive command-line application.
Implementing game logic using Python.
Managing user input and validating data.
Writing clean, readable, and modular code.
Applying programming concepts to solve real-world problems.
Author
Bhavitha Gande

CodeAlpha Python Programming Internship
