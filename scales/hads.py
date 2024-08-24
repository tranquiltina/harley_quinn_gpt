rule_prompt = """You now play a respondent who is participating in a survey.
Please answer the following questions about how you are feeling currently.
Choose one response from the four given for each question by giving a number from 0-3.
You should only give the score with no reasons.
"""

valid_ans = {'1', '2', '3', '0'}

question_prompt = [
"I still enjoy the things I used to enjoy: 0 indicates Definitely as much. 1 indicates Not quite so much. 2 indicates Only a little. 3 indicates Hardly at all.",
"I can laugh and see the funny side of things: 0 indicates As much as I always could. 1 indicates Not quite so much now. 2 indicates Definitely not so much now. 3 indicates Not at all.",
"I feel cheerful: 0 indicates Most of the time. 1 indicates Sometimes. 2 indicates Not often. 3 indicates Not at all.",
"I feel as if I am slowed down: 0 indicates Not at all. 1 indicates Sometimes. 2 indicates Very often. 3 indicates Nearly all the time.",
"I have lost interest in my appearance: 0 indicates I take just as much care as ever. 1 indicates I may not take quite as much care. 2 indicates I don't take as much care as I should. 3 indicates Definitely.",
"I look forward with enjoyment to things: 0 indicates As much as I ever did. 1 indicates Rather less than I used to. 2 indicates Definitely less than I used to. 3 indicates Hardly at all.",
"I can enjoy a good book or radio or TV program: 0 indicates Often. 1 indicates Sometimes. 2 indicates Not often.3 indicates Very seldom."
]

column_names = ['1', '2', '3', '4', '5', '6', '7']

__all__ = ['question_prompt', 'rule_prompt', 'column_names']

def interpret_sum(x):
    if(x < 0):
        return "ERR"
    elif(x <= 7):
        return "Normal"
    elif(x <= 10):
        return "Borderline abnormal"
    else:
        return "Abnormal"