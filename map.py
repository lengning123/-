import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Map
import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

data = [
    #("江岸区", 1),
    #("江汉区", 1),
    #("硚口区", 1),
    #("汉阳区", 1),
    #("武昌区", 1),
    #("青山区", 1),
    ("洪山区", None),
    ("蔡甸区", 9),
    #("江夏区", 9),
    #("黄陂区", 9),
    #("新洲区", 9),
    #('东西湖区',9),
    #('汉南区',9),
]


map = (
    Map()
    .add("", data, "武汉",is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="武汉市地图"),
        visualmap_opts=opts.VisualMapOpts(max_=13,min_=1, is_piecewise=True),
    )
    .set_series_opts(label_opts=opts.LabelOpts(is_show=False),
                     #itemstyle_opts={"normal": {"color": lambda x: color_list[data[x][1]-1] for x in range(13)}}
                     )
)
#地区名字显示
map.render("蔡甸区.html")

'''data=pd.read_excel('222.xlsx')
data=data['money'].values
plt.plot(np.arange(len(data[:4]))+2018,data[:4],color='#7bcfa6')
plt.plot(np.asarray([2021,2023]),data[[3,5]],color='#ff4e20')
plt.plot(np.arange(len(data[5:]))+2023,data[5:],color='#ff4e20')
plt.xlabel('年份')
plt.ylabel('市场规模（亿元）')
plt.show()'''