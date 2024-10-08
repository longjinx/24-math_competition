import pandas as pd
from pulp import LpMaximize, LpProblem, LpVariable, lpSum

# 读取Excel
df1 = pd.read_excel('file4.xlsx')

data_dict = {}
for col in df1.columns:
    data_dict[f'df1_{col}'] = df1[col].tolist()

# 读取附件中的数据
attachment1 = pd.read_excel('附件1.xlsx')  # 包含地块信息
attachment2 = pd.read_excel('附件2.xlsx')  # 包含作物信息和 2023 年的统计数据
FoosnameToProfit = dict(zip(data_dict["df1_作物名称"], data_dict["df1_平均利润（元/亩/季度单位)"]))

# 使用表格中的实际列名
plots = attachment1[['地块名称', '地块类型', '地块面积/亩']].to_dict('records')
crops = attachment2[['作物名称', '作物类型', '种植面积/亩']].to_dict('records')

# 定义优化问题
model = LpProblem(name="Crop-Optimization", sense=LpMaximize)

# 决策变量：x[i][j][t] 表示第 t 年地块 i 种植作物 j 的面积
years = range(2024, 2031)  # 从 2024 年到 2030 年
x = LpVariable.dicts("x", ((i['地块名称'], j['作物名称'], t) for i in plots for j in crops for t in years),
                     lowBound=0, cat="Continuous")

# 辅助变量：z[i][j][t] 表示实际销售的作物产量（不能超过总产量和预期销售量的最小值）
z = LpVariable.dicts("z", ((i['地块名称'], j['作物名称'], t) for i in plots for j in crops for t in years),
                     lowBound=0, cat="Continuous")

# 二进制变量：y[i][j][t] 表示第 t 年地块 i 是否种植作物 j（1 表示种植，0 表示不种植）
y = LpVariable.dicts("y", ((i['地块名称'], j['作物名称'], t) for i in plots for j in crops for t in years),
                     lowBound=0, upBound=1, cat="Binary")

# 目标函数：最大化收益
model += lpSum(z[i['地块名称'], j['作物名称'], t] * j['种植面积/亩'] -
               x[i['地块名称'], j['作物名称'], t] * j['种植面积/亩'] for i in plots for j in crops for t in years)

# 约束条件

# 1. 每个地块每年的总种植面积不能超过其实际面积
for i in plots:
    for t in years:
        model += lpSum(x[i['地块名称'], j['作物名称'], t] for j in crops) <= i['地块面积/亩']

# 2. 作物实际销售产量 z[i][j][t] 不能超过作物的总产量和预期销售量
for i in plots:
    for j in crops:
        for t in years:
            model += z[i['地块名称'], j['作物名称'], t] <= x[i['地块名称'], j['作物名称'], t] * j['种植面积/亩']
            model += z[i['地块名称'], j['作物名称'], t] <= j['种植面积/亩']

# 3. 不重茬约束：同一地块不能连续两年种植相同作物
for i in plots:
    for j in crops:
        for t in range(2025, 2031):  # 确保 t 和 t-1 之间没有种植相同作物
            model += y[i['地块名称'], j['作物名称'], t] + y[i['地块名称'], j['作物名称'], t-1] <= 1

# 4. 每三年内必须种植一次豆类作物
for i in plots:
    for t in range(2024, 2028):
        model += lpSum(y[i['地块名称'], j['作物名称'], t+k] for j in crops if j['作物类型'] == '豆类' for k in range(3)) >= 1

# 5. 面积约束：如果某地块某年种植某作物，则种植面积必须大于 0
for i in plots:
    for j in crops:
        for t in years:
            model += x[i['地块名称'], j['作物名称'], t] <= y[i['地块名称'], j['作物名称'], t] * i['地块面积/亩']

# 求解模型
status = model.solve()

# 输出结果
results = []

for i in plots:
    for j in crops:
        for t in years:
            if x[i['地块名称'], j['作物名称'], t].value() > 0:
                results.append({
                    '地块名称': i['地块名称'],
                    '年份': t,
                    '作物名称': j['作物名称'],
                    '种植面积/亩': x[i['地块名称'], j['作物名称'], t].value()
                })

# 将结果转换为 DataFrame
df_results = pd.DataFrame(results)

# 按照地块名称、年份和作物名称分组，并汇总种植面积
df_results_grouped = df_results.groupby(['地块名称', '年份', '作物名称'], as_index=False).agg({'种植面积/亩': 'sum'})

# 将结果输出到 Excel 文件
df_results_grouped.to_excel('种植优化结果.xlsx', index=False)

print(f"求解状态: {status}")
print("结果已成功保存到 '种植优化结果.xlsx'")
