import pandas as pd

# 读取Excel文件
df = pd.read_excel('file4.xlsx')

# 创建一个大列表来存储结果
data_list = []

# 遍历Excel文件中的每一行
for index, row in df.iterrows():
    key = row[0]  # 读取最左侧一列的序号
    data_list.append({key: 0})  # 将序号作为键，值初始化为0

print(data_list)
