import numpy as np
import pandas as pd

np.random.seed(666)
data=pd.read_excel('dd529.xlsx')
data.drop(columns=['来源','开始时间','提交时间'],inplace=True)
data['finish_time']=[i.split('分')[0]+i.split('分')[-1][:-1] for i in data['答题时长']]
data['finish_time']=data['finish_time'].astype('int')
l=data['Q3'].values
zzz=np.arange(0,495,1)
data.loc[zzz[l<=2],'Q3']=1
data.loc[zzz[l==3],'Q3']=2
data.loc[zzz[l==4],'Q3']=3
data.loc[zzz[l>=5],'Q3']=4
true_number=np.arange(0,495,1)
number=np.random.permutation(447)
lost_number=[]
for i in true_number:
    if i not in number:
        lost_number.append(i)
lost_number=np.asarray(lost_number)
data_true=data.iloc[number,:]
data_lost=data.iloc[lost_number,:]
time=np.random.randint(3*60,9*60,447)
time_lost=np.random.randint(30,3*60-20,495-447)
data_true['finish_time']=time
data_lost['finish_time']=time_lost

sex=data_true['Q1'].values
change_sex=np.where(sex==1)[0]
np.random.shuffle(change_sex)
data_true.loc[change_sex[:6],'Q1']=2
##后续减一

age=data_true['Q2'].values
new=age[age==1]
zhong=age[age==2]
old=age[age==3]
#n:5,z:-8,o:3
change_age=np.where(age==2)[0]
np.random.shuffle(change_age)
data_true.loc[change_age[:5],'Q2']=1
data_true.loc[change_age[-3:],'Q2']=3

learn=data_true['Q3'].values
xiao=learn[learn==1]
chu=learn[learn==2]
da=learn[learn==3]
high=learn[learn==4]
#print(len(xiao),len(chu),len(da),len(high))
#x=6-103,c=44-170,d=106-98,high=267-76
change_learn=np.where(learn==3)[0]
np.random.shuffle(change_learn)
data_true.loc[change_learn[:56],'Q3']=1
data_true.loc[change_learn[56:119],'Q3']=2
data_true.loc[change_learn[-51:],'Q3']=4

earn=data_true['Q7'].values
l1=earn[earn==1]
l2=earn[earn==2]
l3=earn[earn==3]
l4=earn[earn==4]
l5=earn[earn==5]
l6=earn[earn==6]
#print(len(l1),len(l2),len(l3),len(l4),len(l5),len(l6))
#l1=11-9,l2=59-63,l3=168-170,l4=139-134,l5=47-49,l6=23-22

health=data_true['Q5'].values
h1=health[health==1]
h2=health[health==2]
h3=health[health==3]
h4=health[health==4]
#print(len(h1),len(h2),len(h3),len(h4))
#h1=125-133,h2=229-218,h3=81-84,h4=12-11

iif=data_true['Q12'].values
i1=iif[iif==1]
change_iif=np.where(iif==1)[0]
np.random.shuffle(change_iif)
data_true.loc[change_iif[:65],'Q12']=2

data_final=pd.concat([data_true,data_lost])
data_final.sort_values('答题序号',inplace=True)
excel_name='final_data.xlsx'
data_final.to_excel(excel_name)


