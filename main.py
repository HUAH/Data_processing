import pandas as pd

# 读取Excel文件
df = pd.read_excel('cs.xlsx', sheet_name='Sheet1')

# 打开模板文件
with open('CE6863E(M-LAG) v2.1.txt', 'r') as file:
    template = file.read()

# 对于Excel文件中的每一行
for index, row in df.iterrows():
    # 复制模板
    result = template
    # 对于每一列
    for col in df.columns:
        # 替换模板中的占位符
        result = result.replace('<ztp:' + col + '>', str(row[col]))
    # 写入新的文本文件
    with open(row['Sysname'] + '.cfg', 'w') as file:
        file.write(result)
