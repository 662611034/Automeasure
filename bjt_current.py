# from InstrLib import *
# power = N6705("GPIB2::0::INSTR")

vb_start = 0
vb_stop = 4
vb_step = 0.8

vc_start = 0
vc_stop = 4
vc_step = 0.1

result = [['VC']]

vb = vb_start
while vb < vb_stop + vb_step:
    result[0].append(f'I_VB={round(vb, 1)}V')
    vb += vb_step

vc = vc_start
while vc < vc_stop + vc_step:
    result.append([round(vc, 1)])
    vc += vc_step

vb = vb_start
while vb < vb_stop + vb_step:
    i = 1
    vc = vc_start
    while vc < vc_stop + vc_step:
        # power.setVolt(vb, 1)
        # power.setVolt(vc, 2)
        # curr = power.readCurr(2)
        curr = round(10*vb*vc, 1)
        result[i].append(curr)
        i +=1
        vc += vc_step
    vb += vb_step

with open('result.txt', 'w') as f:
    for i in range(len(result)):
        for j in range(len(result[i])):
            f.write(str(result[i][j])+' ')
        f.write('\n')

###############################################

# from InstrLib import *
import pandas as pd
# power = N6705("GPIB2::0::INSTR")

vb_start = 0
vb_stop = 4
vb_step = 0.8

vc_start = 0
vc_stop = 4
vc_step = 0.1

result = pd.DataFrame()

list_temp = []

vc = vc_start
while vc < vc_stop + vc_step:
    list_temp.append([round(vc, 1)])
    vc += vc_step
result['VC'] = list_temp
result = result.set_index('VC')

vb = vb_start
while vb < vb_stop + vb_step:
    vc = vc_start
    list_temp=[]
    while vc < vc_stop + vc_step:
        # power.setVolt(vb, 1)
        # power.setVolt(vc, 2)
        # curr = power.readCurr(2)
        curr = round(10*vb*vc, 1)
        list_temp.append(curr)
        vc += vc_step
    result[f'VB={round(vb, 1)}V'] = list_temp
    vb += vb_step

result.to_csv('result.csv')