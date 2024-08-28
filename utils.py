from openai import OpenAI
import os
import pandas as pd
import numpy as np
from tqdm import tqdm
import json
api_key = os.getenv('ALTERNATE_OPENAI_API_KEY')
# api_key = os.getenv('ALTERNATE_API_KEY_2')
client = OpenAI(base_url='https://openkey.cloud/v1',api_key=api_key)
# client = OpenAI(base_url='https://api.deerapi.com',api_key=api_key)

# 从 scales 目录下的 bdi.py 文件导入相关变量和函数
import scales.depression.bdi as bdi
import scales.depression.phq_9 as phq_9
import scales.depression.sds as sds
import scales.depression.hads_d as hads_d
import scales.anxiety.gad_7 as gad_7
import scales.anxiety.bai as bai
import scales.anxiety.hads_a as hads_a
import scales.anxiety.sas as sas

scale_used = 'sds'

scale_dict = {
    'gad_7': gad_7,
    'sds': sds,
    'phq_9': phq_9,
    'bdi': bdi,
    'hads_d': hads_d,
    'bai': bai,
    'hads_a': hads_a,
    'sas': sas
}

column_names = scale_dict[scale_used].column_names
question_prompt = scale_dict[scale_used].question_prompt
rule_prompt = scale_dict[scale_used].rule_prompt
valid_ans = scale_dict[scale_used].valid_ans

model_dict = {
    # Closed source models
    # OpenAI
    "gpt3.5": "gpt-3.5-turbo-1106", 
    "gpt4": "gpt-4-1106-preview",
    # Anthropic
    "claude3.5": "claude-3-5-sonnet-20240620",
    # Google
    "gemini1.5": "gemini-1.5-pro-preview-0514",
    # Zhipu AI
    "glm4": "glm-4-0520",
    # Moonshot AI
    "moonshot": "moonshot-v1-128k",
    # "moonshot": "moonshot-v1-32k",
    # Alibaba Group
    "qwenmax": "qwen-max-0428",
    # Baichuan AI
    "baichuan2": "Baichuan2-Turbo-192k",
    # Douyin Group
    "doubaopro": "doubao-pro-128k",
    # Open source models
    # Facebook
    "llama2": "llama2-70b-4096",
    "llama3": "llama3-70b-8192"
}

model_used = 'gpt3.5'

illness_tested = 'depression'

round_tested = 2

experiment_name = f"{model_used}_{scale_used}"
conversation_pth = f"./data/conversations/{model_used}_{illness_tested}.json"
baseline_pth = f"./results/baseline_{experiment_name}.csv"
final_pth = f"./results/final_{experiment_name}_{round_tested}round.csv"

# 进行几次测试
n_sample = 1 * 6


# 使用哪个模型，量表和人格生成规则

# 创建一个名为model_dict的字典，用于存储不同模型的名称和对应的标识符
def GetResponse(prompt, conversation_history, temperature):
    conversation_history.append({'role': 'user', 'content': prompt})
    # 开始一个无限循环，直到遇到break语句
    completion = client.chat.completions.create(model=model_dict[model_used], messages=conversation_history, max_tokens=200, temperature=temperature)
    reply = [_.message.content for _ in completion.choices] 
    conversation_history.append({'role': 'assistant', 'content': reply[0]})
    return reply