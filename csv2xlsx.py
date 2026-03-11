import pandas as pd
import sys
import time
# 构造数据
# df = pd.DataFrame({'data': [5, 10, 30, 50, 40, 30, 60]},
#                 index=[11, 22, 42, 83, 94, 111, 333])
# df

input_file = sys.argv[1]
output_file = sys.argv[1].replace("csv","xlsx").replace("meminfo","meminfo"+str(time.strftime("%Y_%m_%d_%H_%M_%S")))

print(input_file,output_file)

df = pd.read_csv(input_file)
h = df.shape[0] + 1
l = df.shape[1]-1
columns = df.columns
print(h, l)
print(columns)

# 使用XlsxWriter作为引擎创建Excel编写器。xi
writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

# 将数据框转换为XlsxWriter Excel对象。
df.to_excel(writer, index=False, header=True)

# 获取xlsxwriter工作簿和工作表对象。
workbook = writer.book
worksheet = writer.sheets['Sheet1']

aaa = ["B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S",
       "T", "U", "V", "W", "X", "Y", "Z","AA","AB","AC","AD","AE","AF","AG","AH","AI","AJ"]

for x in range(l):
    xx = x + 1
    xxx = x + 2
    # 创建图表对象, 类型设置为折线图
    chart = workbook.add_chart({'type': 'line'})

    # 设置图形的标题
    chart.set_title({'name': '{} 的折线图'.format(columns[xx])})
    # 从dataframe数据配置图表，指定序列数据区域
    chart.add_series({
        'categories': '=Sheet1!$A$2:$A${}'.format(h),  # x轴显示内容
        'values': '=Sheet1!${}2:${}${}'.format(aaa[x], aaa[x], h),
        'line': {'color': 'red'},  # 线条颜色
        'name': 'data',  # 图例名称
    })
    chart.width = 1400
    # 将图表插入工作表，指定图表的位置
    xxxx = h + 15 * x + 1
    worksheet.insert_chart('D{}'.format(xxxx), chart)

# 关闭Excel writer并输出Excel文件
writer.save()
