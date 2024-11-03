from sklearn.tree import DecisionTreeClassifier,export_graphviz
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score
import pydotplus


def k_sample(model,df,k):
    a=0
    b=0
    c=0
    d=0
    node=0
    n=int(len(df.index) / k)
    for i in range(n):
        test = df.index.values[i * k:i * k + k]
        train = np.hstack([df.index.values[:i * k], df.index.values[i * k + k:]])
        model.fit(df.iloc[train, :-1], df.iloc[train, -1])
        y = model.predict(df.iloc[test, :-1])
        a+=accuracy_score(df.iloc[test, -1], y)
        b+=precision_score(df.iloc[test, -1], y)
        c+=recall_score(df.iloc[test, -1], y)
        d+=f1_score(df.iloc[test, -1], y)
        node+=model.tree_.node_count
    dot_data = export_graphviz(model, out_file=None,
                               feature_names=['Q2','Q3','Q4','Q7'],
                               class_names=['1','0'],
                               filled=True, rounded=True,
                               special_characters=True)
    l=np.asarray([a,b,c,d])
    return [l/n,node/n]

def model_test(i,j,k,df1):
    dt=DecisionTreeClassifier(max_depth=i,min_samples_split=j,min_samples_leaf=k)
    return k_sample(dt,df1,50)

data=pd.read_excel('data529.xlsx')
data['finish_time']=[i.split('分')[0]+i.split('分')[-1][:-1] for i in data['finish_time']]
data['finish_time']=data['finish_time'].astype('int')
data.drop(data.index[data['finish_time']<70 ], inplace=True)
dd=data.loc[data[data['Q12']==2].index,['Q1','Q2','Q3','Q8','Q9','Q18|R1','Q18|R2','Q18|R3','Q18|R4','Q21|R2']]
dd['Q21']=((dd['Q21|R2']-2.5)/2+0.5).astype('int')
excel_name=pd.ExcelWriter('dd1.xlsx')
dd.to_excel(excel_name)
excel_name.close()
data.drop(data.index[data['Q10']==3],inplace=True)
print(len(data[data['Q10']!=3]))
df0=data[['Q2','Q3','Q4','Q7','Q11|6']].copy()
df0.index=np.arange(len(df0.index))
print(model_test(2,13,13,df0))