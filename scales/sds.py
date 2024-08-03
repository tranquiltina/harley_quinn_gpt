rule_prompt = """For each item below, please answer the quesion by giving a number from 1-4 which best describes how often you felt or behaved this way during the past several days:
1 indicates "a little of the time",
2 indicates "some of the time",
3 indicates "good part of the time",
4 indicates "most of the time".
"""

question_prompt = [
"I feel down-hearted and blue.",
"Morning is when I feel the best.",
"I have crying spells or feel like it.",
"I have trouble sleeping at night.",
"I eat as much as I used to.",
"I still enjoy sex.",
"I notice that I am losing weight.",
"I have trouble with constipation.",
"My heart beats faster than usual.",
"I get tired for no reason.",
"My mind is as clear as it used to be.",
"I find it easy to do the things I used to.",
"I am restless and can't keep still.",
"I feel hopeful about the future.",
"I am more irritable than usual.",
"I find it easy to make decisions.",
"I feel that I am useful and needed.",
"My life is pretty full.",
"I feel that others would be better off if I were dead.",
"I still enjoy the things I used to do."
]

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

def interpret_sum(x):
    if(x < 25):
        return "ERR"
    elif(x <= 49):
        return "Normal Range"
    elif(x <= 59):
        return "Mildly Depressed"
    elif(x <= 69):
        return "Moderately Depressed"
    else:
        return "Severely Depressed"
    
__all__ = ['question_prompt', 'rule_prompt', 'column_names']