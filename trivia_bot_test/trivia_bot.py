import urllib.parse
import json, requests, random, time

# defining game options, like the number of questions and what type of questions they will be
num_of_ques = 1 
category = 15
base_url = f'https://opentdb.com/api.php?amount={num_of_ques}&category={category}'
url = requests.get(base_url)
# data below contains entire json formatted trivia game
data = url.json()
question_info_list = data['results']

# define number of players in function



# start game using data and player count
def game_play(data, players=1, points=0):
    for question_info in question_info_list:
        question_info = question_info_list[0]
        question_num = 1 
        question_d = question_info['difficulty']
        question_t = question_info['type']
        question = question_info['question']
        ques = question.encode()
        answers = list(question_info['incorrect_answers'])
        correct_ans = (question_info['correct_answer'])
        answers.append(correct_ans)
        answer_choices = random.sample(answers, k=len(answers))
    print(f'Question number {question_num} is a {question_d} {question_t} choice question:')
    # small wait to give people time to read the question info above
    time.sleep(5)
    print(str(ques))
    # another small wait here, quicker if the question is True or False
    if len(answer_choices) == 2:
        time.sleep(3)
        print(answer_choices)
    else:
        time.sleep(5)
        print(answer_choices)

        #evaluate answer and award points


# call game function to start the round
game_play(data)


### TODO
# fix character encoding in question/answer strings
# give the ability to define player entries (ie a join command)
# evaluate answer to determine if answer was correct or not
# determine who answered correctly first
# points system for correct answers, more points for answering quicker
# test ability to pass through multiple questions
# determine winner after all questions are completed
