import nltk
from nltk.book import *

def searching_text_1():
    text1.concordance("monstrous")

def searching_text_2():
    text1.similar("monstrous")
    text2.similar("monstrous")

def searching_text_3():
    text2.common_contexts(["monstrous", "very"])

def searching_text_4():
    text4.dispersion_plot(["citizens", "democracy", "freedom", "duties", "America"])

def counting_vocabulary_1():
    print len(text1)
    print len(text2)
    print len(text3)
    print len(text4)

def counting_vocabulary_2():
    return sorted(set(text3))

def counting_vocabulary_3():
    return len(set(text3))

def counting_vocabulary_4():
    return text3.count("smote")

"""Lexical richness of the text; get a count on the number of times
each word is used on average.

Note that len() gives the number of tokens (not characters).

The unique set of tokens (independently of case), is called "word types"
(a unique item of vocabulary). Running set() on the text includes
punctuation so this is more commonly referred to as simply "types."
"""
def lexical_diversity(text):
    return len(text) / len(set(text))

"""Returns what percentage of the text is taken up by a particular
word.
"""
def percentage(word, text):
    return 100 * text.count(word) / len(text)

def lists_1():
    sent1 = ['Call', 'me', 'Ishmael', '.']
    print sent1
    print len(sent1)
    print lexical_diversity(sent1)
