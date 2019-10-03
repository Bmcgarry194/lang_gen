import numpy as np
from typing import Dict, List
from collections import defaultdict

class Author:
    
    def __init__(self):
        self.text = None
        self.word_frequencies = defaultdict(lambda: [])
        
    def __len__(self):
        return len(self.text)
    
    def read_text(self, new_text=None, path=None) -> str:
        '''Adds text in either as a direct string format or a path to a text file'''
        if path:
            with open(path) as f:
                new_text = f.read()
        split_text = new_text.strip().lower().split()
        
        self.text = split_text
        
        for first_w, second_w in list(zip(self.text, self.text[1:])):
            self.word_frequencies[first_w].append(second_w)
            
    def add_text(self, new_text=None, path=None):
        '''
        Add additional books to the current library of text which the text genreation is based on.
        '''
        if path:
            with open(path) as f:
                new_text = f.read()
        split_text = new_text.strip().lower().split()
        
        for first, second in zip(split_text, split_text[1:]):
            self.word_frequencies[first].append(second)
            
        self.text.extend(split_text)

    def create_sentence(self) -> str:
        '''Generates a sentence based on the texts added to the corpus. The end of a sentence occurs when a word is added which contains a period.'''

        first_word = np.random.choice(self.text)

        chain = [first_word]
        
        #This approach could be a problem if there are no periods in the corpus
        while not '.' in chain[-1]:
            chain.append(np.random.choice(self.word_frequencies[chain[-1]]))

        return ' '.join(chain)

    def create_paragraph(self, sentence_num=3) -> str:
        '''Generates a specified number of sentences separted by a newline'''

        paragraph = []

        for _ in range(sentence_num):
            sentence = self.create_sentence()
            paragraph.append(sentence)
        return '\n\n'.join(paragraph)

if __name__ == '__main__':
	author = Author()
	author.read_text(path='data/dracula.txt')
	print(author.create_sentence())
