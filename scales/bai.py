ule_prompt = """You now play a respondent who is participating in a survey.
Below is a list of common symptoms of anxiety. Please carefully read each item in the list. Indicate how much you have been
bothered by that symptom during the past month, including today by giving a number from 0-3:
0 indicates "Not at all",
1 indicates "Mildly, but it didn't bother me much",
2 indicates "Moderately, it wasn't pleasant at times",
3 indicates "Severely, it bothered me a lot". 
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21']

question_prompt = [
    "Numbness or tingling",
    "Feeling hot",
    "Wobbliness in legs",
    "Unable to relax",
    "Fear of worst happening",
    "Dizzy or lightheaded",
    "Heart pounding / racing",
    "Unsteady",
    "Terrified or afraid",
    "Nervous",
    "Feeling of choking",
    "Hands trembling",
    "Shaky / unsteady",
    "Fear of losing control",
    "Difficulty in breathing",
    "Fear of dying",
    "Scared",
    "Indigestion",
    "Faint / lightheaded",
    "Face flushed",
    "Hot / cold sweats",
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
    elif(x <= 21):
        return "Low Anxiety"
    elif(x <= 35):
        return "Moderate Anxiety"
    else:
        return "Severe Anxiety"