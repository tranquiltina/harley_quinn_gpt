# pandas 是一个可用来进行数据分析的包
import pandas as pd
# tqdm函数可以用来显示进度条，使长循环的执行过程可视化
from tqdm import tqdm
# 导入os模块，这个模块提供了许多与操作系统交互的功能，比如文件和目录的创建、删除等
import numpy as np
import os
import time

from openai import OpenAI

# api_key = os.getenv('OPENAI_API_KEY')
api_key = os.getenv('ALTERNATE_OPENAI_API_KEY')
client = OpenAI(base_url='https://openkey.cloud/v1',api_key=api_key)

# 进行几次测试
n_sample = 20
# 控制生成文本的创造性，值越高生成的文本越多样
temperature = 0.7

# 使用哪个模型，量表和人格生成规则

# 创建一个名为model_dict的字典，用于存储不同模型的名称和对应的标识符
model_dict = {
    "gpt3.5": "gpt-3.5-turbo-1106", 
    "gpt4": "gpt-4-1106-preview"
}
model_used = 'gpt3.5'
# 从 scales 目录下的 bdi.py 文件导入相关变量和函数
import scales.bdi as bdi
import scales.phq_9 as phq_9
import scales.sds as sds
import scales.hads as hads
import cbt 

scale_used = 'phq_9'

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

experiment_name = f"{model_used}_{scale_used}"
baseline_pth = f"./results/baseline_{experiment_name}.csv"
final_pth = f"./results/final_{experiment_name}.csv"

# os.path.exists()函数用来检查给定的路径是否指向一个存在的文件或目录
# 创建一个pandas的DataFrame对象，DataFrame是pandas库中用于存储表格数据的主要数据结构
# columns参数用来指定DataFrame的列名，这里列名是从变量column_names中获取的
df = pd.DataFrame(columns=column_names)
# 将创建的DataFrame对象df保存到CSV文件中
# res_pth是保存CSV文件的路径
# index=False参数表示在保存CSV文件时不包括行索引
df.to_csv(baseline_pth, index=False)

df = pd.DataFrame(columns=column_names)
df.to_csv(final_pth, index=False)

def GetResponse(prompt, conversation_history):
    conversation_history.append({'role': 'user', 'content': prompt})
    # 开始一个无限循环，直到遇到break语句
    completion = client.chat.completions.create(model=model_dict[model_used], messages=conversation_history, max_tokens=200, temperature=temperature)
    reply = [_.message.content for _ in completion.choices] 
    conversation_history.append({'role': 'assistant', 'content': reply[0]})
    return reply

def GenConversation(personality_prompt):
    patient_profile = cbt.GenPatientPersonality()
    conversation_history_patient_side = [
        {"role": "system", "content": patient_profile},
    ]
    
    conversation_history_model_side = [
        {"role": "system", "content": personality_prompt}
    ]
    
    n_rounds = 4
    
    patient_talk = GetResponse("Hi, how can I help you today?", conversation_history_patient_side)[0]
    model_talk = GetResponse(patient_talk, conversation_history_model_side)[0]
    #print(model_talk)
    #print(conversation_history_patient_side)
    for i in range(n_rounds - 1):
        patient_talk = GetResponse(model_talk, conversation_history_patient_side)[0]
        model_talk = GetResponse(patient_talk, conversation_history_model_side)[0]
    return conversation_history_model_side
    
# range(n_sample)生成一个从0到n_sample-1的整数序列，
# tqdm函数用于显示一个进度条，在控制台输出，显示当前的进度百分比和估计剩余时间等信息
    
for i in tqdm(range(n_sample)):
    #personality, personality_debug = gen_personality()
    # 第一次获取没对话的 baseline
    # \n 是换行符
    model_personality_prompt = 'Do not reply more than three sentences.'
    baseline_data = []
    for j in question_prompt: 
        while True:
            query = rule_prompt + '\n' + \
            'Here is the question: ' + j 

            conversation_history = [{"role": "system", "content": model_personality_prompt}]
            # print(conversation_history)
            ans = GetResponse(query, conversation_history)
            if ans[0] in valid_ans:
                baseline_data.append(ans)
                break
            else:
                print(j, ans)
        
    baseline_data = np.array(baseline_data).transpose().tolist() 
    
    # 将data列表转换成一个pandas的DataFrame对象 new
    new_raw_res = pd.DataFrame(baseline_data, columns = column_names)
    
    previous_raw_res = pd.read_csv(baseline_pth)
    # 使用pd.concat()方法将previous和new两个DataFrame对象合并为一个新的DataFrame对象df
    # ignore_index=True参数表示在合并后的DataFrame中重新索引，忽略原来的索引
    baseline_df = pd.concat([previous_raw_res, new_raw_res], ignore_index=True)
    # 将合并后的DataFrame对象df保存到CSV文件中，路径为res_pth
    # index=False参数表示在保存CSV文件时不包括行索引
    baseline_df.to_csv(baseline_pth, index=False)
    final_data = []
        
    conversation = GenConversation(model_personality_prompt)
    print(conversation) 
    for j in question_prompt:
        while True:
            query = rule_prompt + '\n' + \
            'Here is the question: ' + j
            conversation_history = conversation 
            # print(conversation_history)
            ans = GetResponse(query, conversation_history)
            if ans[0] in valid_ans:
                final_data.append(ans)
                break
            else:
                print(j, ans)
        
    final_data = np.array(final_data).transpose().tolist() 
    
    # 将data列表转换成一个pandas的DataFrame对象 new
    new_raw_res = pd.DataFrame(final_data, columns = column_names)
    
    previous_raw_res = pd.read_csv(final_pth)
    # 使用pd.concat()方法将previous和new两个DataFrame对象合并为一个新的DataFrame对象df
    # ignore_index=True参数表示在合并后的DataFrame中重新索引，忽略原来的索引
    final_df = pd.concat([previous_raw_res, new_raw_res], ignore_index=True)
    # 将合并后的DataFrame对象df保存到CSV文件中，路径为res_pth
    # index=False参数表示在保存CSV文件时不包括行索引
    final_df.to_csv(final_pth, index=False)
        