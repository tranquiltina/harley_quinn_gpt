import seaborn as sns

from utils import *

baseline_df = pd.read_csv(baseline_pth)
final_df = pd.read_csv(final_pth)
import matplotlib.pyplot as plt

def GetInterpretation(df_pth):
    df = pd.read_csv(df_pth)
    df['sum'] = df.sum(axis=1)
    # 将'interpretation'列添加到baseline_df DataFrame中，该列将存储对'sum'列数值的解释
    df['interpretation'] = df['sum'].apply(scale_dict[scale_used].interpret_sum)
    df.to_csv(df_pth, index=False) 
    
if 'sum' not in baseline_df.columns:
    GetInterpretation(baseline_pth)
    baseline_df = pd.read_csv(baseline_pth)
if 'sum' not in final_df.columns:
    GetInterpretation(final_pth)
    final_df = pd.read_csv(final_pth)

import pingouin as pg

num_questions = len(scale_dict[scale_used].column_names)

baseline_cr_alpha = pg.cronbach_alpha(data=baseline_df.iloc[:, :num_questions])
print(baseline_df.iloc[:, :num_questions])
print(f"Baseline test Cronbach's alpha: {baseline_cr_alpha}")
final_cr_alpha = pg.cronbach_alpha(data=final_df.iloc[:, :num_questions])

print(f"Final test Cronbach's alpha: {final_cr_alpha}")

from scipy.stats import pearsonr

def guttman_split_half_correlation(df: pd.DataFrame) -> float:
    """
    计算 Guttman Split-Half Correlation。

    参数：
    df (pd.DataFrame): 包含问卷回答的 DataFrame，每一列是一个问题的回答，每一行是一个参与者。

    返回：
    float: Guttman Split-Half Correlation 值。
    """
    half = len(df.columns) // 2

    # 前半部分和后半部分
    first_half = df.iloc[:, :half]
    second_half = df.iloc[:, half:]

    # 计算每一半的总得分
    first_half_scores = first_half.sum(axis=1)
    second_half_scores = second_half.sum(axis=1)

    # 计算相关性
    correlation, _ = pearsonr(first_half_scores, second_half_scores)

    return correlation

baseline_split_half_corr = guttman_split_half_correlation(baseline_df.iloc[:, :num_questions])

print(f"Baseline test Guttman split-half correlation: {baseline_split_half_corr}")

final_split_half_corr = guttman_split_half_correlation(final_df.iloc[:, :num_questions])

print(f"Final test Guttman split-half correlation: {final_split_half_corr}")

fig, axs = plt.subplots(3, 2, figsize=(12,12))

#sns.set_style('white')
plt.style.use('fast')
# 在第一个子图上绘制直方图
axs[0, 0].hist(baseline_df['sum'], bins=10)
axs[0, 0].set_title('Baseline Answer Sum')
axs[0, 0].set_xlabel('Value')
axs[0, 0].set_ylabel('Frequency')

# 在第二个子图上绘制柱状图
interpretation_counts = baseline_df['interpretation'].value_counts()
#print(interpretation_counts)
axs[1, 0].bar(interpretation_counts.index, interpretation_counts.values)
axs[1, 0].set_title('Baseline Category Counts')
axs[1, 0].set_xlabel('Interpretation')
axs[1, 0].set_ylabel('Count')
axs[1, 0].set_xticklabels(interpretation_counts.index, rotation=45)  # 旋转x轴标签

# 调整子图间的间距
plt.tight_layout()
# 创建一个新的2x2子图布局，并且指定行索引为2

# 在新的子图中的第一个位置绘制final_df的直方图
axs[0, 1].hist(final_df['sum'], bins=10)
axs[0, 1].set_title('Final Answer Sum')
axs[0, 1].set_xlabel('Value')
axs[0, 1].set_ylabel('Frequency')

# 在新的子图的第二个位置绘制final_df的柱状图
interpretation_counts_final = final_df['interpretation'].value_counts()
axs[1, 1].bar(interpretation_counts_final.index, interpretation_counts_final.values)
axs[1, 1].set_title('Final Category Counts')
axs[1, 1].set_xlabel('Interpretation')
axs[1, 1].set_ylabel('Count')
axs[1, 1].set_xticklabels(interpretation_counts_final.index, rotation=45)


baseline_per_question = baseline_df.iloc[:, :num_questions]
sums = baseline_per_question.apply(lambda x: x.value_counts().reindex(range(int(scale_dict[scale_used].valid_ans[0]), int(scale_dict[scale_used].valid_ans[-1]) + 1), fill_value=0))
bottoms = np.zeros(sums.shape[1])
for i in range(sums.shape[0]):
    axs[2, 0].bar(sums.columns, sums.iloc[i], bottom=bottoms, label=f'{i}')

    # 更新底部位置
    bottoms += sums.iloc[i]
axs[2, 0].set_title('Baseline per Question Count')
axs[2, 0].set_xlabel('Question')
axs[2, 0].set_ylabel('Sum')
axs[2, 0].legend(title='Response Value')

final_per_question = final_df.iloc[:, :num_questions]
sums = final_per_question.apply(lambda x: x.value_counts().reindex(range(int(scale_dict[scale_used].valid_ans[0]), int(scale_dict[scale_used].valid_ans[-1]) + 1), fill_value=0))
#print(sums)
bottoms = np.zeros(sums.shape[1])
for i in range(sums.shape[0]):
    axs[2, 1].bar(sums.columns, sums.iloc[i], bottom=bottoms, label=f'{i}')

    # 更新底部位置
    bottoms += sums.iloc[i]
axs[2, 1].set_title('Final per Question Count')
axs[2, 1].set_xlabel('Question')
axs[2, 1].set_ylabel('Sum')
axs[2, 1].legend(title='Response Value')
# 调整布局以适应所有子图
#plt.tight_layout()
# 显示图形
# 保存整个图形为图像文件
fig.savefig(f"./results/{experiment_name}.png", dpi=300)