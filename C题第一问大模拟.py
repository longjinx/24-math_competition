import pandas as pd

# 读取Excel
df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')
df3 = pd.read_excel('file3.xlsx')
df4 = pd.read_excel('file4.xlsx')
df5 = pd.read_excel('total.xlsx')

# 创建总字典，分包
data_dict = {}
for col in df1.columns:
    data_dict[f'df1_{col}'] = df1[col].tolist()
for col in df2.columns:
    data_dict[f'df2_{col}'] = df2[col].tolist()
for col in df3.columns:
    data_dict[f'df3_{col}'] = df3[col].tolist()
for col in df4.columns:
    data_dict[f'df4_{col}'] = df4[col].tolist()
for col in df5.columns:
    data_dict[f'df5_{col}'] = df5[col].tolist()

# 分发可用变量名
a地块名和地块类型 = dict(zip(data_dict["df1_地块名称"], data_dict["df1_地块类型"]))
a地块名和地块面积 = dict(zip(data_dict["df1_地块名称"], data_dict["df1_地块面积/亩"]))

b23年分离地块与种植面积 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_种植面积/亩"]))
b23年分离地块与作物名称 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_作物名称"]))
t历史作物 = [[i] for i in data_dict["df2_作物名称"]]
b分离地块与作物名称 = dict(zip(data_dict["df2_种植地块"], t历史作物))
b一季度地块与作物名称 = {k: v for k, v in b分离地块与作物名称.items() if "A" or "B" or "C" in k}
b二季度地块与作物名称 = {k: v for k, v in b分离地块与作物名称.items() if "D" or "E" or "F" in k}

c作物编号和作物种类 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物类型"]))
c作物编号和作物名称 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物名称"]))
c作物名称和作物种类 = dict(zip(data_dict["df3_作物名称"], data_dict["df3_作物类型"]))

d序号与作物名称 = dict(zip(data_dict["df4_序号"], data_dict["df4_作物名称"]))
d序号与地块类型 = dict(zip(data_dict["df4_序号"], data_dict["df4_地块类型"]))
d序号与亩产量 = dict(zip(data_dict["df4_序号"], data_dict["df4_亩产量/斤"]))
d序号与平均利润 = dict(zip(data_dict["df4_序号"], data_dict["df4_平均利润（元/亩/季度单位)"]))
d序号与种植季次 = dict(zip(data_dict["df4_序号"], data_dict["df4_种植季次"]))

e作物名称与预计销售量 = dict(zip(data_dict["df5_作物名称"], data_dict["df5_总产量"]))

粮食豆类 = ['黄豆', '黑豆', '红豆', '绿豆', '爬豆']
粮食非豆类 = ['玉米', '谷子', '高粱', '黍子', '荞麦', '南瓜', '红薯', '莜麦', '大麦', '水稻', '小麦']

蔬菜豆类 = ['豇豆', '刀豆', '芸豆']
蔬菜一般 = ['土豆', '西红柿', '茄子', '菠菜', '青椒', '菜花', '包菜', '油麦菜', '小青菜', '黄瓜', '生菜', '辣椒',
            '空心菜', '黄心菜', '芹菜']
蔬菜白菜 = ['大白菜', '白萝卜', '红萝卜']

菌类 = ['榆黄菇', '香菇', '白灵菇', '羊肚菌']

地块平旱地 = ['aA1', 'aA2', 'aA3', 'aA4', 'aA5']
地块梯田 = ['aB1', 'aB2', 'aB3', 'aB4', 'aB5', 'aB6', 'aB7', 'aB8', 'aB9', 'aB10', 'aB11', 'aB12', 'aB13', 'aB14']
地块山坡地 = ['aC1', 'aC2', 'aC3', 'aC4', 'aC5', 'aC6']
地块水浇地 = ['aD1', 'bD1', 'bD2', 'aD3', 'bD3', 'aD4', 'bD4', 'aD5', 'bD5', 'aD6', 'bD6', 'aD7', 'aD8']
地块普通大棚 = ['aE1', 'bE1', 'aE2', 'bE2', 'aE3', 'bE3', 'aE4', 'bE4', 'aE5', 'bE5', 'aE6', 'bE6', 'aE7', 'bE7', 'aE8',
                'bE8', 'aE9', 'bE9', 'aE10', 'bE10', 'aE11', 'bE11', 'aE12', 'bE12', 'aE13', 'bE13', 'aE14', 'bE14',
                'aE15', 'bE15', 'cE15', 'aE16', 'bE16']
地块智能大棚 = ['aF1', 'bF1', 'cF1', 'dF1', 'aF2', 'bF2', 'cF2', 'dF2', 'aF3', 'bF3', 'cF3', 'aF4', 'bF4', 'cF4']

# 开始筛选
for field in 地块平旱地:
    h该地块历史作物列表 = ["豆类检测占位作物"] + b一季度地块与作物名称[field]
    print(
        f"\n\n{field}的历史作物列表：{h该地块历史作物列表},\n最后一位及其作物种类：{h该地块历史作物列表[-1]}     {c作物名称和作物种类[h该地块历史作物列表[-1]]}\n")

    # 豆类检查
    if (len((c作物名称和作物种类[h该地块历史作物列表[-1]])) <= 4) and (
            len((c作物名称和作物种类[h该地块历史作物列表[-2]])) <= 4):
        # 接下来必须种豆类
        check_food_list = 粮食豆类
    else:
        check_food_list = 粮食豆类 + 粮食非豆类

    # 重茬检查
    if h该地块历史作物列表[-1] in check_food_list:
        check_food_list.remove(h该地块历史作物列表[-1])

    print(f"剩余可用列表：{check_food_list}")
