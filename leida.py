import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

def leida(labels,values):
    # 设置角度，用于平分切开一个圆面
    fig, ax = plt.subplots(figsize=(8, 8), dpi=900, subplot_kw=dict(polar=True))
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values=values
    # 闭合图形
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # 绘图
    ax.plot(angles, values ,'g',linewidth=2,alpha=0.9)
    ax.fill(angles, values ,'g',alpha=0.25)
    plt.ylim([0,8])
    ax.set_thetagrids(np.arange(0, 360, 360 / len(labels)), labels0,fontsize=18,va='bottom', ha='center')
    ax.set_yticklabels(np.arange(1, 9), fontsize=20)
    plt.savefig('normal')

labels0=['性别','年龄','学历','职业','身体情况','收入来源','个人收入','婚姻状态','子女数量','意愿']
v=np.asarray([1,1,2,8,3,1,3,2,3,3])
leida(labels0,v)

plt.plot(np.arange(1,7),np.asarray([5.25,2.82,1.46,0.54,0.34,0.29]),marker='o',linestyle='-')
plt.xlabel('分类数')
plt.ylabel('聚合系数')
#plt.show()