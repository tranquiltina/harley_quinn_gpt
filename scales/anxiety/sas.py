rule_prompt = """You now play a respondent who is participating in a survey. Please answer the question by giving a number from 1-4 which best describes how often you felt or behaved this way during the past several days:
1 indicates "a little of the time",
2 indicates "some of the time",
3 indicates "good part of the time",
4 indicates "most of the time".
You should only give the score with no reasons.
"""

valid_ans = ['1', '2', '3', '4']
question_prompt = [
    "I feel more nervous and anxious than usual.",
    "I feel afraid for no reason at all.",
    "I get upset easily or feel panicky.",
    "I feel like I'm falling apart and going to pieces.",
    "I feel that everything is all right and nothing bad will happen.",
    "My limbs tremble and shake.",
    "I am bothered by headaches neck and back pain.",
    "I feel weak and get tired easily.",
    "I feel calm and can sit still easily.",
    "I can feel my heart beating fast.",
    "I am bothered by dizzy spells.",
    "I have fainting spells or feel like it.",
    "I can inhale and exhale easily.",
    "I get numbness and tingling in my fingers and toes.",
    "I am bothered by stomach aches or indigestion.",
    "I have to empty my bladder often.",
    "My hands are usually dry and warm.",
    "My face gets hot and blushes.",
    "I fall asleep easily and get a good night's rest.",
    "I experience terrible dreams."
]

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20']

def interpret_sum(x):
    if(x < 20):
        return "ERR"
    elif(x <= 44):
        return "Normal Range"
    elif(x <= 59):
        return "Mild to Moderate Anxiety Levels"
    elif(x <= 74):
        return "Marked to Severe Anxiety Levels"
    else:
        return "Extreme Anxiety Levels"
    
__all__ = ['question_prompt', 'rule_prompt', 'column_names']
