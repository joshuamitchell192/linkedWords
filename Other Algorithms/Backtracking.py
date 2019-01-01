from random import randint
class Backtracking:

    def __init__(self, words, wordCount):
        self.words = words
        self.wordCount = wordCount
        self.backtrack(self.words, self.wordCount)
        
    def backtrack(self, words, wordCount):
        finalSolution = {}
        i = randint(0, wordCount)
        solution = {}
        solution[0] = words[i]
        deletedWord = ""
        k = 1
        sequenceIndex = []
        sequenceIndex.append(i)
        endOfSequence = False
        while not endOfSequence:
            for j in range(sequenceIndex[k-1], wordCount):
                currentWord = solution.get(k-1)
                #print(currentWord)
                if currentWord[-3:-1] == words[j][1:3] and words[j] not in solution.values() and words[j] != deletedWord:
                    solution[k] = words[j]
                    print(solution)
                    sequenceIndex.append(j)

                    k += 1
                    break

                elif j == wordCount - 1:

                    deletedWord = solution[k-1]
                    del solution[k-1]
                    k -= 1
                    del sequenceIndex[-1]
                    #j = sequenceIndex[-1] + 1
                    print(solution)

                if k == 3500:
                    if len(solution) > len(finalSolution):
                        finalSolution = solution.copy()
                        print('\r', "Solution Length:", len(solution), end='', flush=True)
                    endOfSequence = True

        print(finalSolution)
        return finalSolution