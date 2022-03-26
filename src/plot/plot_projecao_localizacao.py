
import os
import matplotlib.pyplot as plt
import numpy as np

print(" ")
print("================= Plotando as Projecoes =================")

#----------------------------------------------------------------------
# Teste para saber qual diretorio deve ser corretamente informado -----
#----------------------------------------------------------------------
if os.path.isdir('output'):
   dir_output = 'output/Localizacao/'
else:
   dir_output = ''
#-----------------

#======================================================================
#======================================================================
# Estrutura do arquivo para Plot via Matplotlib =======================
#======================================================================
#====================================================================== 

banda = np.loadtxt(dir_output + 'Bandas.dat') 
banda.shape

localizacao = np.loadtxt(dir_output + 'Localizacao.dat') 
localizacao.shape

print(" ")
print(".........................")
print("... Espere um momento ...")
print(".........................")  



#===========================================================================
# Plot as Projeções das Regiões de forma individual: =======================
#===========================================================================

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

rx = localizacao[:,0]
ry = localizacao[:,1] 
ra = localizacao[:,2]
rb = localizacao[:,3]
rc = localizacao[:,4]
rd = localizacao[:,5]
re = localizacao[:,6]

#-----------------------------------------------------------------------------------------------------------------------------------------------------------         
# Notação do Matplotlib para o padrão RGB de cores: color = [red, green, blue] com cada componente variando de 0.0 a 1.0 -----------------------------------
# red = [1.0, 0.0, 0.0]; green = [0.0, 1.0, 0.0]; blue = [0.0, 0.0, 1.0]; rosybrown = [0.737254902, 0.560784313, 0.560784313]; magenta = [1.0, 0.0, 1.0] ---           
#-----------------------------------------------------------------------------------------------------------------------------------------------------------

if (num_A == 1): ax.scatter(rx, ry, s = ra, color = [0.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = 'A')
if (num_B == 1): ax.scatter(rx, ry, s = rb, color = [1.0, 0.0, 0.0], alpha = transp, edgecolors = 'none', label = 'B')
if (num_C == 1): ax.scatter(rx, ry, s = rc, color = [0.0, 1.0, 0.0], alpha = transp, edgecolors = 'none', label = 'C')
if (num_D == 1): ax.scatter(rx, ry, s = rd, color = [0.737254902, 0.560784313, 0.560784313], alpha = transp, edgecolors = 'none', label = 'D')
if (num_E == 1): ax.scatter(rx, ry, s = re, color = [1.0, 0.0, 1.0], alpha = transp, edgecolors = 'none', label = 'E')

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

if (save_png == 1): plt.savefig(dir_output + 'Localizacao_estados.png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Localizacao_estados.pdf', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Localizacao_estados.eps', dpi = 600)

# plt.show()



#==============================================================================
# Plot com as Projeções das Regiões mescladas via soma do padrão de cores: ====
#==============================================================================

#----------------------------------------------------------------------
# Inicialização de Variaveis, Vetores e Matrizes a serem utilizadas ---
#----------------------------------------------------------------------
   
color  = [0]*n_procar*nk*nb  # color_SPD[n_procar*nk*nb]
passo = n_procar*nk*nb

#===========================================================================

color_rbg = open(dir_output + 'color_rgb.dat', "r")

for i in range(passo):
    VTemp = color_rbg.readline().split()
    color[i] = [VTemp[0], VTemp[1], VTemp[2]]

#----------------
color_rbg.close()
#----------------

#=======================================================================

fig, ax = plt.subplots()

# Plot das Projeções ===================================================

peso = ra + rb + rc + rd + re

ax.scatter(rx, ry, s = peso, c = color, alpha = transp, edgecolors = 'none')

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
# ax.legend(loc = "upper right", title = "")
# ax.legend(loc = "best", title = "")

if (save_png == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].png', dpi = 600)
if (save_pdf == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].pdf', dpi = 600)
if (save_eps == 1): plt.savefig(dir_output + 'Localizacao_estados_[sum_colors].eps', dpi = 600)

# plt.show()

#======================================================================

if (dir_output != ''):
   print(" ")
   print("============================================================")
   print("= Edite o Plot das projecoes por meio dos seguintes arquivos")
   print("= gerados na pasta output\Localizacao ======================")   
   print("= arquivos .agr (via Grace) ou Localizacao.py ==============")
   print("============================================================")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------