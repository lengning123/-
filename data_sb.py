import numpy as np
import pandas as pd

data=pd.read_excel('data529.xlsx')
data['finish_time']=[i.split('分')[0]+i.split('分')[-1][:-1] for i in data['finish_time']]
data['finish_time']=data['finish_time'].astype('int')
data.drop(data.index[data['finish_time']<35 ], inplace=True)

print('10:')
print(data['Q10'].value_counts())
print(' ')
print('12:')
print(data['Q12'].value_counts())
print(' ')
print('14:')
label='Q14|1	Q14|3	Q14|4	Q14|5	Q14|7	Q14|8	Q14|9	Q14|10	Q14|11	Q14|12	Q14|13	Q14|15'
label=label.split(' ')[0]
Q14_label=label.split('\t')
a=[]
for i in Q14_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a=pd.DataFrame(data=a,index=Q14_label)
df_a['per']=a/a.sum()
print(df_a)
print(' ')

print('15:')
label='Q15|1	Q15|2	Q15|3	Q15|4	Q15|5	Q15|6	Q15|7	Q15|8	Q15|9	Q15|10	Q15|11	Q15|12	Q15|13	Q15|14	Q15|15	Q15|16	Q15|18'
label=label.split(' ')[0]
Q15_label=label.split('\t')
a=[]
for i in Q15_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a1=pd.DataFrame(data=a,index=Q15_label)
df_a1['per']=a/a.sum()
print(df_a1)
print(' ')

print('13:')
label='Q13|1	Q13|2	Q13|3	Q13|4	Q13|5	Q13|6	Q13|7	Q13|8	Q13|10'
label=label.split(' ')[0]
Q13_label=label.split('\t')
a=[]
for i in Q13_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a2=pd.DataFrame(data=a,index=Q13_label)
df_a2['per']=a/a.sum()
print(df_a2)
print(' ')

print('21:')
label='Q23|1	Q23|2	Q23|3	Q23|4	Q23|5	Q23|6	Q23|7'
label=label.split(' ')[0]
Q21_label=label.split('\t')
a=[]
for i in Q21_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a4=pd.DataFrame(data=a,index=Q21_label)
df_a4['per']=a/a.sum()
df_a4.loc['12',:]=df_a4.iloc[[0,1],:].sum(axis=0)
df_a4.loc['45',:]=df_a4.iloc[[2,3,4],:].sum(axis=0)
print(df_a4)
print(' ')

print('22:')
label='Q22|1	Q22|2	Q22|3	Q22|4	Q22|5	Q22|6	Q22|7	Q22|8	Q22|9'
label=label.split(' ')[0]
Q22_label=label.split('\t')
a=[]
for i in Q22_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a5=pd.DataFrame(data=a,index=Q22_label)
df_a5['per']=a/a.sum()
print(df_a5)
print(' ')

data31=data[Q22_label].groupby(data['Q2']).agg('sum')
m=data31.sum(axis=1)
for i in range(1,4):
    data31.loc[i,:]=data31.loc[i,:]/m[i]
excel=pd.ExcelWriter('22.xlsx')
data31.to_excel(excel,sheet_name='32')

data35=data[Q22_label].groupby(data['Q5']).agg('sum')
m=data35.sum(axis=1)
for i in data35.index:
    data35.loc[i,:]=data35.loc[i,:]/m[i]
data35.to_excel(excel,sheet_name='35')

data37=data[Q22_label].groupby(data['Q7']).agg('sum')
m=data37.sum(axis=1)
for i in data37.index:
    data37.loc[i,:]=data37.loc[i,:]/m[i]
data37.to_excel(excel,sheet_name='37')
excel.close()

print('23:')
label='Q23|1	Q23|2	Q23|3	Q23|4	Q23|5	Q23|6	Q23|7'
label=label.split(' ')[0]
Q23_label=label.split('\t')
a=[]
for i in Q23_label:
    a.append(len(data[data[i]==1].index))
a=np.array(a)
df_a3=pd.DataFrame(data=a,index=Q23_label)
df_a3['per']=a/a.sum()
print(df_a3)
print(' ')

ddf=pd.read_excel('data111.xlsx')
ddf['Q21']=((ddf['Q21|R2']-2.5)/2+0.5).astype('int')
excel_name=pd.ExcelWriter('ddf.xlsx')
ddf.to_excel(ddf)
excel_name.close()