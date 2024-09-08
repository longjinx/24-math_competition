import pandas as pd

# 读取Excel文件
df = pd.read_excel('total.xlsx', sheet_name='Sheet1')
df3 = pd.read_excel('file3.xlsx', sheet_name='Sheet1')
df4 = pd.read_excel('file4.xlsx', sheet_name='Sheet1')

# 将数据转换为列表形式
data = []
e此年产量总表 = []

# 遍历Excel文件中的每一行
for index, row in df.iterrows():
    key = row[0]  # 读取最左侧一列的序号
    e此年产量总表.append({key: 0})
for index, row in df4.iterrows():
    key = row[0]
    values = row[1:].tolist()
    data.append({key: values})


# 排序函数
d平均利润总表 = sorted(data, key=lambda x: list(x.values())[0][-1], reverse=True)

print((d平均利润总表)[50])

