from utils import *

df = pd.DataFrame(columns=column_names)
df.to_csv(final_pth, index=False)

# range(n_sample)生成一个从0到n_sample-1的整数序列，
# tqdm函数用于显示一个进度条，在控制台输出，显示当前的进度百分比和估计剩余时间等信息

with open(conversation_pth, 'r') as file:
    conversations = json.load(file)

for i in tqdm(range(n_sample)):
    final_data = []
    
    conversation = conversations[i]
    num_messages = 2 * round_tested + 1
    
    # 截取所需数量的对话
    conversation = conversation[:num_messages]
    print(conversation) 
    for j in question_prompt:
        while True:
            query = rule_prompt + '\n' + \
            'Here is the question: ' + j
            conversation_history = conversation 
            # print(conversation_history)
            ans = GetResponse(query, conversation_history, 0)
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
        