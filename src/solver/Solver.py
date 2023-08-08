from operator import contains
from gensim.test.utils import datapath, get_tmpfile
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec
from numpy import dot
from numpy.linalg import norm


class ssatTester:

    '''
    Param:
    A list of questions, each question is a list of 9 words.
    A vector embedding.
    '''

    def __init__(self, questionList, embedding):
        self.questionList = questionList
        self.model = KeyedVectors.load_word2vec_format(embedding)

    def runTest(self):
        totalquestion = 0
        questionCorrect = 0
        for question in self.questionList:
            questionVector = []
            skip = False
            try:
                for word in question:
                    if contains_space(word):
                        word = "Placeholder"

                    word = word.lower()
                    try:
                        vector = self.model[word]
                        questionVector.append(vector)
                    except KeyError:
                        skip = True
                        break
            except TypeError:
                continue

            if skip == True:
                continue

            # Word A,B are first analogy, word C are one of the word for the answer analogy.
            wordA = questionVector[0]
            wordB = questionVector[1]
            wordC = questionVector[2]
            # Difference vector is the vector we are trying to match.
            differenceVector = wordA-wordB

            # Find all difference vector between word C, and 3,4,5,6,7 (The answer choices)
            differenceVectorChoices = []
            for i in range(3, 8):
                differenceVectorChoices.append(wordC-questionVector[i])

            # Find the similarity between differnceVectorChoices to our differenceVector
            choiceScores = []
            for i in differenceVectorChoices:
                # cos_sim = dot(differenceVector, i) / \
                # (norm(differenceVector)*norm(i))
                euclidean_similarity = 1 / (1 + norm(differenceVector - i))
                choiceScores.append(euclidean_similarity)

            # Find the highest score, and the its index.
            max = -1
            maxIndex = -1
            for i in range(5):
                if choiceScores[i] > max:
                    max = choiceScores[i]
                    maxIndex = i

            """
            Note that maxIndex is the highest score in choiceScores, which match to one of the five choices
            from word 3 to 7 inclusive, add 3 to max index to skip the first three words of the wordlist,
            which are wordA, wordB, and wordC for our question prompt. 
            """
            ourResultAnswer = question[maxIndex+3]
            print("The highest difference vector similarity score is: " + str(max))
            print("Which coorespond to answer choice: " + ourResultAnswer)
            print(f'The right answer is {question[-1]}')
            totalquestion += 1
            if (ourResultAnswer == question[-1]):
                questionCorrect += 1
                print("Our solver correctly solved the problem")
            else:
                print("Our solver incorrectly solved the problem")
        print("Total Question Processed: " + str(totalquestion))
        print("Question Correct: " + str(questionCorrect))
        print("Percentage: " + str(questionCorrect/totalquestion))


def contains_space(word):
    return ' ' in word
