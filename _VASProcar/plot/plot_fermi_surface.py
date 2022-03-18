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
print("============ Plotando a Superficie de Fermi: ============")

#----------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado
#----------------------------------------------------------------
if os.path.isdir('saida'):
   Diretorio_saida = 'saida/Fermi_Surface/'
else:
   Diretorio_saida = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

sfermi = np.loadtxt(Diretorio_saida + 'Fermi_Surface.dat') 
sfermi.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")
print(". Pode demorar um pouco .")
print(".........................")

if (Plano_k == 1):     # Plano (kx,ky) ou (k1,k2)     
   eixo1 = sfermi[:,0]
   eixo2 = sfermi[:,1]
if (Plano_k == 2):     # Plano (kx,kz) ou (k1,k3)     
   eixo1 = sfermi[:,0]
   eixo2 = sfermi[:,2]
if (Plano_k == 3):     # Plano (ky,kz) ou (k2,k3)    
   eixo1 = sfermi[:,1]
   eixo2 = sfermi[:,2]

# Create meshgrid for x,y ------------------------------------------------

xi = np.linspace(min(eixo1), max(eixo1), n_d)
yi = np.linspace(min(eixo2), max(eixo2), n_d)
x_grid, y_grid = np.meshgrid(xi,yi)

#-------------------------------------------------------------------------

font = {'family' : 'arial',  
        'color'  : 'black',  
        'weight' : 'normal',  
        'size'   : 10,  
        }

#-------------------------------------------------------------------------

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

   

#=========================================================================
# Plot 2D das Curvas de Nível: ===========================================
#=========================================================================

levels = [0.0]*1

for i in range(n_energ):

    fig, ax = plt.subplots()

    cmap_black = (mpl.colors.ListedColormap(['black', 'black']))

    for j in range(Band_i,(Band_f+1)):
        #----------------------------------------------------------------------------
        energ  = sfermi[:,(j + 2)]
        levels[0] = E[i]
        #----------------------------------------------------------------------------
        if (min(energ) < E[i] and max(energ) > E[i]):
           # Create meshgrid for z --------------------------------------------------
           z_grid = griddata((eixo1,eixo2), energ, (x_grid,y_grid), method = 'cubic')
           #------------------------------------------------------------------------- 
           plt.contour(x_grid, y_grid, z_grid, levels, linestyles = '-', cmap = cmap_black, alpha = 1.0, antialiased = True)

    plt.xlabel(c1, fontdict = font)
    plt.ylabel(c2, fontdict = font)

    ax.set_box_aspect(1.0/1)

    if (E[i] < 0.0): c_energ = str(E[i])
    if (E[i] > 0.0): c_energ = '+' + str(E[i])

    if (save_png == 1): plt.savefig(Diretorio_saida + 'Fermi_Surface_[' + c_energ + '].png', dpi = 600, pad_inches = 0)
    if (save_pdf == 1): plt.savefig(Diretorio_saida + 'Fermi_Surface_[' + c_energ + '].pdf', dpi = 600, pad_inches = 0)
    if (save_eps == 1): plt.savefig(Diretorio_saida + 'Fermi_Surface_[' + c_energ + '].eps', dpi = 600, pad_inches = 0)

    # plt.show()

#======================================================================
   
if (Diretorio_saida != ''):
   print(" ")
   print("=========================================================")
   print("= Edite os Plots por meio do arquivo Fermi_Surface.py ===")
   print("= gerado na pasta saida\Fermi_Surface ===================")   
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
