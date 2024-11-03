import pandas as pd
import numpy as np
from statsmodels.sandbox.stats.runs import runstest_1samp
import matplotlib.pyplot as plt
from pyecharts.charts import Pie
from pyecharts import options as opts
from pyecharts.globals import ThemeType
import seaborn as sns

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

data=pd.read_excel('data529.xlsx')
data['finish_time']=[i.split('分')[0]+i.split('分')[-1][:-1] for i in data['finish_time']]
data['finish_time']=data['finish_time'].astype('int')
data.drop(data.index[data['finish_time']<35 ], inplace=True)
#print(len(data.index))

'''age_mapping = {
    1: '45岁-54岁',
    2: '55岁-64岁',
    3: '65岁及以上'
}

data['age_category'] = data['Q2'].map(age_mapping)

# 统计各个分类的数量
age_counts = data['age_category'].value_counts()

# 绘制饼图
pie = (
    Pie()
    .add("", [list(z) for z in zip(age_counts.index.tolist(), age_counts.tolist())])
    .set_global_opts(title_opts=opts.TitleOpts(title="年龄分布"),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=22)))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", font_size=22))
)

pie.render("age_distribution.html")'''

degree_mapping = {
    1: '初中及以下',
    2: '高中及以下',
    3: '大专',
    4:'本科及以上',
    5:'本科及以上',
    6:'本科及以上',
}

data['degree_category'] = data['Q3'].map(degree_mapping)

# 统计各个分类的数量
degree_counts = data['degree_category'].value_counts()

# 绘制饼图
pie1 = (
    Pie()
    .add("", [list(z) for z in zip(degree_counts.index.tolist(), degree_counts.tolist())])
    .set_global_opts(title_opts=opts.TitleOpts(title="学历分布"),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=22)))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", font_size=22))
)

pie1.render("degree_distribution2.html")

job_mapping = {
    1: '机关单位工作人员',
    2: '事业单位工作人员',
    3: '企业管理及一般工作人员',
    4:'服务人员',
    5:'个体户、私营业主',
    6:'文化教育工作者',
    7:'科技、医疗卫生工作者',
    8:'自由职业者',
    9:'其他',
}

data['Q4'] = data['Q4'].map(job_mapping)

Q4_counts = data['Q4'].value_counts().reset_index()
Q4_counts.columns = ['Q4', '人数']
age1_counts = data[data['Q21|R2'] >=4]['Q4'].value_counts().reset_index()
age1_counts.columns = ['Q4', '有康养旅游意愿的人数']
Q4_counts = Q4_counts.merge(age1_counts, on='Q4', how='left').fillna(0)
job_counts_long = pd.melt(Q4_counts, id_vars=['Q4'], value_vars=['人数', '有康养旅游意愿的人数'], var_name='type', value_name='count_value')
# 设置图形大小
plt.figure(figsize=(10, 6))

sns.barplot(x='Q4', y='count_value', hue='type', data=job_counts_long, palette=['skyblue', 'lightcoral'])

# 添加图例
plt.legend()

# 添加标题和标签
plt.xlabel('职业')
plt.ylabel('人数')
plt.title('职业分布图')

# 显示图形
plt.show()

health_mapping = {
    1: '健康',
    2: '良好',
    3: '一般',
    4:'较差',
}

data['Q5'] = data['Q5'].map(health_mapping)

Q5_counts = data['Q5'].value_counts().reset_index()
Q5_counts.columns = ['Q5', '人数']
age1_counts = data[data['Q21|R2'] >=4]['Q5'].value_counts().reset_index()
age1_counts.columns = ['Q5', '有康养旅游意愿的人数']
Q5_counts = Q5_counts.merge(age1_counts, on='Q5', how='left').fillna(0)
health_counts_long = pd.melt(Q5_counts, id_vars=['Q5'], value_vars=['人数', '有康养旅游意愿的人数'], var_name='type', value_name='count_value')
# 设置图形大小
plt.figure(figsize=(10, 6))

sns.barplot(x='Q5', y='count_value', hue='type', data=health_counts_long, palette=['skyblue', 'lightcoral'])

# 添加图例
plt.legend()

# 添加标题和标签
plt.xlabel('健康情况')
plt.ylabel('人数')
plt.title('职业分布图')

# 显示图形
plt.show()


earn_mapping = {
    1: '2千元及以下',
    2: '2千-5千元',
    3: '5千-8千元',
    4:'8千-1.2万元',
    5:'1.2万-1.8万元',
    6:'1.8万元以上',
}

data['earn_category'] = data['Q7'].map(earn_mapping)

# 统计各个分类的数量
earn_counts = data['earn_category'].value_counts()

# 绘制饼图
pie = (
    Pie(init_opts=opts.InitOpts(width="1000px", height="800px"))
    .add("", [list(z) for z in zip(earn_counts.index.tolist(), earn_counts.tolist())],radius=["40%", "75%"])
    .set_global_opts(title_opts=opts.TitleOpts(title="月收入分布"),
                     legend_opts=opts.LegendOpts(textstyle_opts=opts.TextStyleOpts(font_size=22),pos_top="bottom"))
    .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}", font_size=22))
)

pie.render("earn_distribution.html")