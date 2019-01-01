from random import randint


class Experimentation:

    def __init__(self, frontLetters, endLetters, words, numberOfWords):
        self.frontLetters = frontLetters
        self.endLetters = endLetters
        self.words = words
        self.numberOfWords = numberOfWords
        self.search()

    def search(self):
        """
        k is the frontier index of the sequence

        :return:
        """
        self.sequenceIndexes = []
        self.sequence = []
        x = randint(0, self.numberOfWords - 1)
        self.sequenceIndexes.append(x)
        self.sequence.append(self.words[x])
        self.endOfSequence = False
        self.k = 0
        self.i = 0
        for y in range(3):

            self.appendLetters()
            #print(k)

            #endOfSequence = True

        print(self.sequence, "\n", len(self.sequence))


    def appendLetters(self):
        """

        :return:
        """
        # Set the key to the letters of the word at the end of the sequence
        currentLetters = self.sequence[self.k][-3:-1]
        print(self.frontLetters[currentLetters])
        # Check if the the word is not already within the sequence and that there still exists a word
        if len(self.frontLetters[currentLetters]) != 0 and self.frontLetters[currentLetters][self.i] not in self.sequenceIndexes:
            # append the word with matching letters
            self.sequence.append(self.words[self.frontLetters[currentLetters][self.i]])
            self.sequenceIndexes.append(self.frontLetters[currentLetters][self.i])
            print(self.sequence)

            if self.sequence[self.k+1][-3:-1] == currentLetters:
                self.i += 1
            else:
                self.i = 0
            self.k += 1


            #del self.frontLetters[currentLetters][0]

            #del self.endLetters[self.frontLetters[currentLetters][0]]
            #return self.sequence
        else:
            if self.sequence[self.k][-3:-1] == currentLetters:
                self.i += 1
            else:
                self.i = 0
            print("No match found for last word in sequence")
            delWord = self.sequence.pop()
            delWord = delWord[1:3]
            delIndex = self.sequenceIndexes.pop()
            element = self.frontLetters[delWord].index(delIndex)
            del self.frontLetters[delWord][element]
            if len(self.sequence) > 1:
                self.k -= 1
            print(self.sequence)
            #self.endOfSequence = True
            #return -1
        '''else:
            # iterate through all of the words with matching letters starting from the second and check if
            for i in range(1, len(self.frontLetter[currentLetters])):
                if self.frontLetters[currentLetters] not in sequenceIndexes:
                    sequence.append(self.allWords[self.frontLetters[currentLetters][i]])
                    break'''


