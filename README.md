# SSAT Analogy Solver
[Background info](https://github.com/Weile-Zheng/word2vec-vector-embedding)
- Load vector embeddings from GloVe
- Solver
- Testing on real questions
- Web scrapping for gathering mass data on questions and answers

Data Collecting:
- Web scraping 

Data Processing:
- Putting the questions scrapped from data to ssatQuestion class. 
- Putting the records into CSV File

Data Cleaning:
- Remove all incomplete questions: missing one of the three: Question Prompt, Answer Choice, Correct Choice

Data Analysis:
- Feeding the questions into solver using GloVe vector embedding and Gensim library functions, test
the accuracy in regard to 1. Training data size, 2. Vector dimension embedded.

[Here](https://github.com/Weile-Zheng/word2vec-vector-embedding) for training your own embedding using word2vec and explaining underlying reasoning for analogies in vector semantic.
