from html.parser import HTMLParser
import urllib.parse, json, requests, random, time, html

# hopefully fixing character encoding problems wwith questions and answers
# edit: It does :D Finally
h = html.unescape
# defining game options, like the number of questions and what type of questions they will be
num_of_ques=1
category=15
base_url = f'https://opentdb.com/api.php?amount={num_of_ques}&category={category}'
url = requests.get(base_url)
data = url.content
# data below contains entire json formatted trivia question

# define number of players in function

# start game using data and player count
def game_play(data, players=1, points=0, total_rounds=5):
    current_round = 1 
    while current_round <= total_rounds:
        url = requests.get(base_url)
        data = url.json()
        question_info_list = data['results']
        question_info = question_info_list[0]
        question_d = question_info['difficulty']
        question_t = question_info['type']
        question = h(question_info['question'])
        answers = list(question_info['incorrect_answers'])
        correct_ans = (question_info['correct_answer'])
        answers.append(correct_ans)
        answer_choices = h(random.sample(answers, k=len(answers)))
        print(f'Question number {current_round} is a {question_d} {question_t} choice question:')
        # small wait to give people time to read the question info above
        time.sleep(3)
        print(question)
        # another small wait here, quicker if the question is True or False
        if len(answer_choices) == 2:
            time.sleep(3)
            print(answer_choices)
        else:
            time.sleep(5)
            print(answer_choices)
            time.sleep(5)
        current_round += 1
        continue
    

        #evaluate answer and award points


# call game function to start the round
game_play(data)


### TODO
# give the ability to define player entries (ie a join command)
# evaluate answer to determine if answer was correct or not
# stop waiting once all players have answered
# determine who answered correctly first
# points system for correct answers, more points for answering quicker
# test ability to pass through multiple questions
# determine winner after all questions are completed
# give ability to randomize category, or choose categories to add to list to bounce in between
