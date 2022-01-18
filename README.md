# Wordle Helper
A program to find better words for solving [Wordle](powerlanguage.co.uk) puzzles.
![image](https://user-images.githubusercontent.com/16577014/149848610-9d3cc7bc-2524-4dca-bbf2-934db3262b25.png)

## Warning
This program takes the fun out of Wordle puzzles. 

It was developed solely as a programming exercise. Please use it at your own risk.

## Description
This program uses statistics in a word list to make better guesses in a Wordle puzzle.

Currently, it simply ranks words by frequencies characters appear in specific places.

A demo version is also included to let the helper guess a word you pick. 

## Getting Started
### Prerequisites
Python 3.9+
### Installation
1. Clone the repository
2. Run `pip install -r requirements.txt` in the directory.
3. Run `python load_words.py` to download words.
#### Usage
To get help playing wordle, run `python wordle_helper.py`.

To let the helper guess your word, run `python wordle_demo.py`

## Credits
Word list from [dwyl/english-words](https://github.com/dwyl/english-words)
