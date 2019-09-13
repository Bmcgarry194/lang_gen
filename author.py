import numpy as np
from typing import Dict, List
from collections import defaultdict

class Author:
    
    def __init__(self):
        self.text = None
        self.word_frequencies = None 
        
    def __len__(self):
        return len(self.text)
    
    def read_text(self, path: str) -> str:  
        with open(path) as f:
            text = f.read().strip().lower().split()
        self.text = text
        
        word_freqs = defaultdict(lambda: [])

        for first_w, second_w in list(zip(self.text, self.text[1:])):
            word_freqs[first_w].append(second_w)
            
        self.word_frequencies = word_freqs

    def create_sentence(self) -> str:

        first_word = np.random.choice(self.text)

        chain = [first_word]

        while not '.' in chain[-1]:
            chain.append(np.random.choice(self.word_frequencies[chain[-1]]))

        return ' '.join(chain)

    def create_paragraph(self, sentence_num=3) -> str:

        paragraph = []

        for i, _ in enumerate(range(sentence_num)):
            sentence = self.create_sentence() 
            paragraph.append(sentence)
        return '\n\n'.join(paragraph)
