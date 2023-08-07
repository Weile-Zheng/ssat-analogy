import httpx
from parsel import Selector


class Scraper:
    '''
    Variables:
    header: Type Dict - Request Header Configuration
    urls: Type List - List of URLs to scrape
    questionSelector, choiceSelector, answerSelector: Type String - CSS selector
    questions - List of tuple containing different parts of a full question


    '''

    def __init__(self, header, urls, questionSelector, choiceSelector, answerSelector) -> None:
        self.header = header
        self.urls = urls
        self.questionSelector = questionSelector
        self.choiceSelector = choiceSelector
        self.answerSelector = answerSelector
        self.session = httpx.Client(headers=header)

    def scrape(self) -> None:
        '''
        Scrape and save list as an instance variable
        Three item tuple with raw html information of question prompt, choices, and, answers
        '''
        question = []
        choice = []
        answer = []
        for url in self.urls:
            response = self.session.get(url)
            html = response.text
            tree = Selector(html)
            question.extend(tree.css(self.questionSelector).getall())
            choice.extend(tree.css(self.choiceSelector).getall())
            answer.extend(tree.css(self.answerSelector).getall())

        full_questions = list(zip(question, choice, answer))
        # for i, j, k in full_questions:
        #     print(i)
        #     print(j)
        #     print(k)

        print("Scraping Complete")
        print("Total Questions Scraped: " + str(len(full_questions)))
        self.questions = full_questions

 # def getHTML(self) -> str:
    #     html = []
    #     for url in self.urls:
    #         response = self.session.get(url)
    #         html.append(response.text)
    #     return html.join()

    # def getResponseHeader(self) -> str:
    #     responseHeader = []
    #     for url in self.urls:
    #         response = self.session.get(url)
    #         responseHeader.append(response.text)
    #    return responseHeader.join()
