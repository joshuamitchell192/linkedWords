from random import randint
from collections import defaultdict


class Backtracking:

    def __init__(self, frontLetters, endLetters, words, numberOfWords):
        self.frontLetters = frontLetters
        self.endLetters = endLetters
        self.words = words
        self.numberOfWords = numberOfWords

    def search(self):
        """

        :return: The final solution
        """
        # Initialise variables
        sequenceIndex = []
        sequence = []
        self.deletedWords = []
        self.deletedIndex = []
        noBacktracks = 0

        # Random index to select random word from the dictionary
        x = randint(0, self.numberOfWords - 1)

        # Make sure that if the word length equals 4, set the starting word to contain 'ar'
        if len(self.words[x]) == 4:
            for i in range(self.numberOfWords):
                x = randint(0, self.numberOfWords - 1)
                if self.words[x][1:3] == 'ar':
                    break

        # Append the starting word the sequence
        sequenceIndex.append(x)
        sequence.append(self.words[x])

        print("Word Length: ", len(self.words[x]), "\n")

        # Continue to backtrack through the sequence until the threshold is reached
        while noBacktracks <= 4:
            # Set the key to access words in the dictionary that match the last word in the sequence
            currentLetters = sequence[-1][-3:-1]
            # Initialise variables
            bestLength = 0
            bestIndex = 0
            foundWord = False
            # Iterate through each matching word
            for i in range(len(self.frontLetters[currentLetters]) - 1):

                # Get the index of the word in the list
                x = self.frontLetters[currentLetters][i]

                # If the word already exists within the sequence, skip to the next word
                if x in sequenceIndex:
                    continue
                # Get the letters of the word in the list to check it number of neighbours
                xLetters = self.words[x][-3:-1]

                # If the number of the neighbours is more than previously found, store the length and the word's index
                if len(self.frontLetters[xLetters]) > bestLength:
                    bestLength = len(self.frontLetters[xLetters])
                    bestIndex = x
                    foundWord = True

            # Append the matching word with the most number of neighbours to the sequence
            if foundWord == True:
                # Reset backtracks to zero so that the algorithm will continue to backtrack for the new word
                noBacktracks = 0
                sequence.append(self.words[bestIndex])
                sequenceIndex.append(bestIndex)

                print('\r', "Solution Length:", len(sequence), end='', flush=True)

            # foundWord will be False when no matching words are found, in this case backtrack the sequence
            if foundWord == False:
                noBacktracks += 1
                self.backtrack(sequence, sequenceIndex)

        # Check if the solution has duplicates
        if len(sequence) == len(set(sequence)):
            print('\nSolution Valid! :)')
        print("Sequence:\n", sequence)
        return len(sequence)


    def backtrack(self, sequence, sequenceIndex):
        """

        :param sequence:
        :param sequenceIndex:
        :return:
        """
        # Pop the last word from the sequence and sequenceIndex and store so that it can be added back to the dictionary
        self.deletedWords.append(sequence.pop())
        self.deletedIndex.append(sequenceIndex.pop())
        # Get the index of the deleted word in dictionary list so that it can be deleted from the dictionary
        element = self.frontLetters[self.deletedWords[-1][1:3]].index(self.deletedIndex[-1])
        # Delete the word from the dictionary
        del self.frontLetters[self.deletedWords[-1][1:3]][element]
