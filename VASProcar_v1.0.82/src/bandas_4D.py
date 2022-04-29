
def execute_python_file(filename: str):
   return exec(open(main_dir + str(filename)).read(), globals())

#--------------------------------------------------------------------
# Verificando se a pasta "Plot_4D" existe, se não existe ela é criada
#--------------------------------------------------------------------
if os.path.isdir(dir_files + '/output/Plot_4D'):
   0 == 0
else:
   os.mkdir(dir_files + '/output/Plot_4D')
#----------------------------

#======================================================================
# Extraindo informações dos arquivos OUTCAR e CONTCAR =================
#======================================================================
execute_python_file(filename = 'informacoes.py')

#======================================================================
# Obtenção dos parâmetros de input ====================================
#======================================================================

print ("##############################################################")
print ("################## Plot 4D (ISOSUPERFICIE): ##################")
print ("##############################################################")
print (" ")

if (escolha == -1):

   print ("##############################################################") 
   print ("## Escolha a dimensao dos eixos-k no Plot: ================ ##")
   print ("##############################################################")
   print ("## [1] (kx,ky,kz) em unidades de 2pi/Param. =============== ##")
   print ("## [2] (kx,ky,kz) em unidades de 1/Angs. ================== ##")
   print ("## [3] (kx,ky,kz) em unidades de 1/nm. ==================== ##")
   print ("## [4] (k1,k2,k3) Coord. Diretas: K = k1*B1 + k2*B2 + k3*B3 ##")   
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

   print ("##############################################################")
   print ("Quantas isosuperficies deseja obter no Plot: =================")
   print ("Dica: Utilize 15 (Quanto maior mais preciso e pesado) ========")
   print ("##############################################################") 
   n_iso = input (" "); n_iso = int(n_iso)
   print (" ")

   print ("##############################################################")
   print ("Qual a dimensao-D (DxDxD) do GRID de interpolacao? ===========")
   print ("Dica: Utilize 31 (Quanto maior mais preciso e pesado) ========")
   print ("##############################################################") 
   n_d = input (" "); n_d = int(n_d)
   print (" ")   

if (escolha == 1):
   Dimensao = 1
   n_iso = 15
   n_d = 31

print ("##############################################################")
print ("O que deseja analisar? =======================================")
print ("[1] Dispersao de energia 3D de uma banda especifica ==========")
print ("[2] Magnitude de separacao entre 2 bandas ====================")
print ("##############################################################") 
esc = input (" "); esc = int(esc)
print (" ")

if (esc == 1):
   print ("##############################################################")
   print ("Escolha a Banda a ser analisada: =============================")
   print ("##############################################################")
   Band = input (" "); Band = int(Band)
   print (" ")
   
   Band_1 = 0; Band_2 = 0

if (esc == 2):
   print ("##############################################################")
   print ("Escolha as duas Bandas a serem analisadas: ================== ")
   print ("Digite como no exemplo abaixo =============================== ")
   print ("--------------------------------------------------------------")
   print ("Banda_1 Banda_2: 8 9                                          ")
   print ("##############################################################") 
   print (" ")
   Band_1, Band_2 = input ("Banda_1 Banda_2: ").split()
   Band_1 = int(Band_1)
   Band_2 = int(Band_2)
   print (" ")
      
   Band = 0
 

#----------------------------------------------------------------------
# Extraindo os resultados do(s) arquivo(s) PROCAR ---------------------
#----------------------------------------------------------------------
execute_python_file(filename = 'procar.py')

#======================================================================
#======================================================================
# Gravando dados para o Plot 4D =======================================
#======================================================================
#======================================================================

#------------------------------------------------------------
plot4D = open(dir_files + '/output/Plot_4D/Plot_4d.dat', 'w')
#------------------------------------------------------------

for i in range (1,(n_procar+1)):
    for j in range (1,(nk+1)):
        if (Dimensao < 4):
           x = kx[i][j]
           y = ky[i][j]
           z = kz[i][j]          
        if (Dimensao == 4):
           x = kb1[i][j]
           y = kb2[i][j]
           z = kb3[i][j]
        if (esc == 1):    
           e = Energia[i][j][Band]
        if (esc == 2):    
           e = (Energia[i][j][Band_2] - Energia[i][j][Band_1])
           e = (e**2)**0.5 
        plot4D .write(f'{x} {y} {z} {e} \n')

#--------------
plot4D .close()
#--------------

#----------------------------------------------------------------------
#----------------------------------------------------------------------
# Copiando o codigo Plot_4D.py para o diretório de saida --------------
#----------------------------------------------------------------------
#----------------------------------------------------------------------

# Teste para saber se o arquivo Plot_4D.py já se encontra no diretorio de saida
try: f = open(dir_files + '/output/Plot_4D/Plot_4D.py'); f.close(); os.remove(dir_files + '/output/Plot_4D/Plot_4D.py')
except: 0 == 0
  
source = main_dir + '/plot/plot_bandas_4D_plotly.py'
destination = dir_files + '/output/Plot_4D/Plot_4D.py'
shutil.copyfile(source, destination)

#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------
# Inserindo parâmetros para que o código Plot_4D.py possa ser executado isoladamente ---
#---------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'r')
lines = file.readlines()
file.close()

linha = 8

lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '# Parâmetros para que o código possa ser executado isoladamente ====== \n')
linha += 1; lines.insert(linha, '#===================================================================== \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, f'n_iso = {n_iso}  # Número de isosuperficies \n')
linha += 1; lines.insert(linha, f'n_d = {n_d}  #  Dimensao-D (DxDxD) do GRID de interpolacao \n')
linha += 1; lines.insert(linha, f'Band = {Band}  #  Banda cuja dispersão de energia 3D sera analisada \n')
linha += 1; lines.insert(linha, f'Band_1 = {Band_1}  #  1º Banda do par, cuja magnitude de separacao sera analisada \n')
linha += 1; lines.insert(linha, f'Band_2 = {Band_2}  #  2º Banda do par, cuja magnitude de separacao sera analisada \n')
linha += 1; lines.insert(linha, f'Dimensao  = {Dimensao}  #  [1] (kx,ky,kz) em 2pi/Param.; [2] (kx,ky,kz) em 1/Angs.; [3] (kx,ky,kz) em 1/nm.; [4] (k1,k2,k3) \n')
linha += 1; lines.insert(linha, f'esc = {esc} \n')
linha += 1; lines.insert(linha, '\n')
linha += 1; lines.insert(linha, '#===================================================================== \n')

file = open(dir_files + '/output/Plot_4D/Plot_4D.py', 'w')
file.writelines(lines)
file.close()

#----------------------------------------------------------
exec(open(dir_files + '/output/Plot_4D/Plot_4D.py').read())
#----------------------------------------------------------
