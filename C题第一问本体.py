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
# 开始筛选
for field in b一季度地块与作物名称.keys():
    # 能种哪些
    check_food_list = data_dict["df3_作物名称"]

    h该地块历史作物列表 = ["豆类检测占位作物"] + b一季度地块与作物名称[field]
    print(f"\n\n{field}的历史作物列表：{h该地块历史作物列表},\n\n最后一位：{h该地块历史作物列表[-1]}\n")
    print(f"作物种类：{(c作物名称和作物种类[h该地块历史作物列表[-1]])}\n")
    # 重茬检查
    if h该地块历史作物列表[-1] in check_food_list:
        check_food_list.remove(h该地块历史作物列表[-1])

    check_food_list_onlytofor = list(check_food_list)
    # 遍历作物检查表
    for check_food in check_food_list_onlytofor:
        # print(f"\n当前checkfood: {check_food}")
        # print(f"当前checkfoodlist: {check_food_list}")

        # 只留粮食
        if c作物名称和作物种类[check_food][0] != "粮":
            # print(f"过if的checkfood: {check_food}")
            check_food_list.remove(check_food)

        # 豆类检查
        elif (len((c作物名称和作物种类[h该地块历史作物列表[-1]])) <= 4) and (
                len((c作物名称和作物种类[h该地块历史作物列表[-2]])) <= 4):
            # 接下来必须种豆类
            for i in c作物名称和作物种类.keys():
                if i in check_food_list and c作物名称和作物种类[i][-3] != "豆":
                    check_food_list.remove(i)

        print(f"\n{check_food}的剩余可用列表：{check_food_list}")
