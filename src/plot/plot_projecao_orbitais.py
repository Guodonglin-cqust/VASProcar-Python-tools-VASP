
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================= Plotando as Projecoes =================")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('output'):
   dir_output = 'output/Orbitais/'
else:
   dir_output = ''
#----------------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#======================================================================

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

orbitais = np.loadtxt(dir_output + 'Orbitais.dat') 
orbitais.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------

if (lorbit == 10): loop = 1          
if (lorbit >= 11): loop = 3

rx = orbitais[:,0]
ry = orbitais[:,1]

#===========================================================================
# Plot as Projeções dos Orbitais de forma individual: ======================
#===========================================================================
    
for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================

    #-----------------------------------------------------------------------------------------------------------------------------------------------------------         
    # Notação do Matplotlib para o padrão RGB de cores: color = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------------------
    # red = [1.0, 0.0, 0.0]; green = [0.0, 1.0, 0.0]; blue = [0.0, 0.0, 1.0]; rosybrown = [0.737254902, 0.560784313, 0.560784313]; magenta = [1.0, 0.0, 1.0] ---           
    #-----------------------------------------------------------------------------------------------------------------------------------------------------------

    if (l == 1):
       S = orbitais[:,2]
       P = orbitais[:,3]
       D = orbitais[:,4]
       #----------------
       ax.scatter(rx, ry, s = S, color = [0.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = 'S')
       ax.scatter(rx, ry, s = P, color = [1.0, 0.0, 0.0], alpha = transp, edgecolors = 'none', label = 'P') 
       ax.scatter(rx, ry, s = D, color = [0.0, 1.0, 0.0], alpha = transp, edgecolors = 'none', label = 'D') 
       #----------------------
       file = 'Orbitais_S_P_D'       
       
    if (l == 2):
       Px = orbitais[:,5]
       Py = orbitais[:,6]
       Pz = orbitais[:,7]
       #-----------------
       ax.scatter(rx, ry, s = Px, color = [0.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = r'${P}_{x}$')
       ax.scatter(rx, ry, s = Py, color = [1.0, 0.0, 0.0], alpha = transp, edgecolors = 'none', label = r'${P}_{y}$')
       ax.scatter(rx, ry, s = Pz, color = [0.0, 1.0, 0.0], alpha = transp, edgecolors = 'none', label = r'${P}_{z}$')
       #------------------
       file = 'Orbitais_P'
       
    if (l == 3):
       Dxy = orbitais[:,8]
       Dyz = orbitais[:,9]
       Dz2 = orbitais[:,10]
       Dxz = orbitais[:,11]
       Dx2 = orbitais[:,12]
       #-------------------
       ax.scatter(rx, ry, s = Dxy, color = [0.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = r'${D}_{xy}$')
       ax.scatter(rx, ry, s = Dyz, color = [1.0, 0.0, 0.0], alpha = transp, edgecolors = 'none', label = r'${D}_{yz}$')
       ax.scatter(rx, ry, s = Dz2, color = [0.0, 1.0, 0.0], alpha = transp, edgecolors = 'none', label = r'${D}_{z^{2}}$')
       ax.scatter(rx, ry, s = Dxz, color = [0.737254902, 0.560784313, 0.560784313], alpha = transp, edgecolors = 'none', label = r'${D}_{xz}$')
       ax.scatter(rx, ry, s = Dx2, color = [1.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = r'${D}_{x^{2}}$')
       #------------------
       file = 'Orbitais_D'

    # Plot das Bandas =====================================================

    x = banda[:,0]

    for i in range (1,(nb+1)):
        y = banda[:,i]
        plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x[0], x[(n_procar*nk)-1]], [0.0, 0.0], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [energ_min, energ_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Rotulando pontos-k de interesse na estrutura de Bandas ==============

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)        
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((energ_min, energ_max))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    ax.legend(loc = "upper right", title = "")
    # ax.legend(loc = "best", title = "")

    if (save_png == 1): plt.savefig(dir_output + file + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '.eps', dpi = 600)

    # plt.show()



#==============================================================================
# Plot com as Projeções dos Orbitais mescladas via soma do padrão de cores: ===
#==============================================================================

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------
   
color_SPD  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
color_P    = [0]*n_procar*nk*nb  # color_P[n_procar*nk*nb]
color_D    = [0]*n_procar*nk*nb  # color_D[n_procar*nk*nb]

passo = n_procar*nk*nb

#===========================================================================

color_rbg = open(dir_output + 'color_rgb.dat', "r")

for i in range(passo):
    VTemp = color_rbg.readline().split()
    color_SPD[i] = [VTemp[0], VTemp[1], VTemp[2]]
    if (lorbit >= 11): color_P[i] = [VTemp[3], VTemp[4], VTemp[5]]
    if (lorbit >= 11): color_D[i] = [VTemp[6], VTemp[7], VTemp[8]]

#----------------
color_rbg.close()
#----------------

#===========================================================================
    
for l in range (1,(loop+1)):     # Loop para a analise das Projecoes

    fig, ax = plt.subplots()

    # Plot das Projeções ===================================================   

    if (l == 1):
       peso = S + P + D
       file = 'Orbitais_S_P_D'
       #----------------------
       ax.scatter(rx, ry, s = peso, c = color_SPD, alpha = transp, edgecolors = 'none')            
       
    if (l == 2):
       peso = Px + Py + Pz
       file = 'Orbitais_P'
       #------------------
       ax.scatter(rx, ry, s = peso, c = color_P, alpha = transp, edgecolors = 'none')
       
    if (l == 3):
       peso = Dxy + Dyz + Dz2 + Dxz + Dx2
       file = 'Orbitais_D'
       #------------------
       ax.scatter(rx, ry, s = peso, c = color_D, alpha = transp, edgecolors = 'none')      

    # Plot das Bandas =====================================================

    for i in range (1,(nb+1)):
        y = banda[:,i]
        plt.plot(x, y, color = 'black', linestyle = '-', linewidth = 0.25, alpha = 0.3)

    # Destacando a energia de Fermi na estrutura de Bandas ================

    plt.plot([x[0], x[(n_procar*nk)-1]], [0.0, 0.0], color = 'red', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Destacando pontos-k de interesse na estrutura de Bandas =============

    if (dest_k > 0): 
       for j in range (len(dest_pk)):
           plt.plot([dest_pk[j], dest_pk[j]], [energ_min, energ_max], color = 'gray', linestyle = '-', linewidth = 0.1, alpha = 1.0)

    # Rotulando pontos-k de interesse na estrutura de Bandas ==============

    if (dest_k == 2): plt.xticks(dest_pk,label_pk)        
    
    #======================================================================

    plt.xlim((x[0], x[(n_procar*nk)-1]))
    plt.ylim((energ_min, energ_max))

    if (Dimensao == 1 and dest_k != 2): plt.xlabel('$2{\pi}/{a}$')
    if (Dimensao == 2 and dest_k != 2): plt.xlabel('${\AA}^{-1}$')
    if (Dimensao == 3 and dest_k != 2): plt.xlabel('${nm}^{-1}$')

    plt.ylabel('$E-E_{f}$ (eV)')

    ax.set_box_aspect(1.25/1)
    # ax.legend(loc = "upper right", title = "")
    # ax.legend(loc = "best", title = "")

    if (save_png == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.png', dpi = 600)
    if (save_pdf == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.pdf', dpi = 600)
    if (save_eps == 1): plt.savefig(dir_output + file + '_[sum_colors]' + '.eps', dpi = 600)

    # plt.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
   print("= gerados na pasta output\Orbitais =========================")   
   print("= arquivos .agr (via Grace) ou Orbitais.py =================")
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------
