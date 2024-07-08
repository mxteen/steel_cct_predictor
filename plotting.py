import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
from utils import roundup
from transformations import Ae3_Calc, Ae1_Calc
# import seaborn as sns

# sns.set(style="ticks", palette="pastel")
# sns.set_context("notebook", font_scale=1.5, rc={"lines.linewidth": 2.5})

def CCT_Plotter(Ts, comp, rates):
    colors = {'f':'steelblue','p':'mediumorchid','b':'chocolate','bu':'sandybrown','bl':'chocolate','m':'mediumseagreen'}

    plt.figure(figsize=(12,8))

    Ae3i, Ae1i = Ae3_Calc(comp), Ae1_Calc(comp)

    maxX = roundup(Ae3_Calc(comp)/min(rates))

    plt.plot([0.1,maxX],[Ae3i,Ae3i], color = 'k', linestyle = '--', linewidth = 1.5)
    plt.text(maxX*0.1, Ae3i-10, '$Ae_3$='+str(Ae3i)+'\N{DEGREE SIGN}C', bbox={'facecolor': 'white'},fontsize=14)
    plt.plot([0.1,maxX],[Ae1i,Ae1i], color = 'dimgray', linestyle = '--', linewidth = 1.5)
    plt.text(maxX*0.2, Ae1i-10, '$Ae_1$='+str(Ae1i)+'\N{DEGREE SIGN}C', bbox={'facecolor': 'white'},fontsize=14)

    dT = 1
    temp = np.linspace(Ae3i,0,(Ae3i+1)*int(dT**(-1)))

    for r in rates:
        times = []
        for T in temp[1:]:
            times.append((Ae3i-T)/r)
        if r in [0.01,0.1,1,10,100]:
            plt.plot(times,temp[1:],color='red',linewidth=0.75)
            plt.text((Ae3i-250)/r, 25, str(r)+'\N{DEGREE SIGN}C/s', bbox={'facecolor': 'white'},fontsize=12)
        else:
            plt.plot(times,temp[1:],color='red',linewidth=0.25)

        for phase in ['f','p','bu','bl','m']:
            for T in Ts[r][phase]:
                plt.scatter((Ae3i-T)/r,T,color=colors[phase],marker='o')

    for phase in ['f','p','b','m']:
        ti,Ti = [],[]
        for r in rates:
            try:
                ti.append((Ae3i-Ts[r][phase][0])/r)
                Ti.append(Ts[r][phase][0])
            except IndexError:
                ti.append(np.nan)
                Ti.append(np.nan)
        plt.plot(ti,Ti,color=colors[phase])#,marker='o')

    handle = []
    for phase in ['f','p','bu','bl','m']:
        handle.append(mpatches.Patch(color=colors[phase],label=phase))
    plt.legend(handles=handle,loc='lower left',
              fancybox=True, shadow=True, ncol=1, prop={'size': 16})

    plt.xlabel('Time (s)', fontsize = 18)
    plt.ylabel('Temperature (\N{DEGREE SIGN}C)', fontsize=18)
    plt.xscale('log')
    plt.xlim(1,maxX)
    plt.ylim(0,Ae3i+25)

    plt.tick_params(axis='x', labelsize=16)
    plt.tick_params(axis='y', labelsize=16)
