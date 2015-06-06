from .logic import LogicAdapter
from collections import Counter
import nltk
import string


from nltk.data import path
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk import pos_tag


from nltk.corpus import stopwords
from nltk import word_tokenize

'''
Get the distance between each word in a sentence.
'''

#path.append("./nltk_data/")

"""
Similarity

http://www.nltk.org/howto/wordnet.html
Return a score denoting how similar two word senses are, based on the shortest path that connects the senses in the is-a (hypernym/hypnoym) taxonomy. The score is in the range 0 to 1. By default, there is now a fake root node added to verbs so for cases where previously a path could not be found---and None was returned---it should return a value. The old behavior can be achieved by setting simulate_root to be False. A score of 1 represents identity i.e. comparing a sense with itself will return 1.
"""

class ClosestMeaningAdapter(LogicAdapter):

    def get_tokens(self, text, exclude_stop_words=True):
        """
        Takes a string and converts it to a tuple
        of each word. Skips common stop words such
        as ("is, the, a, ...") is 'exclude_stop_words'
        is True.
        """
        lower = text.lower()
        tokens = word_tokenize(lower)

        # Remove any stop words from the string
        if exclude_stop_words:
            excluded_words = stopwords.words("english")

            for token in tokens:
                if token in excluded_words:
                    tokens.remove(token)
        return tokens
        

    def get_similarity(self, string1, string2):
        """
        Calculate the similarity of two statements.
        """

        tokens1 = self.get_tokens(string1)
        tokens2 = self.get_tokens(string2)

        print tokens1, tokens2

        while len(tokens1) > 0:
            token1 = tokens1.pop()

            for token2 in tokens2:
                print token1, token2

                synset1 = wordnet.synsets(token1)
                synset2 = wordnet.synsets(token2)

                print synset1
                print synset2

                if synset1 and synset2:

                    # Compare the first synset in each list of synsets
                    print synset1[0].path_similarity(synset2[0])

        return ""

    def get(self, text, list_of_statements):
        """
        Takes a statement string and a list of statement strings.
        Returns the closest matching statement from the list.
        """

        # Check if an exact match exists
        if text in list_of_statements:
            return text

        similarity = self.get_similarity(text, text)
        print similarity

        # Get the closest matching statement from the database
        return text
