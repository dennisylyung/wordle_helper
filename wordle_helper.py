import sys
from typing import Dict, Any, Union, Set

from word_statisitcs import WordStatistics


class WordleHelper:
    class WordleFeedback:
        def __init__(self, word: str, color: str):
            self.word = word
            self.color = color
            self.inclusion_filter = {}
            self.exclusion_filter = set()
            for i, char, c in zip(range(5), word, color):
                if c.lower() == 'g':
                    self.inclusion_filter[char] = {i}
                elif c.lower() == 'y':
                    self.inclusion_filter[char] = {j for j in range(5) if j != i}
                elif c.lower() == 'b':
                    self.exclusion_filter.add(char)

    def __init__(self, word_list: list[str]):
        self.word_list = word_list

    def filter_words(self, feedbacks: list[WordleFeedback]) -> list[str]:
        inclusion_filter, exclusion_filter = self.combine_feedbacks(feedbacks)
        return [word for word in self.word_list if self.filter_word(inclusion_filter, exclusion_filter, word)]

    @staticmethod
    def filter_word(inclusion_filter: Dict[str, Set[int]], exclusion_filter: Set[str], word: str) -> bool:
        for char, indices in inclusion_filter.items():
            if char not in word or word.index(char) not in indices:
                return False
        for char in exclusion_filter:
            if char in word:
                return False
        return True

    @staticmethod
    def combine_feedbacks(feedbacks: list[WordleFeedback]) -> tuple[Any, Union[set[Any], Any]]:
        inclusion_filter = {}
        exclusion_filter = set()
        for feedback in feedbacks:
            for char, indices in feedback.inclusion_filter.items():
                if char in inclusion_filter:
                    inclusion_filter[char] = inclusion_filter[char].intersection(indices)
                else:
                    inclusion_filter[char] = indices
            exclusion_filter = exclusion_filter.union(feedback.exclusion_filter)
        return inclusion_filter, exclusion_filter

    @staticmethod
    def choose_word(words):
        return WordStatistics(words).top_word()


if __name__ == "__main__":

    with open('words.txt', 'r') as f:
        words = f.read().split()

    print(f'{len(words)} words loaded')

    helper = WordleHelper(words)
    feedbacks = []

    while True:
        print(f'Possible words: {len(words)}')
        while True:
            word = helper.choose_word(words)
            print(f'try word: {word}')
            colors = input('Feedback colors\n g for green, y for yellow, b for black (e.g. "ybybg")\n'
                           'inpout "n" for not in word list:')
            if colors == 'n':
                words.remove(word)
                continue
            elif colors == 'ggggg':
                print('Congrats, you win!')
                sys.exit(0)
            else:
                break
        feedbacks.append(WordleHelper.WordleFeedback(word, colors))
        words = helper.filter_words(feedbacks)
