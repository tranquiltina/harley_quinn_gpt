from openai import OpenAI
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import json
api_key = os.getenv('ALTERNATE_OPENAI_API_KEY')
client = OpenAI(base_url='https://openkey.cloud/v1',api_key=api_key)

# 从 scales 目录下的 bdi.py 文件导入相关变量和函数
import scales.bdi as bdi
import scales.phq_9 as phq_9
import scales.sds as sds
import scales.hads as hads

scale_used = 'sds'

scale_dict = {
    'sds': sds,
    'phq_9': phq_9,
    'bdi': bdi,
    'hads': hads
}

column_names = scale_dict[scale_used].column_names
question_prompt = scale_dict[scale_used].question_prompt
rule_prompt = scale_dict[scale_used].rule_prompt
valid_ans = scale_dict[scale_used].valid_ans

model_dict = {
    "gpt3.5": "gpt-3.5-turbo-1106", 
    "gpt4": "gpt-4-1106-preview"
}
model_used = 'gpt3.5'

illness_tested = 'depression'

experiment_name = f"{model_used}_{scale_used}"
conversation_pth = f"./data/{model_used}_{illness_tested}.json"
baseline_pth = f"./results/baseline_{experiment_name}.csv"
final_pth = f"./results/final_{experiment_name}.csv"

# 进行几次测试
n_sample = 20

# 使用哪个模型，量表和人格生成规则

# 创建一个名为model_dict的字典，用于存储不同模型的名称和对应的标识符
def GetResponse(prompt, conversation_history, temperature):
    conversation_history.append({'role': 'user', 'content': prompt})
    # 开始一个无限循环，直到遇到break语句
    completion = client.chat.completions.create(model=model_dict[model_used], messages=conversation_history, max_tokens=200, temperature=temperature)
    reply = [_.message.content for _ in completion.choices] 
    conversation_history.append({'role': 'assistant', 'content': reply[0]})
    return reply