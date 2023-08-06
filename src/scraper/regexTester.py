from bs4 import BeautifulSoup

html = """<div class="med_question">
            <p>Atom is to molecule as minute is to <span style="text-decoration:underline;">__________</span>.</p>
          </div>
<div class="possible_answers">
                <div class="concept_answer">
                  <p>stopwatch</p>
                </div>
                <div class="concept_answer">
                  <p>clock</p>
                </div>
                <div class="concept_answer">
                  <p>century</p>
                </div>
                <div class="concept_answer">
                  <p>tiny</p>
                </div>
                <div class="concept_answer">
                  <p>hour</p>
                </div>
            </div>
<div class="question_correct">
              <strong>Correct answer:</strong> <p>hour</p>
            </div>"""

soup = BeautifulSoup(html, 'html.parser')
p_tag_text = soup.find_all('p')
for tag in p_tag_text:
    print(tag.get_text(strip=True))
