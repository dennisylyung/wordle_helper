import requests

if __name__ == '__main__':
    r = requests.get('https://github.com/dwyl/english-words/raw/master/words_alpha.txt')
    r.raise_for_status()

    word_list = r.text.splitlines()
    word_count = 0
    with open('words.txt', 'w') as f:
        for word in word_list:
            if len(word) == 5:
                if len({c for c in word}) == 5:
                    f.write(word + '\n')
                    word_count += 1
    print(f'{word_count} words written to words.txt')