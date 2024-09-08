import pandas as pd

# 读取Excel文件
df = pd.read_excel('file4.xlsx', sheet_name='Sheet1')

# 将数据转换为列表形式
data = []

# 遍历每一行
for index, row in df.iterrows():
    key = row[0]  # 假设第一列为序号
    values = row[1:].tolist()  # 其他列数据转换为列表
    data.append({key: values})

# 排序函数
d平均利润总表 = sorted(data, key=lambda x: list(x.values())[0][-1], reverse=True)

print(d平均利润总表[86])
