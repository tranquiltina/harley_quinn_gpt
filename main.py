# pandas 是一个可用来进行数据分析的包
import pandas as pd
# tqdm函数可以用来显示进度条，使长循环的执行过程可视化
from tqdm import tqdm
# 导入os模块，这个模块提供了许多与操作系统交互的功能，比如文件和目录的创建、删除等
import numpy as np
import os
import time

from openai import OpenAI

api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

# 进行几次测试
n_sample = 10
# 控制生成文本的创造性，值越高生成的文本越多样
temperature = 0.7
test_flag = False
# 使用哪个模型，量表和人格生成规则
model_dict = {
    "gpt3.5": "gpt-3.5-turbo-1106", 
    "gpt4": "gpt-4-1106-preview"
}
model_used = 'gpt3.5'

import scales.bdi as bdi
import scales.phq_9 as phq_9
import scales.sds as sds

scale_used = 'sds'

scale_dict = {
    'sds': sds,
    'phq_9': phq_9,
    'bdi': bdi
}

column_names = scale_dict[scale_used].column_names
question_prompt = scale_dict[scale_used].question_prompt
rule_prompt = scale_dict[scale_used].rule_prompt

import personalities.big_five as big_five

personality_used = 'big_five'

personality_dict = {
    'big_five': big_five
}

experiment_name = f"{model_used}_{personality_used}_{scale_used}"
gen_personality = personality_dict[personality_used].gen_personality
baseline_pth = f"./results/baseline_{experiment_name}.csv"
personality_pth = f"./results/personality_{experiment_name}.csv"

# os.path.exists()函数用来检查给定的路径是否指向一个存在的文件或目录
if not os.path.exists(baseline_pth) or test_flag:
    # 创建一个pandas的DataFrame对象，DataFrame是pandas库中用于存储表格数据的主要数据结构
    # columns参数用来指定DataFrame的列名，这里列名是从变量column_names中获取的
    df = pd.DataFrame(columns=column_names)
    # 将创建的DataFrame对象df保存到CSV文件中
    # res_pth是保存CSV文件的路径
    # index=False参数表示在保存CSV文件时不包括行索引
    df.to_csv(baseline_pth, index=False)

if not os.path.exists(personality_pth) or test_flag:
    df = pd.DataFrame(columns=['personality'])
    df.to_csv(personality_pth, index=False)
    
if test_flag:
    # range(n_sample)生成一个从0到n_sample-1的整数序列，
    # tqdm函数用于显示一个进度条，在控制台输出，显示当前的进度百分比和估计剩余时间等信息
    for i in tqdm(range(n_sample)):
        personality, personality_debug = gen_personality()
        previous_personality = pd.read_csv(personality_pth)
        new_personality = pd.DataFrame([personality_debug], columns =['personality'])
        personality_df = pd.concat([previous_personality, new_personality], ignore_index=True)
        personality_df.to_csv(personality_pth, index=False)
        
        personality_prompt = """You play a respondent who is participating in a survey.\
        {}
        Please answer the questions as concisely as possible.\
        You should only give the score with no reasons. """.format(personality)

        # \n 是换行符
        data = []
        for j in question_prompt: 
            background = personality_prompt +'\n' + rule_prompt + '\n' + \
            'Here are the questions: [' + j + ']' + '\n' + \
            'Please carefully obey the rule: ' + rule_prompt

            msg = [{"role": "system", "content": personality_prompt},
                    {"role": "user", "content": background}]
            # print(msg)

            # 开始一个无限循环，直到遇到break语句
            while True:
                try:
                    # 尝试执行client.chat.completions.create()方法
                    completion = client.chat.completions.create(model=model_dict[model_used], messages=msg, max_tokens=200, temperature=temperature)
                    # 如果正常执行，跳出循环
                    break
                except:
                    # 否则使程序暂停1秒，然后继续尝试
                    time.sleep(1)
    
            # 将completion.choices中的每个消息内容提取出来，并存入列表ans中
            # _.message.content表示choices列表中每个元素的消息内容
            ans = [_.message.content for _ in completion.choices]
            data.append(ans)
        
        data = np.array(data).transpose().tolist() 
    
        # 将data列表转换成一个pandas的DataFrame对象 new
        new_raw_res = pd.DataFrame(data, columns = column_names)
    
        previous_raw_res = pd.read_csv(baseline_pth)
        # 使用pd.concat()方法将previous和new两个DataFrame对象合并为一个新的DataFrame对象df
        # ignore_index=True参数表示在合并后的DataFrame中重新索引，忽略原来的索引
        baseline_df = pd.concat([previous_raw_res, new_raw_res], ignore_index=True)
        # 将合并后的DataFrame对象df保存到CSV文件中，路径为res_pth
        # index=False参数表示在保存CSV文件时不包括行索引
        baseline_df.to_csv(baseline_pth, index=False)

    baseline_df = pd.read_csv(baseline_pth)
    baseline_df['sum'] = baseline_df.sum(axis=1)
    baseline_df['interpretation'] = baseline_df['sum'].apply(scale_dict[scale_used].interpret_sum)
    baseline_df.to_csv(baseline_pth, index=False)

baseline_df = pd.read_csv(baseline_pth)
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2, figsize=(15, 5))  # 1行2列
plt.style.use('seaborn')
# 在第一个子图上绘制直方图
if 'sum' in baseline_df.columns:
    axs[0].hist(baseline_df['sum'], bins=10)
    axs[0].set_title('Baseline Answer Sum')
    axs[0].set_xlabel('Value')
    axs[0].set_ylabel('Frequency')

# 在第二个子图上绘制柱状图
if 'interpretation' in baseline_df.columns:
    interpretation_counts = baseline_df['interpretation'].value_counts()
    #print(interpretation_counts)
    axs[1].bar(interpretation_counts.index, interpretation_counts.values)
    axs[1].set_title('Baseline Category Counts')
    axs[1].set_xlabel('Interpretation')
    axs[1].set_ylabel('Count')
    axs[1].set_xticklabels(interpretation_counts.index, rotation=45)  # 旋转x轴标签

# 调整子图间的间距
plt.tight_layout()

# 保存整个图形为图像文件
fig.savefig(f"./results/{experiment_name}.png")