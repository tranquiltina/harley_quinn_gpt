from utils import *

# os.path.exists()函数用来检查给定的路径是否指向一个存在的文件或目录
# 创建一个pandas的DataFrame对象，DataFrame是pandas库中用于存储表格数据的主要数据结构
# columns参数用来指定DataFrame的列名，这里列名是从变量column_names中获取的
df = pd.DataFrame(columns=column_names)
# 将创建的DataFrame对象df保存到CSV文件中
# res_pth是保存CSV文件的路径
# index=False参数表示在保存CSV文件时不包括行索引
df.to_csv(baseline_pth, index=False)

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