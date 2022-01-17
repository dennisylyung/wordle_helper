import string

import numpy as np


class WordStatistics:

    def __init__(self, words: list[str]):
        self.words = words
        self.word_count = len(words)
        self.words_mask = np.zeros((self.word_count, 26, 5), dtype=np.int)
        self.statistics = np.zeros((26, 5), dtype=int)
        for i, word in enumerate(words):
            for j, char in enumerate(word):
                char_index = ord(char) - ord('a')
                self.words_mask[i, char_index, j] = 1
                self.statistics[char_index, j] += 1
        self.word_scores = (self.words_mask * self.statistics).sum(axis=2).sum(axis=1)

    def frequencies(self):
        return self.statistics.sum(axis=1) / self.word_count

    def top_word(self):
        return self.words[np.argmax(self.word_scores)]


if __name__ == '__main__':
    with open('words.txt', 'r') as f:
        words = f.read().split()

    print(f'{len(words)} words loaded')

    statistics = WordStatistics(words)

    print('Frequencies:')
    for char, frequency in zip(string.ascii_lowercase, statistics.frequencies()):
        print(f'{char} - {frequency * 100:.2f}%')

    print(f'Top word: {statistics.top_word()}')
