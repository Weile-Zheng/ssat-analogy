import httpx
from parsel import Selector


class Scraper:
    '''
    Parameters:
    header: Type Dict - Request Header Configuration
    urls: Type List - List of URLs to scrape
    questionSelector, choiceSelector, answerSelector: Type String - CSS selector
    '''

    def __init__(self, header, urls, questionSelector, choiceSelector, answerSelector) -> None:
        self.header = header
        self.urls = urls
        self.questionSelector = questionSelector
        self.choiceSelector = choiceSelector
        self.answerSelector = answerSelector
        self.session = httpx.Client(headers=header)

    def scrape(self) -> None:
        allHTML = []
        for url in self.urls:
            print(url)
            response = self.session.get(url)
            allHTML.append(response.text)
        html = "".join(allHTML)
        with open("output.txt", "w") as file:
            file.write(html)
        assert (False)
        print("Data written to the file successfully.")
        tree = Selector(html)
        question = tree.css(self.questionSelector).getall()
        choice = tree.css(self.choiceSelector).getall()
        answer = tree.css(self.answerSelector).getall()
        print("Scraping Complete")

        full_questions = zip(question, choice, answer)
        for i, j, k in full_questions:
            print(i)
            print(j)
            print(k)

        print("Scraping Complete")
        #print("Total Questions Scraped: " + str(len(full_questions)))
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
