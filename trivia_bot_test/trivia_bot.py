import urllib.parse
import json, requests, random, time

#def build_questions(num_of_ques=15, category=15):
    # builds a list of questions

#decodes question and answer
num_of_ques = 1 
category = 15
base_url = f'https://opentdb.com/api.php?amount={num_of_ques}&category={category}'
url = requests.get(base_url)
data = url.json()
question_info_list = data['results']

def game_play(data, players=1, points=0):
    for question_info in question_info_list:
        question_info = question_info_list[0]
        question_num = 1 
        #starts with question_info = question_info_list[0]
        question_d = question_info['difficulty']
        question_t = question_info['type']
        question = question_info['question']
        ques = question.encode()
        answers = list(question_info['incorrect_answers'])
        correct_ans = (question_info['correct_answer'])
        answers.append(correct_ans)
        answer_choices = random.sample(answers, k=len(answers))
        print(f'Question number {question_num} is a {question_d} {question_t} choice question:')
        time.sleep(5)
        print(str(ques))
        #for i in range(len(answer_choices)):
        if len(answer_choices) == 2:
            time.sleep(3)
            print(answer_choices)
        else:
            time.sleep(5)
            print(answer_choices)

        # evaluate answer

    #for answer in answer_choices:
    #    if len(answer) == 2:
    #        print(answer)
    #    else:


#question_info = question_info_list[0]
#question = str(question_info['question'])
#question = question_list[0][4]
#correct_answer = question_list[0][5]
#answers = question_list[0][5] + question_list[0][6]
#answer_choices = random.sample(answers)

game_play(data)

#print(question)
#print(category)

#print(f'Trivia Questions loaded! The category is {data["category"]}!')
#for i in num_of_ques:



    
    
