# harley_quinn_gpt

Codes for ChatGPT: Will It Become Harley Quinn? Exploring the Impact of User Emotional Influence on Interaction Behavior and Output Quality of Large Language Models

## Installation

### Setting Up OpenAI API Key

1. **Edit Shell Configuration (MacOS)**

   Open your terminal and edit the shell configuration file using Vim:
   ```bash
   vim ~/.zshrc
   ```

2. **Add API Key**

   Inside Vim:
   - Press `i` to enter Insert mode.
   - Scroll to the end and add:
     ```bash
     export OPENAI_API_KEY="your_actual_api_key"
     ```
   - Press `esc` to exit Insert mode.

3. **Save and Exit Vim**

   - Press `Shift` + `:`, type `x`, and press `Enter` to save and exit Vim.

4. **Refresh Shell Configuration**

   ```bash
   source ~/.zshrc
   ```

Now your environment is configured to use the `main.py` script for running experiments.

### Project Structure

- **personality/**: Contains code for generating the personality of LLM agents.
  - **Core Function**: Each file includes the `gen_personality()` function, which retains the personality prompt (`prompt`) and relevant debugging info (`debug_personality`).

- **scales/**: Contains code for generating questionnaires.
  - **Scale Details**: Each scale includes:
    - `rule_prompt`: Guidance for LLMs on completing the questionnaire.
    - `question_prompt`: Text of the questions.
    - Detailed explanations for each scale can be found in the [scale used](#scales-used) section of the README.

- **results/**: Contains experiment results in CSV format.
  - **Experiment Files**: Each experiment generates three files:
    - `baseline.csv`: Original answers of LLMs to each question in scales with no interference.
    - `personality.csv`: Personality information of the LLM that answered the scale.

## Scales Used

### Beck's Depression Inventory (BDI)

[questionnaire](scales/bdi.py)

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

[questionnaire](scales/sds.py)

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

[questionnaire](scales/phq_9.py)

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

[questionnaire](scales/hads.py)

[source](https://bmjopen.bmj.com/content/bmjopen/8/6/e021890/DC2/embed/inline-supplementary-material-2.pdf?download=true)

Only included depression related questions, anxiety related questions are omitted.

Scoring (add the As = Anxiety. Add the Ds = Depression). The norms below will give you an idea of the level of Anxiety and Depression.
0-7 = Normal
8-10 = Borderline abnormal
11-21 = Abnormal