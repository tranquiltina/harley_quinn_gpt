rule_prompt = """
Over the last 2 weeks, how often have you been bothered by any of the following problems?
0 indicates "not at all",
1 indicates "several days",
2 indicates "more than half the days",
3 indicates "nearly every day".
"""

question_prompt = [ 
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling bad about yourself or that you are a failure or have let yourself or your family down",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so figety or restless that you have been moving around a lot more than usual",
    "Thoughts that you would be better off dead, or of hurting yourself",
]
# 10. If you checked off any problems, how difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?
# Not difficult at all
# Somewhat difficult
# Very difficult
# Extremely difficult'''

column_names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

__all__ = ['question_prompt', 'rule_prompt', 'column_names']

def interpret_sum(x):
    if(x < 1):
        return "ERR"
    elif(x <= 4):
        return "Minimal depression"
    elif(x <= 9):
        return "Mild depression"
    elif(x <= 14):
        return "Moderate depression"
    elif(x <= 19):
        return "Moderately severe depression"
    else:
        return "Severe depression"