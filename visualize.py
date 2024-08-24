import pandas as pd

model_used = 'gpt3.5'
scale_used = 'sds'

experiment_name = f"{model_used}_{scale_used}"
baseline_pth = f"./results/baseline_{experiment_name}.csv"
final_pth = f"./results/final_{experiment_name}.csv"
baseline_df = pd.read_csv(baseline_pth)
final_df = pd.read_csv(final_pth)
import matplotlib.pyplot as plt

import scales.bdi as bdi
import scales.phq_9 as phq_9
import scales.sds as sds

scale_dict = {
    'sds': sds,
    'phq_9': phq_9,
    'bdi': bdi
}

def GetInterpretation(df_pth):
    df = pd.read_csv(df_pth)
    df['sum'] = df.sum(axis=1)
    # 将'interpretation'列添加到baseline_df DataFrame中，该列将存储对'sum'列数值的解释
    df['interpretation'] = df['sum'].apply(scale_dict[scale_used].interpret_sum)
    df.to_csv(df_pth, index=False) 


GetInterpretation(baseline_pth)
GetInterpretation(final_pth)

fig, axs = plt.subplots(2, 2, figsize=(15, 5))  # 1行2列

plt.style.use('seaborn')
# 在第一个子图上绘制直方图
if 'sum' in baseline_df.columns:
    axs[0, 0].hist(baseline_df['sum'], bins=10)
    axs[0, 0].set_title('Baseline Answer Sum')
    axs[0, 0].set_xlabel('Value')
    axs[0, 0].set_ylabel('Frequency')

# 在第二个子图上绘制柱状图
if 'interpretation' in baseline_df.columns:
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
if 'sum' in final_df.columns:
    axs[0, 1].hist(final_df['sum'], bins=10)
    axs[0, 1].set_title('Final Answer Sum')
    axs[0, 1].set_xlabel('Value')
    axs[0, 1].set_ylabel('Frequency')

# 在新的子图的第二个位置绘制final_df的柱状图
if 'interpretation' in final_df.columns:
    interpretation_counts_final = final_df['interpretation'].value_counts()
    axs[1, 1].bar(interpretation_counts_final.index, interpretation_counts_final.values)
    axs[1, 1].set_title('Final Category Counts')
    axs[1, 1].set_xlabel('Interpretation')
    axs[1, 1].set_ylabel('Count')
    axs[1, 1].set_xticklabels(interpretation_counts_final.index, rotation=45)

# 调整布局以适应所有子图
plt.tight_layout()
# 显示图形
# 保存整个图形为图像文件
fig.savefig(f"./results/{experiment_name}.png")