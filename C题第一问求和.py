import pandas as pd

# 读取Excel文件
df = pd.read_excel('rusult222.xlsx')

# 对前三列进行分组，并对第四列（'种植面积/亩'）求和
result = df.groupby(['地块名称', '年份', '作物名称'], as_index=False)['种植面积/亩'].sum()

# 将结果写入新的Excel文件
result.to_excel('result_processed2223.xlsx', index=False)

import pandas as pd

# 读取Excel文件
df = pd.read_excel('rusult222.xlsx')

# 对前三列进行分组，并对第四列（'种植面积/亩'）求和
result = df.groupby(['地块名称'], as_index=False)['种植面积/亩'].sum()

# 将结果写入新的Excel文件
result.to_excel('result_processed2224.xlsx', index=False)