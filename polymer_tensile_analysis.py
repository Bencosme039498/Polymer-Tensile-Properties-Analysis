# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 09:27:23 2022

@author: Juan A. BENCOSME
"""

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 
from mpl_toolkits.axes_grid1 import host_subplot
import mpl_toolkits.axisartist as AA



data = pd.read_excel ("polymer_tensile_data.xlsx",sheet_name = "Sheet1")

x1 = data["PVA"]
y1 = data["E"]
y2 = data["MY"]
y3 = data["D"]
y_error = data["E-1"]
y_error1 = data["MY-1"]
y_error2 = data["D-1"]
fig = plt.figure (figsize = (8,8), dpi = 2500); 

fig, ax1 = plt.subplots();

line1 = ax1. plot(x1,y3, color = 'blue', label = 'Déformation... (%)', marker = '>', markersize = 8, linestyle='--')
ax1.errorbar(x1, y3, yerr = y_error2,color = 'blue', linestyle='--')


ax2 = ax1.twinx()
line2 = ax2.plot(x1,y2,color = 'crimson', label = 'Module de Young (MPa)',marker = '>',  markersize = 8, linestyle='-.') 
ax2.errorbar(x1, y2, yerr = y_error1,color = 'crimson', linestyle='-.' )



# ax2.tick_params(axis = 'y', labelcolor=color2)
# ax2.spines ['left'].set_color(color1)
# ax2.spines ['left'].set_color(color2)
# ax2.spines ['left'].set_position(('outward',60))

ax3 = ax1.twinx()
line3 = ax3.plot(x1,y1, color = 'green', label = 'Résistance... (MPa)',  marker = '>', markersize = 8,linestyle=':'  ) 
ax3.errorbar(x1, y1, yerr = y_error,color = 'green', linestyle=':' )
ax3.spines ['right'].set_position(('outward',60))


ax1.tick_params(axis = 'y', labelcolor='blue')
ax2.tick_params(axis = 'y', labelcolor='crimson')
ax3.tick_params(axis = 'y', labelcolor='green')


ax1.set_ylabel ('Déformation à la rupture(%)', color = 'blue')
ax2.set_ylabel ('Module de Young (MPa)', color = 'crimson')
ax3.set_ylabel ('Résistance à la rupture (MPa)', color = 'green')

plt.xticks([0,10,20,30,40])

ax1.set_xlabel("Liquide Ionique dans le PVA (%)")

lines = line1 + line2 + line3 

labels = [l.get_label() for l in lines]
ax1.legend(lines,labels, loc ="lower center", fontsize=8, shadow=0);

plt.savefig('GRAFICA DEFINITIVA TENSILE.svg', bbox_inches='tight', dpi=2500)
plt.show()

# ax3.plot(x1,y3, color = color2, label = 'Strain1', marker = 4, markersize = 8, linestyle='-.')
# offset = 0


# 	best
# 	upper right
# 	upper left
# 	lower left
# 	lower right
# 	right
# 	center left
# 	center right
# 	lower center
# 	upper center
# 	center


# # ax1.legend(loc='best')

# ax1.set_xlabel ('Linear')




# host = host_subplot(111, axes_class=AA.Axes)
# plt.subplots_adjust(top=1.0, right=0.85)

# par1 = host.twinx()
# par2 = host.twinx()
# # par3 = host.twinx()

# offset = -25
# new_fixed_axis = par2.get_grid_helper().new_fixed_axis
# par2.axis["left"] = new_fixed_axis(loc="left",
#                                     axes=par2,
#                                     offset=(offset, 0))

# # offset = 0
# # new_fixed_axis = par1.get_grid_helper().new_fixed_axis
# # par1.axis["left"] = new_fixed_axis(loc="left",
# #                                     axes=par1,
# #                                     offset=(offset, 0))

# # offset = 0
# # new_fixed_axis = par3.get_grid_helper().new_fixed_axis
# # par3.axis["left"] = new_fixed_axis(loc="right",
# #                                     axes=par3,
# #                                     offset=(offset, 0))
# par1.axis["left"].toggle(all=True)
# # par2.axis["left"].toggle(all=True)
# host.set_xlim(0, 45)
# #
# # offset = -35
# # new_fixed_axis = par1.get_grid_helper().new_fixed_axis
# # par1.axis["left"] = new_fixed_axis(loc="left",
# #                                     axes=par1,
# #                                     offset=(offset, 0))


# # host.set_xlabel("Fraction Liquide-Ethane")
# # host.set_ylabel("Temperature (K)")
# # par1.set_ylabel("Fraction Vapeur-Ethane")
# # par2.set_ylabel("Fraction")


# # # par3.axis["left"].toggle(all=True)

# p1, = par1.plot(x1,y1,'b',label='Liquide',markersize = 10)
# p2, =par2.plot(x1,y3,'g',label='Liquide',markersize = 10)
# # p3, = par3.plot(x1,y3,'y--',label='Liquide',markersize = 10)
# # p3, = plt.plot(x1,y3,'y--',label='Liquide',markersize = 10)
# # par1.axis["right"].label.set_color(p1.get_color())
# # par2.axis["left"].label.set_color(p2.get_color())
