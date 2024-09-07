import pandas as pd

# 读取Excel
df1 = pd.read_excel('file1.xlsx')
df2 = pd.read_excel('file2.xlsx')
df3 = pd.read_excel('file3.xlsx')
df4 = pd.read_excel('file4.xlsx')

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

# 分发可用变量名
a地块名和地块类型 = dict(zip(data_dict["df1_地块名称"], data_dict["df1_地块类型"]))
a地块名和地块面积 = dict(zip(data_dict["df1_地块名称"], data_dict["df1_地块面积/亩"]))

b23年分离地块与种植面积 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_种植面积/亩"]))
b23年分离地块与作物名称 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_作物名称"]))

c作物编号和作物种类 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物类型"]))
c作物编号和作物名称 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物名称"]))
c作物名称和作物种类 = dict(zip(data_dict["df3_作物名称"], data_dict["df3_作物类型"]))

d序号与作物名称 = dict(zip(data_dict["df4_序号"], data_dict["df4_作物名称"]))
d序号与地块类型 = dict(zip(data_dict["df4_序号"], data_dict["df4_地块类型"]))
d序号与亩产量 = dict(zip(data_dict["df4_序号"], data_dict["df4_亩产量/斤"]))
d序号与平均利润 = dict(zip(data_dict["df4_序号"], data_dict["df4_平均利润（元/亩/季度单位)"]))
d序号与种植季次 = dict(zip(data_dict["df4_序号"], data_dict["df4_种植季次"]))

# # 打印一些关键数据结构以确保数据正确
# print("a地块名和地块类型:", a地块名和地块类型)
# print("b23年分离地块与作物名称:", b23年分离地块与作物名称)
# print("d序号与作物名称:", d序号与作物名称)

# 计算23年各个作物产量
作物总产量 = {}

# 遍历每个地块
for field, crop_name in b23年分离地块与作物名称.items():
    field_prefix_removed = field[1:]  # 假设前缀是第一个字符
    a地块类型 = a地块名和地块类型.get(field_prefix_removed, "未知类型")
    地块面积 = a地块名和地块面积.get(field_prefix_removed, 0)

    print(f"this is {a地块类型}")

    # 确保地块类型和面积是有效的
    if a地块类型 != "未知类型" and 地块面积 > 0:
        print(f"处理地块: {field}, 作物: {crop_name}, 地块类型: {a地块类型}, 面积: {地块面积}")

        # 获取作物在该地块类型的亩产量
        if crop_name in d序号与作物名称.values():
            # 找到该作物的所有序号
            序号列表 = [i for i, name in d序号与作物名称.items() if name == crop_name]
            # 遍历序号列表，找到对应地块类型的亩产量
            for 序号 in 序号列表:
                if d序号与地块类型[序号] == a地块类型:
                    亩产量 = d序号与亩产量[序号]
                    # 计算总产量
                    if crop_name in 作物总产量:
                        作物总产量[crop_name] += 地块面积 * 亩产量
                    else:
                        作物总产量[crop_name] = 地块面积 * 亩产量
                    print(f"更新作物产量: {crop_name}, 总产量: {作物总产量[crop_name]}")
    else:
        print(f"未找到有效的地块类型或面积: {field}")

# 打印每个作物的总产量
if 作物总产量:
    for 作物, 产量 in 作物总产量.items():
        print(f"{作物} 的总产量为: {产量} 斤")
else:
    print("没有计算出任何作物的产量。")

# 创建一个新的DataFrame来存储作物和产量
crop_yield_df = pd.DataFrame(list(作物总产量.items()), columns=['作物名称', '总产量'])

# 打印DataFrame以确保数据正确
print(crop_yield_df)

# 导出DataFrame到Excel文件
output_file_path = '作物产量报表.xlsx'
crop_yield_df.to_excel(output_file_path, index=False)

print(f"作物产量已经成功导出到 {output_file_path}")
