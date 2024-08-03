# harley_quinn_gpt

Codes for ChatGPT: Will It Become Harley Quinn? Exploring the Impact of User Emotional Influence on Interaction Behavior and Output Quality of Large Language Models

## Installation

### Add OpenAI API key to environment variable

If you are using MacOS, in terminal, type:

```bash
vim ~/.zshrc
```

The type `G` (must be capitalized), this will go to the end of your shell config file.

Then press `i`, this will enter the "Insert" mode of Vim editor. 

Then, add 

```
export OPENAI_API_KEY="你的实际API密钥"
```

After that, press `esc`, this exits the "Insert" mode.

Finally, press `shift` + `:`, then type `x`, then press `enter`, this saves your changes and close the config file.

Then, type 

```bash
source ~/.zshrc
```

in your terminal, this refreshes the config file, now you are able to run the `main.py` to start experiments.

### Project Structure

The `personality` folder contains codes for generating the personality of LLM agents. 

The core function of each file is the `gen_personality()` function, it retains the personality prompt `prompt` and relevant debugging info `debug_personality`

The `scales` folder contains codes for generating the questionaire, each scale has `rule_prompt`, which gives the guidance for LLMs to complete the questionaire, `question_prompt`, which are the texts of the questions.

The `results` folder contains results, in `csv` format, of experiments. Each experiment generates $3$ files:

`baseline` contains the original answer of LLM to each of the question in scales with no interference
`personality` contains the personality information of the LLM that answers the scale.

## Scales Used

### Beck's Depression Inventory (BDI)

[questionaire](scales/bdi.txt)

[source](https://www.ismanet.org/doctoryourspirit/pdfs/Beck-Depression-Inventory-BDI.pdf)

Add up the score for each of the twenty-one questions by counting the number to the right of each question you marked.

- $1-10$: These ups and downs are considered normal

- $11-16$: Mild mood disturbance

- $17-20$: Borderline clinical depression

- $21-30$: Moderate depression

- $31-40$: Severe depression

- over $40$: Extreme depression 

## Hamilton Depression Rating Scale (HAM-D)

Not yet added cuz it needs to be completed after a structured interview

### Zung Self-Rating Depression Scale (SDS)

[questionaire](scales/sds.txt)

[source](https://integrationacademy.ahrq.gov/sites/default/files/2020-07/Zung_Self_Rating_Depression_Scale.pdf)

The Zung Self-Rating Depression Scale was designed by W.W. Zung to assess the level of depression for patients diagnosed with depressive disorder.

The Zung Self-Rating Depression Scale is a short self-administered survey to quantify the depressed status of a patient. There are $20$ items on the scale that rate the four common characteristics of
depression: the pervasive effect, the physiological equivalents, other disturbances, and psychomotor activities.

There are ten positively worded and ten negatively worded questions. Each question is scored on a scale of $1-4$ (a little of the time, some of the time, good part of the time, most of the time).

The scores range from $25-100$.

- $25-49$: Normal Range
- $50-59$: Mildly Depressed
- $60-69$: Moderately Depressed
- $70$ and above: Severely Depressed

Zung, WW (1965) A self-rating depression scale. Arch Gen Psychiatry 12, 63-70. 

### Patient Health Questionnaire-9 (PHQ-9)

[questionaire](scales/phq_9.txt)

[source](https://www.ismanet.org/doctoryourspirit/pdfs/Beck-Depression-Inventory-BDI.pdf)

For initial diagnosis:
1. Patient completes PHQ-9 Quick Depression Assessment.
2. If there are at least 4 3s in the shaded section (including Questions #1 and #2), consider a depressive
disorder. Add score to determine severity.
Consider Major Depressive Disorder
- if there are at least 5 3s in the shaded section (one of which corresponds to Question #1 or #2)
Consider Other Depressive Disorder
- if there are 2-4 3s in the shaded section (one of which corresponds to Question #1 or #2)
Note: Since the questionnaire relies on patient self-report, all responses should be verified by the clinician,
and a definitive diagnosis is made on clinical grounds taking into account how well the patient understood
the questionnaire, as well as other relevant information from the patient.
Diagnoses of Major Depressive Disorder or Other Depressive Disorder also require impairment of social,
occupational, or other important areas of functioning (Question #10) and ruling out normal bereavement, a
history of a Manic Episode (Bipolar Disorder), and a physical disorder, medication, or other drug as the
biological cause of the depressive symptoms.
To monitor severity over time for newly diagnosed patients or patients in current treatment for
depression:
1. Patients may complete questionnaires at baseline and at regular intervals (eg, every 2 weeks) at
home and bring them in at their next appointment for scoring or they may complete the
questionnaire during each scheduled appointment.
2. Several days = 1 More than half the days = 2 Nearly every day = 3
3. Add together column scores to get a TOTAL score.
4. Refer to the accompanying PHQ-9 Scoring Box to interpret the TOTAL score.
5. Results may be included in patient files to assist you in setting up a treatment goal, determining degree of
response, as well as guiding treatment intervention.
Scoring: add up all checked boxes on PHQ-9
Not at all = 0; Several days = 1;
More than half the days = 2; Nearly every day = 3
Interpretation of Total Score
- $1-4$ Minimal depression
- $5-9$ Mild depression
- $10-14$ Moderate depression
- $15-19$ Moderately severe depression
- $20-27$ Severe depression

### Hospital Anxiety and Depression Scale (HADS)