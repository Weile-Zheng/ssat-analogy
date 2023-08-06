from bs4 import BeautifulSoup


class typeA:
    '''
    A Type Question: 
    Structure:
    A is to B as C is to
    ......

    Param:
    question, three item tuple containing html for question prompt, answer choices, and answer

    '''

    def __init__(self, question) -> None:
        self.question = question
        self.list = self.parseQuestion(question)

    def parseQuestion(self, question) -> list:
        '''
        Parsing a question from HTML format

        Param: the question tuple of three items

        Return: a list of 9 strings 

        [Queston] [Question] [Question] [Choices] [Choices] [Choices] [Choices] [Choice] [Answer]
        '''
        string = "".join(question)
        soup = BeautifulSoup(string, 'html.parser')
        p_tag_text = soup.find_all('p')
        for tag in p_tag_text:
            print(tag.get_text(strip=True))
        return 1

    def printQuestion() -> str:
        pass
