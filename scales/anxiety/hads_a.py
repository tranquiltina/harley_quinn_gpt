rule_prompt = """You now play a respondent who is participating in a survey.
Please answer the following questions about how you are feeling currently.
Choose one response from the four given for each question by giving a number from 0-3.
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

column_names = ['1', '2', '3', '4', '5', '6', '7']

question_prompt = [
    "I feel tense or 'wound up': 3 indicates Most of the time 2 indicates A lot of the time 1 indicates From time to time, occasionally 0 indicates Not at all",
    "I get a sort of frightened feeling as if something awful is about to happen: 3 indicates Very definitely and quite badly 2 indicates Yes, but not too badly 1 indicates A little, but it doesn't worry me 0 indicates Not at all",
    "Worrying thoughts go through my mind: 3 indicates A great deal of the time 2 indicates A lot of the time 1 indicates From time to time, but not too often 0 indicates Only occasionally",
    "I can sit at ease and feel relaxed: 0 indicates Definitely 1 indicates Usually 2 indicates Not Often 3 indicates Not at all",
    "I get a sort of frightened feeling like 'butterflies' in the stomach: 0 indicates Not at all 1 indicates Occasionally 2 indicates Quite Often 3 indicates Very Often",
    "I feel restless as I have to be on the move: 3 Very much indeed 2 Quite a lot 1 Not very much 0 Not at all",
    "I get sudden feelings of panic: 3 indicates Very often indeed 2 indicates Quite often 1 indicates Not very often 0 indicates Not at all"
]

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