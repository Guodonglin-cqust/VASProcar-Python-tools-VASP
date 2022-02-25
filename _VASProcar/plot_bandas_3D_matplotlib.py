#########################################################################################
## VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ################
## Autores: #############################################################################
## =================================================================================== ##
## Augusto de Lelis Araujo - Federal University of Uberlandia (Uberlândia/MG - Brazil) ##
## e-mail: augusto-lelis@outlook.com                                                   ##
## =================================================================================== ##
## Renan da Paixão Maciel - Uppsala University (Uppsala/Sweden) #########################
## e-mail: renan.maciel@physics.uu.se                           #########################
#########################################################################################

import os
import numpy as np
import matplotlib as mpl
from matplotlib import cm
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
from mpl_toolkits.mplot3d.axes3d import Axes3D
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import matplotlib.colors as mcolors
from scipy.interpolate import griddata
import pandas as pd

print(" ")
print("========== Plotando as Bandas 3D (Matplotlib): ==========")

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Bandas_3D/'
else:
   Diretorio_saida = ''
#----------------------

#======================================================================
#======================================================================
# Gerando o arquivo para Plot 3D via Matplotlib =======================
#======================================================================
#======================================================================

banda = np.loadtxt(Diretorio_saida + 'Bandas_3D.dat') 
banda.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = banda[:,0]
   eixo2 = banda[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = banda[:,1]
   eixo2 = banda[:,2]

#----------------------------------------------------------------------

E = [0]*((Band_f - Band_i)+2)
number = 0
# E_min = +1000.0
# E_max = -1000.0

#----------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 10,  
        } 

fig = plt.figure()

# ax = fig.add_subplot(projection="3d")
ax = plt.axes(projection='3d')

# colormap = plt.cm.get_cmap('coolwarm')
# normalize = mcolors.Normalize(vmin = E_min, vmax = E_max)

for i in range (1,(Band_f - Band_i +2)):
    #-----------------------
    energ = banda[:,(i + 2)]
    #-----------------------
    if (tipo_plot == 0):
       ax.scatter(eixo1, eixo2, energ, s = 1.0, alpha = 0.9, antialiased = False)
    if (tipo_plot == 1):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       # ax.plot_trisurf(eixo1, eixo2, E[number], alpha = 0.9, cmap = colormap, norm = normalize, edgecolor='black', linewidth = 0.0, antialiased = False)
    if (tipo_plot == 2):
       ax.plot_trisurf(eixo1, eixo2, energ, alpha = 0.9, cmap = 'coolwarm', edgecolor='black', linewidth = 0.0, antialiased = False)
       ax.scatter(eixo1, eixo2, energ, s = 0.1, alpha = 0.25, color = 'gray', antialiased = False)

    # ax.contourf(X, Y, Z[i], zdir = 'z', alpha = 0.9, offset = #####, cmap = cmap1)

if (Dimensao == 1):
   cl = r' $(2{\pi}/{a})$'
if (Dimensao == 2):
   cl = r' $({\AA}^{-1})$'
if (Dimensao == 3):
   cl = r' $({nm}^{-1})$' 

if (Plano_k == 1 and Dimensao != 4):             # Plano (kx,ky)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{y}$' + cl
if (Plano_k == 2 and Dimensao != 4):             # Plano (kx,kz)      
   c1 = r'${k}_{x}$' + cl
   c2 = r'${k}_{z}$' + cl
if (Plano_k == 3 and Dimensao != 4):             # Plano (ky,kz)      
   c1 = r'${k}_{y}$' + cl
   c2 = r'${k}_{z}$' + cl

if (Plano_k == 1 and Dimensao == 4):             # Plano (k1,k2)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{2}$'
if (Plano_k == 2 and Dimensao == 4):             # Plano (k1,k3)      
   c1 = r'${k}_{1}$'
   c2 = r'${k}_{3}$'
if (Plano_k == 3 and Dimensao == 4):             # Plano (k2,k3)      
   c1 = r'${k}_{2}$'
   c2 = r'${k}_{3}$'

ax.set_xlabel(c1, fontdict = font)
ax.set_ylabel(c2, fontdict = font)
ax.set_zlabel(r'$E-{E}_{f}(eV)$', fontdict = font)

# ax.set_xlim((-5,5))
# ax.set_ylim((-5,5))
# ax.set_zlim((-5,5))

ax.view_init(elev = 5, azim = 45)
  
fig = plt.gcf()
fig.set_size_inches(8,6)

plt.savefig(Diretorio_saida + "Bandas_3d.png", dpi = 300, pad_inches = 0)
# plt.savefig(Diretorio_saida + "Bandas_3d.pdf", dpi = 300, pad_inches = 0)
# plt.savefig(Diretorio_saida + "Bandas_3d.eps"', dpi = 300, pad_inches = 0)

plt.show()

#======================================================================
   
print(" ")
print("=========================================================")
print("= Edite o Plot3D por meio dos seguintes arquivos gerados ")
print("= na pasta ""saida\Bandas_3D"" ==========================")   
print("= bandas_3D_matplotlib.py e bandas_3D_plotly.py =========")
print("=========================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

#######################################################################
#######################################################################
#######
####### FIM DO CÓDIGO #################################################
#######
#######################################################################
#######################################################################