rule_prompt = """
You now play a respondent who is participating in a survey. Please answer the question by giving a number from 0-3 which best describes over the last 2 weeks, how often have you been bothered by any of the following problems?
0 indicates "not at all",
1 indicates "several days",
2 indicates "more than half the days",
3 indicates "nearly every day".
You should only give the score with no reasons.
"""

valid_ans = ['0', '1', '2', '3']

question_prompt = [ 
    "Little interest or pleasure in doing things",
    "Feeling down, depressed, or hopeless",
    "Trouble falling or staying asleep, or sleeping too much",
    "Feeling tired or having little energy",
    "Poor appetite or overeating",
    "Feeling down about yourself or thinking that you haven't met your own or your family's expectations",
    "Trouble concentrating on things, such as reading the newspaper or watching television",
    "Moving or speaking so slowly that other people could have noticed. Or the opposite - being so figety or restless that you have been moving around a lot more than usual",
    "Thoughts about feeling overwhelmed to the point of not wanting to continue working",
    "How difficult have depression problems made it for you to do your work, take care of things at home, or get along with other people?"
]
    # 9. "Thoughts that you would be better off dead, or of hurting yourself",
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