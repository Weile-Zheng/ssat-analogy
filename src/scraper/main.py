from Scraper import Scraper


def main():
    headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    urls = [
        "https://www.varsitytutors.com/ssat_upper_level_verbal-help/analogies"
    ]

    for i in range(2, 11):
        urls.append(
            f"https://www.varsitytutors.com/ssat_upper_level_verbal-help/analogies?page={i}")

    question = '.med_question:not(:contains("Complete this analogy"))'
    choice = '.possible_answers'
    answer = '.question_correct'
    scraper = Scraper(headers, urls, question, choice, answer)
    scraper.scrape()


if __name__ == '__main__':
    main()
