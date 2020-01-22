from random import randint



class DepthFirstSearch:

    def __init__(self, words, wordCount):
        self.words = words
        self.wordCount = wordCount



    def depthFirstSearch(self, words, wordCount):

        finalSolution = {}
        # Repeat the algorithm an arbitrary number of times to find the best solution
        for x in range(50):

            # Random integer to select starting word
            i = randint(0, wordCount)
            # Initialise solution
            solution = dict()
            solution[0] = words[i - 1]

            # Initialise other variables
            k = 1
            endOfSequence = False
            # Continue to search for words until the end of the list is reached or no matches are found
            while not endOfSequence:

                # Search through each word in the list to see if it matches the last word in the sequence
                for j in range(wordCount):

                    currentWord = solution.get(k-1)

                    # Check if the word matches the last word in the sequence and if it already exits in the sequence
                    if currentWord[-3:-1] == words[j][1:3] and words[j] not in solution.values():
                        solution[k] = words[j]
                        k += 1
                        break
                    elif j == wordCount - 1:
                        k = 500
                # Terminating Condition
                if k == 500:
                    # If the solution is the longest sequence found thus far, store it.
                    if len(solution) > len(finalSolution):
                        finalSolution = solution.copy()
                        print('\r', "Solution Length:", len(solution), end='', flush=True)
                    endOfSequence = True
        print("\nStarting Word: ", finalSolution[0])

        print(finalSolution)
        return len(finalSolution)

    def run(self):
        return self.depthFirstSearch(self.words, self.wordCount)
