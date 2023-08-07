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
        for question in list:
            for i in range(9):
                



#cos_sim = dot(a, b)/(norm(a)*norm(b))
