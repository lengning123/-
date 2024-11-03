from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif'] = 'SimHei'

def leida(labels,values,ax):
    # 设置角度，用于平分切开一个圆面
    #fig, ax = plt.subplots(figsize=(8, 8), dpi=150, subplot_kw=dict(polar=True))
    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    values=values.values[0,:]
    # 闭合图形
    values = np.concatenate((values, [values[0]]))
    angles = np.concatenate((angles, [angles[0]]))

    # 绘图
    ax.plot(angles, values, linewidth=2,alpha=0.9)
    #ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(np.arange(0, 360, 360 / len(labels)), labels0)
    #plt.show()
    return ax

data=pd.read_excel('data529.xlsx')
data['finish_time']=[i.split('分')[0]+i.split('分')[-1][:-1] for i in data['finish_time']]
data['finish_time']=data['finish_time'].astype('int')
data.drop(data.index[data['finish_time']<70 ], inplace=True)
data['Q23']=data['Q23|1']+data['Q23|2']+data['Q23|3']+data['Q23|5']+data['Q23|4']+data['Q23|6']
k_data=data[['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9']]
pca = PCA()
X_pca = pca.fit_transform(k_data)
X_pca[:,5]=data['Q21|R2']
k_means=KMeans(n_clusters=4,init='k-means++')
k_means.fit(X_pca[:,:6])
data['label']=k_means.labels_
Q4_counts = data['label'].value_counts().reset_index()
Q4_counts.columns = ['label', '人数']
age1_counts = data[data['Q7']>=4]['label'].value_counts().reset_index()
age1_counts.columns = ['label', '有康养旅游意愿的人数']
Q4_counts = Q4_counts.merge(age1_counts, on='label', how='left').fillna(0)
Q4_counts['percent']=Q4_counts['有康养旅游意愿的人数']/Q4_counts['人数']
score=[]
for i in range(4):
    s=-0.25*data.loc[data['label']==i,'Q2'].mode()+0.2*data.loc[data['label']==i,'Q5'].mode()+\
      0.35*data.loc[data['label']==i,'Q7'].mode()+0.25*data.loc[data['label']==i,'Q21|R2'].mode()
    score.append(s)
Q4_counts['score']=np.asarray(score)
Q4_counts.sort_values(by='score',inplace=True,ascending=False)
print(Q4_counts)
data['Q3']-=1
labels=['Q1','Q2','Q3','Q4','Q5','Q6','Q7','Q8','Q9','Q21|R2']
labels0=['性别','年龄','学历','职业','身体情况','收入来源','个人收入','婚姻状态','子女数量','意愿']
fig, ax = plt.subplots(figsize=(8, 8), dpi=150,subplot_kw=dict(polar=True))
for i in Q4_counts['label'].values:
    print(i)
    ax=leida(labels0,data.loc[data['label']==i,labels].mode(axis=0),ax)

ax.set_thetagrids(np.arange(0, 360, 360 / len(labels)), labels0)

plt.legend(['高价值群体','较高价值群体','一般价值群体','低价值群体'],loc='upper right', bbox_to_anchor=(1.08, 1.1))
#plt.show()
plt.savefig('leida_all.png')

plt.plot(np.asarray([1,2,3,4,5,6]),np.asarray([3.341,1.809,1.253,0.867,0.728,0.636]))
plt.scatter(np.asarray([1,2,3,4,5,6]),np.asarray([3.341,1.809,1.253,0.867,0.728,0.636]))
plt.xlabel('因子个数')
plt.ylabel('特征根')
plt.show()
