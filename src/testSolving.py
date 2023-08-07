from solver.Solver import ssatTester
from scraper.Scraper import Scraper
from scraper.Question import typeA


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    urls = [
        "https://www.varsitytutors.com/ssat_upper_level_verbal-help/analogies"
    ]

    # for i in range(2, 11):
    #     urls.append(
    #         f"https://www.varsitytutors.com/ssat_upper_level_verbal-help/analogies?page={i}")

    # Scraping base on the urls and css selector provided
    question = '.med_question:contains("_")'
    choice = '.possible_answers'
    answer = '.question_correct'
    scraper = Scraper(headers, urls, question, choice, answer)
    scraper.scrape()
    questionList = scraper.questions
    typeAList = []

    # For each question in the scraped question list, convert it to of typeA, a class for better processing questions
    # TypeA list is a list of typeA, which holds a list,
    for question in questionList:
        x = typeA(question)
        typeAList.append(x.dataList)

    count = 0
    for x in typeAList:
        if x != None:
            count += 1
            print(str(count) + ": " + str(x))
    print("Valid question data: " + str(count))

    converted_file = '/Users/weilezheng/CompSci/ML/solver_ssat/src/glove.6B.100d.word2vec.txt"'
    solver = ssatTester(typeAList, converted_file)
    solver.runTest()


if __name__ == '__main__':
    main()
