import numpy as np
from typing import Dict, List
from collections import defaultdict

Class Author(object):

    def read_text(path: str) -> str:    
        with open(path) as f:
            text = f.read().strip().lower().split()
        return text

    def word_frequencies(text: str) -> Dict[str, List[str]]:
        '''Create a dictionary defining an order 1 model of language'''

        word_freqs = defaultdict(lambda: [])

        for first_w, second_w in list(zip(text, text[1:])):
            word_freqs[first_w].append(second_w)
        return word_freqs

    def create_sentence(text: str, word_freqs: Dict[str, List[str]]) -> str:

        first_word = np.random.choice(text)

        chain = [first_word]

        while not '.' in chain[-1]:
            chain.append(np.random.choice(word_freqs[chain[-1]]))

        return ' '.join(chain)

    def paragraph(text: str, sentence_num: int=3) -> str:

        word_freqs = word_frequencies(text)
        paragraph = []

        for _ in range(sentence_num):
            paragraph.append(create_sentence(text, word_freqs))

        return '\n\n'.join(paragraph)