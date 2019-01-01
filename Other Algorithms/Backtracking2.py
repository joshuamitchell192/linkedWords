from random import randint

class Backtracking:

    def __init__(self, words, wordCount):
        self.words = words
        self.wordCount = wordCount
        self.backtrack(self.words, self.wordCount)

    def backtrack(self, words, wordCount):

        bestSequence = {}
        sequence = {}
        sequenceIndex = {}
        k = 0
        x = randint(0, wordCount)

        sequence[k] = words[x]
        sequenceIndex[k] = x

        for i in range(sequenceIndex[k], wordCount):



            if sequence[k][-3:-1] == words[i][1:3]:
                print(1)