from S5055278_DepthFirstSearch import DepthFirstSearch
from S5055278_Experimentation2 import Backtracking

from collections import defaultdict
import time
from random import randint
import matplotlib.pyplot as plt
import sys

"""
Extract words from the dictionary of the given length.
Then find sequences of linked words
Store the process time and the sequence length
Find the longest sequence for each word length

"""
"""
Algorithms:
    Backtracking
    Depth first search
    
"""

file = open("dictionary.txt")
allWords = file.read().splitlines()

numberOfWords = len(allWords)   
def extractLetters(i):
    words = []
    frontLetters = defaultdict(list)
    endLetters = defaultdict(list)
    k = 0
    for j in range(numberOfWords - 1):
        if len(allWords[j]) == i:
            frontLetters[allWords[j][1:3]].append(k)
            endLetters[allWords[j][-3:-1]].append(k)
            words.append(allWords[j])
            k += 1
    return frontLetters, endLetters, words

# Order the list of words in terms of the number of

def main():
    # grab word length
    i = int(sys.argv[1][0])
    # start timer
    start = time.time()
    # Get relevant words
    frontLetters, endLetters, words = extractLetters(i)
    wordCount = len(words)
    #DFS = DepthFirstSearch(words, wordCount)
    #solution = DFS.run()
    BT = Backtracking(frontLetters, endLetters, words, wordCount)
    solution = BT.search()
    end = time.time()
    print("Time: ", end-start)

main()
file.close()

