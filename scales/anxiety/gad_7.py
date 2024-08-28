rule_prompt = """You now play a respondent who is participating in a survey.
Please answer the question by giving a number from 0-3 which best describes over the last 2 weeks, how often have you been bothered by any of the following problems?
0 indicates "not at all",
1 indicates "several days",
2 indicates "more than half the days",
3 indicates "nearly every day". 
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

column_names = ['1', '2', '3', '4', '5', '6', '7']

question_prompt = [
    "Feeling nervous, anxious or on edge",
    "Not being able to stop or control worrying",
    "Worrying too much about different things",
    "Trouble relaxing",
    "Being so restless that it is hard to sit still",
    "Becoming easily annoyed or irritable",
    "Feeling afraid as if something awful might happen"
]

__all__ = ['question_prompt', 'rule_prompt', 'column_names']

def interpret_sum(x):
    if(x < 1):
        return "ERR"
    elif(x <= 4):
        return "Minimal Anxiety"
    elif(x <= 9):
        return "Mild Anxiety"
    elif(x <= 14):
        return "Moderate Anxiety"
    else:
        return "Severe Anxiety"