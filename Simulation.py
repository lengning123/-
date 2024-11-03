import numpy as np

rho = 1.08
m = 176.3*1000
Fq_max = 310*1000
Fz_max = 260*1000
Fz_machine = 760*1000
v0 = 0
a0 = 0
vmax = 100/3.6
d0 = 5144.7
alpha = []
g = 9.8
i = []
dt = 0.01


def f(v):
     f=2.0895+0.0098*v+0.006*v*v
     return f*1000

def Fq(v):
    if v <= 10:
        return Fq_max / 1000*0.9
    elif 10 < v and v <= 40:
        fq=Fq_max / 1000 * 10 / v *0.9
        return fq
    else:
        print("v to Fq error")

def Fz(v):
    if v <= 17:
        return Fz_max*0.6 / 1000
    elif 17 < v and v <= 40:
        fq=Fz_max / 1000 * 17 / v *0.6
        return fq
    else:
        print("v to Fz error")

def V(vi,F,ii):
    v = (F-f(v0)-m*g*ii)/(1+rho)/m*dt+vi
    return v

def count_t(v,v0):
    v_list=[v]
    for i in range(10000):
        Fi = Fz_machine + Fz(v_list[-1])
        vi= (-Fi-f(v_list[-1])-m*g*i)/(1+rho)/m*dt+v_list[-1]
        v_list.append(vi)
        if vi<=v0:
            break
    return (len(v_list)-1)*dt


def xunhang(v_set,vlimit_list,i_list,d_list):
    v_list=[0]
    w_list=[0]
    distance_list=[0]
    vlimit_list.append(0)
    n=0
    vi_max=v_set
    point=0
    w_change=0
    for i in range(1,10000):
        for j in range(len(d_list)):
            if j+1 <= len(d_list)-1:
                if d_list[j]<= distance_list[-1] < d_list[j+1]:
                    point = j
            else:
                if d_list[j-1] <= distance_list[-1]:
                    point = j
        vi_max = min(v_set,vlimit_list[point])
        #加速
        if v_list[-1]<=vi_max:
            vi=V(v_list[-1],Fq(v_list[-1]),i_list[point])
            di=v_list[-1]*dt
            Fi=Fq(v_list[-1])
            wi=Fi*di
        #匀速
        elif v_list[-1] == vi_max:
            vi=v_list[-1]
            di=vi*dt
            Fi=f(vi)+m*g*i_list[point]
            wi=Fi*di
        #减速
        if w_list[point]<w_change:
            di=v_list[-1]
        elif v_list[-1]>vlimit_list[point+1]:
            Fi=Fz_machine+Fz(v_list[-1])
            tmin=count_t(v_list[-1],vlimit_list[point+1])
            p=min(point+1,len(d_list)-1)
            t = (d_list[p]-distance_list[-1])/v_list[-1]
            w_change=v_list[-1]*(t-tmin)+distance_list[-1]
            Fi = Fz_machine + Fz(v_list[-1])
            vi = (-Fi - f(v_list[-1]) - m * g * i) / (1 + rho) / m * dt + v_list[-1]
            di=v_list[-1]*dt
            wi = Fi * di
        v_list.append(vi)
        distance_list.append(di + distance_list[-1])
        w_list.append(wi)
        if v_list[-1]<=0:
            break
    return v_list,distance_list,w_list


