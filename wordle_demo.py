from wordle_helper import WordleHelper

with open('words.txt', 'r') as f:
    words = f.read().split()

print(f'{len(words)} words loaded')

while True:
    word = input("Enter a word: ")
    if word in words:
        break
    print('Word not in list')


helper = WordleHelper(words)
feedbacks = []
guess_count = 0

while True:
    print(f'Possible words: {len(words)}')
    guess = helper.choose_word(words)
    print(f'Helper tried word: {guess}')
    feedback = ''
    for i, char in enumerate(guess):
        if char == word[i]:
            feedback += 'g'
        elif char in word:
            feedback += 'y'
        else:
            feedback += 'b'
    print(f'Feedback: {feedback}')
    guess_count += 1
    if feedback == 'ggggg':
        print(f'Helper got answer in {guess_count} guesses')
        break
    feedbacks.append(WordleHelper.WordleFeedback(guess, feedback))
    words = helper.filter_words(feedbacks)
