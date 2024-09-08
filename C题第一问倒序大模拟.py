import pandas as pd

# 读取Excel
df2 = pd.read_excel('file2.xlsx')
df3 = pd.read_excel('file3.xlsx')
df4 = pd.read_excel('file4.xlsx')
df5 = pd.read_excel('total.xlsx')

# 创建总字典，分包
data_dict = {}
for col in df2.columns:
    data_dict[f'df2_{col}'] = df2[col].tolist()
for col in df3.columns:
    data_dict[f'df3_{col}'] = df3[col].tolist()

# 分发可用变量名
b23年分离地块与种植面积 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_种植面积/亩"]))
b23年分离地块与作物名称 = dict(zip(data_dict["df2_种植地块"], data_dict["df2_作物名称"]))
t历史作物 = [[i] for i in data_dict["df2_作物名称"]]
b分离地块与作物名称 = dict(zip(data_dict["df2_种植地块"], t历史作物))
b一季度地块与作物名称 = {k: v for k, v in b分离地块与作物名称.items() if "A" or "B" or "C" in k}
b二季度地块与作物名称 = {k: v for k, v in b分离地块与作物名称.items() if "D" or "E" or "F" in k}

c作物编号和作物种类 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物类型"]))
c作物编号和作物名称 = dict(zip(data_dict["df3_作物编号"], data_dict["df3_作物名称"]))
c作物名称和作物种类 = dict(zip(data_dict["df3_作物名称"], data_dict["df3_作物类型"]))

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
地块汇总 = ['aA1', 'aA2', 'aA3', 'aA4', 'aA5', 'aB1', 'aB2', 'aB3', 'aB4', 'aB5', 'aB6', 'aB7', 'aB8', 'aB9', 'aB10',
            'aB11', 'aB12', 'aB13', 'aB14', 'aC1', 'aC2', 'aC3', 'aC4', 'aC5', 'aC6', 'aD1', 'bD1', 'bD2', 'aD3', 'bD3',
            'aD4', 'bD4', 'aD5', 'bD5', 'aD6', 'bD6', 'aD7', 'aD8', 'aE1', 'bE1', 'aE2', 'bE2', 'aE3', 'bE3', 'aE4',
            'bE4', 'aE5', 'bE5', 'aE6', 'bE6', 'aE7', 'bE7', 'aE8',
            'bE8', 'aE9', 'bE9', 'aE10', 'bE10', 'aE11', 'bE11', 'aE12', 'bE12', 'aE13', 'bE13', 'aE14', 'bE14', 'aE15',
            'bE15', 'cE15', 'aE16', 'bE16', 'aF1', 'bF1', 'cF1', 'dF1', 'aF2', 'bF2', 'cF2', 'dF2', 'aF3', 'bF3', 'cF3',
            'aF4', 'bF4', 'cF4']

# 读取Excel文件
df = pd.read_excel('total.xlsx', sheet_name='Sheet1')
df3 = pd.read_excel('file3.xlsx', sheet_name='Sheet1')
df4 = pd.read_excel('file4.xlsx', sheet_name='Sheet1')

# 将数据转换为列表形式
data = []
data1 = []
e此年产量总表 = []

# 遍历Excel文件中的每一行
for index, row in df.iterrows():
    key = row[0]  # 读取最左侧一列的序号
    e此年产量总表.append({key: 0})
for index, row in df4.iterrows():
    key = row[0]
    values = row[1:].tolist()
    data.append({key: values})
for index, row in df.iterrows():
    key = row[0]
    values = row[1:].tolist()
    data1.append({key: values})

# 排序函数
d平均利润总表 = sorted(data, key=lambda x: list(x.values())[0][-1], reverse=True)
e产量总表 = sorted(data1, key=lambda x: list(x.values())[0][0], reverse=True)

# 将e产量总表转换为字典格式，方便查找
此年产量总表_dict = {list(item.keys())[0]: list(item.values())[0] for item in e此年产量总表}
地块与可行性原始列表 = [True for i in range(len(地块汇总))]
地块与可行性字典 = dict(zip(地块汇总,地块与可行性原始列表))

# print(f'e产量总表:{e产量总表}')
# print(f'd平均利润总表:{d平均利润总表}')
# print(f'e此年产量总表:{e此年产量总表}')

for w检测产物 in d平均利润总表:
    w作物名称 = list(w检测产物.values())[0][1]
    # 检测作物与产量对比
    for x检测作物 in e产量总表:
        x作物名称 = list(x检测作物.keys())[0]
        if x作物名称 == w作物名称:
            x检测作物值 = list(x检测作物.values())[0][0]
            x当前实际产量 = 此年产量总表_dict.get(x作物名称)
            if x当前实际产量 < x检测作物值:
                print(f"{x作物名称} 的产量符合条件，当前产量: {x当前实际产量}, 检测值: {x检测作物值}")

                # 上述代码：作物产量筛选过了，接下来我们安排一块地种植这种作物
                w作物种植地块类型 = list(w检测产物.values())[0][2]
                if w作物种植地块类型 == '平旱地':
                    print('这块地是平旱地')

                    for field in 地块平旱地:
                        h该地块历史作物列表 = ["豆类检测占位作物"] + b一季度地块与作物名称[field]
                        # print(
                        #     f"\n\n地块 {field} 的历史作物列表：{h该地块历史作物列表},\n最后一位及其作物种类：{h该地块历史作物列表[-1]}     {c作物名称和作物种类[h该地块历史作物列表[-1]]}\n")

                        # 豆类检查
                        if (len((c作物名称和作物种类[h该地块历史作物列表[-1]])) <= 4) and (
                                len((c作物名称和作物种类[h该地块历史作物列表[-2]])) <= 4):
                            # field这块地接下来必须种豆类
                            if w作物名称 not in 粮食豆类:
                                地块与可行性字典[field] = False

                        # 重茬检查
                        if h该地块历史作物列表[-1] == w作物名称:
                            地块与可行性字典[field] = False

                        if 地块与可行性字典[field]:
                            地块与可行性字典[field] = False
                            x当前实际产量 += b23年分离地块与种植面积[field]
                    print(f'{w作物名称}的面积为{x当前实际产量}')


                #
                # if w作物种植地块类型 == '梯田':
                #     print('这块地是梯田')
                # if w作物种植地块类型 == '山坡地':
                #     print('这块地是山坡地')
                # if w作物种植地块类型 == '水浇地':
                #     print('这块地是水浇地')
                # if w作物种植地块类型 == '普通大棚':
                #     print('这块地是普通大棚')
                # if w作物种植地块类型 == '智能大棚':
                #     print('这块地是智能大棚')
            else:
                print('else过了')
