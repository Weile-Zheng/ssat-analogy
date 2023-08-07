from bs4 import BeautifulSoup


class typeA:
    '''
    A Type Question:
    Structure:
    A is to B as C is to
    ......

    Param:
    question, three item tuple containing html for question prompt, answer choices, and answer
    dataList: [Queston] [Question] [Question] [Choices] [
        Choices] [Choices] [Choices] [Choice] [Answer]
    '''

    def __init__(self, question) -> None:
        self.question = question
        self.dataList = self.parseQuestion(question)

    def parseQuestion(self, question) -> list:
        '''
        Parsing a question from HTML format

        Param: the question tuple of three items

        Return a list in dataList format
        '''
        string = "".join(question)
        soup = BeautifulSoup(string, 'html.parser')
        p_tag_text = soup.find_all('p')
        list = [tag.get_text(strip=True) for tag in p_tag_text]
        firstString = list.pop(0)
        firstString = firstString.replace("\xa0", "").replace(" as ", ";").replace(" ", "").replace(
            "_", "").replace("isto", ";").replace(".", "")
        keywords = firstString.split(";")
        filtered = [item for item in keywords if item != ""]
        if (len(filtered) < 3):
            return
        for i in range(3):
            list.insert(i, filtered[i])

        return list



