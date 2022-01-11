##############################################################
# Versao 1.001 (10/01/2022) ##################################
########################## Autores: ##########################
# Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG) ########
# e-mail: augusto-lelis@outlook.com ##########################
# ---------------------------------------------------------- #
# Renan Maciel da Paixão - ????????????????????????????????? #
# e-mail: ?????????????????????.com ##########################
##############################################################

#---------------------------------------------
exec(open("_VASProcar/informacoes.py").read())
#---------------------------------------------
inform = open("saida/informacoes.txt", "a")
#------------------------------------------

if os.path.isdir("temp"):
   0 == 0
else:
   os.mkdir("temp")

#######################################################
############ Lendo o arquivo de input #################
#######################################################

sim_nao = ["nao"]*(ni + 1)             # Inicialização do vetor sim_nao

###########################################################################

if (leitura == 0):
   print ("##############################################################")
   print ("################### Projecao dos Orbitais ####################")
   print ("##############################################################") 
   print ("Escolha a dimensao do eixo-k: ================================")
   print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
   print ("Utilize 2 para k em unidades de 1/Angs. ======================")
   print ("Utilize 3 para k em unidades de 1/nm. ========================")
   print ("##############################################################")
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print(" ")

   print ("##############################################################")
   print ("Digite o peso/tamanho das esferas na projecao: ===============")
   print ("Digite um valor entre 0.0 e 1.0 ==============================")
   print ("##############################################################")
   peso_total = input (" "); peso_total = float(peso_total)
   print(" ")

   print ("##############################################################")
   print ("O que vc deseja Plotar/Analisar? =============================")
   print ("Digite 0 para analisar todos os ions da rede =================")
   print ("Digite 1 para analisar ions selecionados =====================")
   print ("==============================================================")
   esc = input (" "); esc = int(esc)

   if (esc == 1):
      print ("Especifique os ions selecionados em intervalos ===============")
      print ("Quantos intervalos de ions ira fornecer abaixo? ==============")
      print ("##############################################################")
      loop = input (" "); loop = int(loop)
      for i in range (1,(loop+1)):
          print (f'{i} intervalo: ==============================================')
          print ("Digite o ion inicial do intervalo ============================")
          loop_i = input (" "); loop_i = int(loop_i)
          print ("Digite o ion final do intervalo ==============================")
          loop_f = input (" "); loop_f = int(loop_f)
          if (loop_i > ni) or (loop_f > ni) or (loop_i < 0) or (loop_f < 0):
             print ("")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("   ERRO: Os valores de ions informados estao incorretos   ")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("")
          for i in range(loop_i, (loop_f + 1)):
             sim_nao[i] = "sim"

   print (" ")

###########################################################################

if (leitura == 1):
   #----------------------------------------------
   entrada = open("input/input_projecoes.txt", "r")
   #----------------------------------------------

   for i in range(6):
       VTemp = entrada.readline()
   Dimensao = int(VTemp)                          # Unidade de medida adotada no eixo-k (2pi/Param, 1/Angs ou 1/nm).

   for i in range(4):
       VTemp = entrada.readline()
   peso_total = float(VTemp)                      # Tamanho/peso das esferas nos graficos de projeções.

   for i in range(5):
       VTemp = entrada.readline()
   esc = int(VTemp)                               # Escolha se serão Plotados/Analisados todos os ions ou não, nas projeções.                                                   

   #-------------
   if (esc == 1):

      for i in range(4):
          VTemp = entrada.readline()
      loop = int(VTemp)

      VTemp = entrada.readline()
      VTemp = entrada.readline()

      for j in range(loop):

          VTemp = entrada.readline().split()
          loop_i = int(VTemp[0]); loop_f = int(VTemp[1])

          if (loop_i > ni) or (loop_f > ni):
             print ("")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("ERRO: Corrija o arquivo de entrada (ions_selecionados.txt)")
             print ("      existe mais atomos definidos do que na rede")
             print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
             print ("")       
       
          for i in range(loop_i, (loop_f + 1)):
              sim_nao[i] = "sim"

   #--------------
   entrada.close()
   #--------------

########################################################################### 

esc_b = 1                                      # Plotar todas as bandas (tanto com numeração par quanto com numeração ímpar) !!! REMOVER ESTA OPÇÃO DO CÓDIGO !!!
destacar_efermi = 1                            # Destacar o nível de fermi nos gráficos.
destacar_pontos_k = 1                          # Destacar pontos-k nos gráficos.
peso_inicial = 0.0                             # Menor tamanho de esfera nos gráficos de projeções.

#---------------------------
if (esc == 0) or (esc == 1):                   # Para esc = 0 ou 1, todas as Bandas e K_Points sao plotados.
   Band_i = 1
   Band_f = nb
   point_i = 1
   point_f = nk

#-------------       
if (esc == 0):                                 # Para esc = 0 ou 1, todos os ions sao analisados.
   ion_i = 1
   ion_f = ni                                                     

############## Criação de Arquivos temporários ###################

if (lorbit == 10):
   Orbital_S = open("temp/Temp_orb-S_Excluir.txt", "w")
   Orbital_P = open("temp/Temp_orb-P_Excluir.txt", "w")
   Orbital_D = open("temp/Temp_orb-D_Excluir.txt", "w")

if (lorbit > 10):
   Orbital_Px = open("temp/Temp_orb-Px_Excluir.txt", "w")
   Orbital_Py = open("temp/Temp_orb-Py_Excluir.txt", "w")
   Orbital_Pz = open("temp/Temp_orb-Pz_Excluir.txt", "w")
   Orbital_S  = open("temp/Temp_orb-S_Excluir.txt", "w")
   Orbital_P  = open("temp/Temp_orb-P_Excluir.txt", "w")
   Orbital_D  = open("temp/Temp_orb-D_Excluir.txt", "w")

#-----------------------------------------------------------------

# Band_antes   = (Band_i  - 1)       # Bandas que nao serao plotadas.
# Band_depois  = (Band_f  + 1)       # Bandas que nao serao plotadas.
# point_antes  = (point_i - 1)       # K_points que nao serao plotados.
# point_depois = (point_f + 1)       # K_points que nao serao plotados.
# ion_antes  = (ion_i - 1)       # ions que nao serao analisados.
# ion_depois = (ion_f + 1)       # ions que nao serao analisados.

#-----------------------------------------------------------------

#*****************************************************************
# Dimensao = 1 >> k em unidades de 2pi/Param com Param em Angs. **
# Dimensao = 2 >> k em unidades de 1/Angs. ***********************
# Dimensao = 3 >> K em unidades de 1/nm **************************
#*****************************************************************

if (Dimensao == 1):
   fator_zb = 1.0

if (Dimensao == 2):
   fator_zb = (2*3.1415926535897932384626433832795)/Parametro

if (Dimensao == 3):
   fator_zb = (10*2*3.1415926535897932384626433832795)/Parametro

B1x = B1x*fator_zb
B1y = B1y*fator_zb
B1z = B1z*fator_zb
B2x = B2x*fator_zb
B2y = B2y*fator_zb
B2z = B2z*fator_zb
B3x = B3x*fator_zb
B3y = B3y*fator_zb
B3z = B3z*fator_zb

#-----------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("*********** Pontos-k na Zona de Brillouin *********** \n")
inform.write("***************************************************** \n")
inform.write(" \n")
      
if (Dimensao == 1):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (2Pi/Param) \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (1/Angs.) \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas M1, M2 e M3          |   Separacao (1/nm) \n")

inform.write("         |          K =  M1*B1 + M2*B2 + M3*B3          | \n")
inform.write(" \n")

########################## Loop dos PROCAR #############################

wp = 0
n_point_k = 0
energ_max = -1000.0
energ_min = +1000.0

################# Inicialização de Vetores e Matrizes: #################
                                              
xx = [[0]*(nk+1) for i in range(n_procar+1)]
kx = [[0]*(nk+1) for i in range(n_procar+1)]
ky = [[0]*(nk+1) for i in range(n_procar+1)]
kz = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]    

for wp in range(1, (n_procar+1)):

    if (wp == 1) and (n_procar == 1):
       procar = open("PROCAR", "r")
    if (wp == 1) and (n_procar != 1):
       procar = open("PROCAR.1", "r")
    if (wp == 2):
       procar = open("PROCAR.2", "r")
    if (wp == 3):
       procar = open("PROCAR.3", "r")
    if (wp == 4):
       procar = open("PROCAR.4", "r")
    if (wp == 5):
       procar = open("PROCAR.5", "r")
    if (wp == 6):
       procar = open("PROCAR.6", "r")
    if (wp == 7):
       procar = open("PROCAR.7", "r")
    if (wp == 8):
       procar = open("PROCAR.8", "r")
    if (wp == 9):
       procar = open("PROCAR.9", "r")
    if (wp == 10):
       procar = open("PROCAR.10", "r")

    for i in range(3):
        VTemp = procar.readline()
      
######################### Loop dos Pontos_k ###########################
                                      
    for point_k in range(1, (nk+1)):                                  

#######################################################################

        if (n_procar == 1 and point_k == 1):
           print("Analisando o arquivo PROCAR)

        if (n_procar > 1 and point_k == 1):
           print("Analisando o arquivo PROCAR",wp)
                                                                      
        VTemp = procar.readline().split()                             # Observacao: No VASP k_b1, k_b2 e k_b3 correspondem as coordenadas diretas de cada ponto-k na ZB,                                                         
        k_b1 = float(VTemp[3])                                        # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X,
        k_b2 = float(VTemp[4])                                        # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        k_b3 = float(VTemp[5])                                        # em unidades de 2pi/Parametro.
        
        VTemp = procar.readline()

############### Distancia de separacao entre os pontos-k ##############

        Coord_X = ((k_b1*B1x) + (k_b2*B2x) + (k_b3*B3x))
        Coord_Y = ((k_b1*B1y) + (k_b2*B2y) + (k_b3*B3y))
        Coord_Z = ((k_b1*B1z) + (k_b2*B2z) + (k_b3*B3z))

        kx[wp][point_k] = Coord_X       
        ky[wp][point_k] = Coord_Y
        kz[wp][point_k] = Coord_Z   

        if (wp == 1) and (point_k == point_i):
           comp = 0.0
           xx[wp][point_k] = comp 

        if (wp != 1) or (point_k != point_i):
           delta_X = Coord_X_antes - Coord_X
           delta_Y = Coord_Y_antes - Coord_Y
           delta_Z = Coord_Z_antes - Coord_Z
           comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           comp = comp + comp_antes
           xx[wp][point_k] = comp

        # if (wp == 1) and (point_k == point_i):
           # comp = 0.0
           # xx[wp][point_k] = comp 

        # if (wp != 1) or (point_k != point_i):
           # delta_X = Coord_X_antes - Coord_X
           # delta_Y = Coord_Y_antes - Coord_Y
           # delta_Z = Coord_Z_antes - Coord_Z
           # comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           # comp = comp + comp_antes
           # xx[wp][point_k] = comp

        Coord_X_antes = Coord_X
        Coord_Y_antes = Coord_Y
        Coord_Z_antes = Coord_Z
        comp_antes = comp
        
        separacao[wp][point_k] = comp

        n_point_k = n_point_k + 1   

        inform.write(f'{n_point_k:>4}{k_b1:>19,.12f}{k_b2:>17,.12f}{k_b3:>17,.12f}{comp:>19,.14f} \n')

########################## Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            if (esc_b == 1):
               Band_nn = float(Band_n)                                # Converte a variavel inteira (Band_n) para o tipo real.
               criterio_2 = (Band_n/1.0)
               int_crit_2 = int(criterio_2)                           # Retorna a parte inteira do numero real (criterio_2).
               resto_crit_2 = (criterio_2 % 1.0)                      # Retorna a parte fracionaria do numero real (criterio_2).

            if (esc_b != 1):
               Band_nn = float(Band_n)                                # Converte a variavel inteira (Band_n) para o tipo real.
               criterio_2 = (Band_n/2.0)
               int_crit_2 = int(criterio_2)                           # Retorna a parte inteira do numero real (criterio_2).
               resto_crit_2 = (criterio_2 % 1.0)                      # Retorna a parte fracionaria do numero real (criterio_2).

            if (esc_b == 1) or (esc_b == 2):
               rest = 0.0
               
            if (esc_b == 3):
               rest = 0.5

            if (resto_crit_2 == rest):
               VTemp = procar.readline().split()
               energ =  float(VTemp[4])

######################### Ajuste das energias #########################        

            if (wp == 1):                                             # y(1,1,1)                                      
               dE  = (Efermi)*(-1)
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 2):
               if (point_k == point_i) and (Band_n == Band_i):        # y(2,1,1)
                  dE  = y[1][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 3):
               if (point_k == point_i) and (Band_n == Band_i):        # y(3,1,1)
                  dE  = y[2][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 4):
               if (point_k == point_i) and (Band_n == Band_i):        # y(4,1,1)
                  dE  = y[3][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = float(energ) + flost(dE)
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 5):
               if (point_k == point_i) and (Band_n == Band_i):        # y(5,1,1)
                  dE  = y[4][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 6):
               if (point_k == point_i) and (Band_n == Band_i):        # y(6,1,1)
                  dE  = y[5][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 7):
               if (point_k == point_i) and (Band_n == Band_i):        # y(7,1,1)
                  dE  = y[6][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 8):
               if (point_k == point_i) and (Band_n == Band_i):        # y(8,1,1)
                  dE  = y[7][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 9):
               if (point_k == point_i) and (Band_n == Band_i):        # y(9,1,1)
                  dE  = y[8][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 10):
               if (point_k == point_i) and (Band_n == Band_i):        # y(10,1,1)
                  dE  = y[9][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

#######################################################################

            if (energ_max < auto_valor):                              # Calculo do maior auto-valor de energia.
               energ_max = auto_valor

            if (energ_min > auto_valor):                              # Calculo do menor auto-valor de energia.
               energ_min = auto_valor
              
            VTemp = procar.readline()
            VTemp = procar.readline()      
            
            orb_S  = 0.0
            orb_P  = 0.0
            orb_D = 0.0
            orb_Px = 0.0
            orb_Py = 0.0
            orb_Pz = 0.0
            orb_total = 0.0                       
            
############################ Loop dos ions #############################

#====================== Lendo o Orbital Total ==========================

            for ion_n in range (1, (ni+1)):

#-----------------------------------------------------------------------
                
                if (esc == 0):
                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                      dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                      p = px + py + pz
                      d = dxy + dyz + dz2 + dxz + dx2
                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                         
                   orb_total = orb_total + tot

                   orb_S = orb_S + s
                   orb_P = orb_P + p
                   orb_D = orb_D + d

                   if (lorbit > 10):
                      orb_Px = orb_Px + px
                      orb_Py = orb_Py + py
                      orb_Pz = orb_Pz + pz                

#-----------------------------------------------------------------------

                if (esc == 1):                                         # Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                   temp_sn = sim_nao[ion_n]
                   if (temp_sn == "sim"):
                      
                      if (lorbit >= 11):
                         VTemp = procar.readline().split()
                         ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                         dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])

                         p = px + py + pz
                         d = dxy + dyz + dz2 + dxz + dx2
                      if (lorbit == 10):
                         VTemp = procar.readline().split() 
                         ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])

                      orb_total = orb_total + tot                      # orb_total refere-se a uma quantidade que sera utilizada na normalizacao dos orbitais.

                      orb_S = orb_S + s
                      orb_P = orb_P + p
                      orb_D = orb_D + d
             
                      if (lorbit > 10):
                         orb_Px = orb_Px + px
                         orb_Py = orb_Py + py
                         orb_Pz = orb_Pz + pz
                    
                   if (temp_sn == "nao"):                              # ions nao-selecionados no arquivo (ions_selecionados.txt).
                      if (lorbit >= 11):
                         VTemp = procar.readline().split()
                         ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                         dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                      if (lorbit == 10):
                         VTemp = procar.readline().split() 
                         ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])

                      orb_total = orb_total + tot

            VTemp = procar.readline()
           
#=======================================================================
#========== Pulando as linhas referentes as componentes de Spin ========
#=======================================================================

            if (SO == 2):                                                          # Condicao para calculo com acoplamento Spin-orbita

               n_skip = (3*ni + 3)

               for ion_n in range (1, (n_skip+1)):
                   VTemp = procar.readline()          
 
#============= Pulando as linhas referente a fase (LORBIT 12) ==========

            if (lorbit == 12):
               temp2 = ((2*ni) + 2)
               for i in range (1, (temp2 + 1)):
                   VTemp = procar.readline()

            if (lorbit != 12):
               VTemp = procar.readline()

            #-----------------------------------------------------------------------
            # Fim do laço/loop dos ions --------------------------------------------
            #-----------------------------------------------------------------------                  

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%% Escrita das Texturas/Projeções em um arquivo temporario %%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             
                 
            orb_S = ((orb_S/orb_total) + peso_inicial)*peso_total
            Orbital_S.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_S:>17,.12f} \n')    # Escrita do Orbital_S em um arquivo temporario.                      
            orb_P = ((orb_P/orb_total) + peso_inicial)*peso_total
            Orbital_P.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_P:>17,.12f} \n')    # Escrita do Orbital_P em um arquivo temporario.
            orb_D = ((orb_D/orb_total) + peso_inicial)*peso_total 
            Orbital_D.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_D:>17,.12f} \n')    # Escrita do Orbital_D em um arquivo temporario.

            if (lorbit > 10):
               orb_Px = ((orb_Px/orb_total) + peso_inicial)*peso_total
               Orbital_Px.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Px:>17,.12f} \n')    # Escrita do Orbital_Px em um arquivo temporario.
               orb_Py = ((orb_Py/orb_total) + peso_inicial)*peso_total
               Orbital_Py.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Py:>17,.12f} \n')    # Escrita do Orbital_Py em um arquivo temporario.
               orb_Pz = ((orb_Pz/orb_total) + peso_inicial)*peso_total
               Orbital_Pz.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Pz:>17,.12f} \n')    # Escrita do Orbital_Pz em um arquivo temporario.
                  
        #-----------------------------------------------------------------------
        # Fim do laço/loop das bandas ------------------------------------------
        #-----------------------------------------------------------------------

#================== Ignorar linhas ao final de cada ponto-k ============

        if (point_k < nk):
           VTemp = procar.readline()
        
    #-----------------------------------------------------------------------
    # Fim do laço/loop dos pontos-k ----------------------------------------
    #-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Fim do laço/loop dos procar ------------------------------------------
#-----------------------------------------------------------------------

#=============== Fim da escrita do arquivo "informacoes.txt" ===========

inform.write(" \n")

if (Dimensao == 1):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (2Pi/Param) \n")
   inform.write("         |                  (2Pi/Param)                 | \n")
if (Dimensao == 2):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/Angs.) \n")
   inform.write("         |                   (1/Angs.)                  | \n")
if (Dimensao == 3):
   inform.write("Pontos-k |        Coord. Cartesianas kx, ky e kz        |   Separacao (1/nm) \n")
   inform.write("         |                    (1/nm)                    | \n")
 
inform.write(" \n")

n_point_k = 0

for i in range (1,(n_procar+1)):
    for j in range (1, (nk+1)):
        n_point_k += 1
        inform.write(f'{n_point_k:>4}{kx[i][j]:>19,.12f}{ky[i][j]:>17,.12f}{kz[i][j]:>17,.12f}{separacao[i][j]:>19,.14f} \n')
        
inform.close()

#========== ! Obtendo os pontos-k a serem destacados nos gráficos ======

#------------------------------------------
inform = open("saida/informacoes.txt", "r")
#------------------------------------------

if (SO == 1):
   for i in range (1, (39+1)):
       VTemp = inform.readline()

if (SO == 2):
   for i in range (1, (46+1)):
       VTemp = inform.readline()
       
nk_total = nk*n_procar

contador2 = 0
dest_pk = [0]*(100)                    # Inicialização do vetor dest_pk de dimensão 100.

for i in range (1, (nk_total+1)):
    VTemp = inform.readline().split()
    r1 = int(VTemp[0]); r2 = float(VTemp[1]); r3 = float(VTemp[2]); r4 = float(VTemp[3]); comprimento = float(VTemp[4])
    if (i != 1) and (i != (nk_total+1)):  
       dif = comprimento - comprimento_old     
       if(dif == 0.0):
          contador2 += 1
          dest_pk[contador2] = comprimento
          
    comprimento_old = comprimento

#-------------
inform.close()
#-------------

#-----------------------------------------------------------------------

#-------------
procar.close()
#-------------

#-----------------------------------------------------------------------

Orbital_S.close()
Orbital_P.close()
Orbital_D.close()

if (lorbit > 10):
   Orbital_Px.close()
   Orbital_Py.close()
   Orbital_Pz.close()
    
################## Parametros para ajustes dos Graficos ################

x_inicial = xx[1][1]
x_final   = xx[n_procar][point_f]
y_inicial = energ_min
y_final   = energ_max

# Parametros que ajustam os contornos do grafico: ######################

# delta_xi = ((xx(point_f))/100)*2.5                                   # Aumenta ou diminui a distancia do grafico com relacao a borda Esquerda.
# delta_xf = delta_xi                                                  # Aumenta ou diminui a distancia do grafico com relacao a borda Direita.
# delta_yi = (sqrt(((energ_max - energ_min)/100)**2))*2.5              # Aumenta ou diminui a distancia do grafico com relacao a borda Inferior.
# delta_yf = delta_yi                                                  # Aumenta ou diminui a distancia do grafico com relacao a borda Superior.

# x_inicial = x_inicial - delta_xi
# x_final   = x_final   + delta_xf
# y_inicial = y_inicial - delta_yi
# y_final   = y_final   + delta_yf

print (" ")
print ("==================================")
print (" ")   

########################################################################
################## Agora sera escrito o arquivo de saída ###############
########################################################################
                          
if (lorbit == 10):              # Orbitais (S, P, D)
   wm = 1; wn = 3            
if (lorbit > 10):               # Orbitais (S, P, D) e (Px, Py, Pz)
   wm = 1; wn = 6                   

for t in range (wm,(wn+1)):                   # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

    if (t == 1):
       texturas = open("saida/Orbitais_S_P_D.agr", "w") 
    if (t == 4):
       texturas = open("saida/Orbitais_Px_Py_Pz.agr", "w") 

#-----------------------------------------------------------------------
          
    if (t == 1):
       print ("Analisando a Projecao do Orbital S")
    if (t == 2):
       print (" ")
       print ("Analisando a Projecao do Orbital P")
    if (t == 3):
       print (" ")
       print ("Analisando a Projecao do Orbital D")
    if (t == 4):
       print (" ")
       print ("Analisando a Projecao do Orbital Px")
    if (t == 5):
       print (" ")
       print ("Analisando a Projecao do Orbital Py")
    if (t == 6):
       print (" ")
       print ("Analisando a Projecao do Orbital Pz")

#-----------------------------------------------------------------------

################### Plot das Texturas nos arquivos ".agr" ##############

    if (t == 1 or t == 4):

       texturas.write("# Grace project file \n")
       texturas.write("# \n")
       texturas.write("@version 50122 \n")

       texturas.write("@with box \n")
       texturas.write("@    box on \n")
       if (t <= 3):
          texturas.write("@    box 0.81, 0.95, 0.88, 0.83 \n")
       if (t > 3):
          texturas.write("@    box 0.81, 0.95, 0.8875, 0.83 \n")
       texturas.write("@box def \n")

       for i in range (1,(3+1)):

           texturas.write("@with ellipse \n")
           texturas.write("@    ellipse on \n")
          
           if (i == 1):
              texturas.write("@    ellipse 0.815, 0.92, 0.835, 0.94 \n")
              color = cor[4]       # Cor (Azul) do Orbital S ou Px.
           if (i == 2):
              texturas.write("@    ellipse 0.815, 0.88, 0.835, 0.9 \n")
              color = cor[5]       # Cor (Vermelho) do Orbital P ou Py.
           if (i == 3):
              texturas.write("@    ellipse 0.815, 0.84, 0.835, 0.86 \n")
              color = cor[6]       # Cor (Verde) do Orbital D ou Pz.

           texturas.write(f'@    ellipse color {color} \n')
           texturas.write(f'@    ellipse fill color {color} \n')
           texturas.write("@    ellipse fill pattern 1 \n")
           texturas.write("@ellipse def \n")

       for i in range (1,(3+1)):

           texturas.write("@with string \n")
           texturas.write("@    string on \n")

           if (i == 1):
              if (t <= 3):
                 texturas.write("@    string 0.8525, 0.92 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "S" \n')
              if (t > 3):
                 texturas.write("@    string 0.8525, 0.92 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "Px" \n')                 

           if (i == 2):
              if (t <= 3):              
                 texturas.write("@    string 0.8525, 0.88 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "P" \n')
              if (t > 3):              
                 texturas.write("@    string 0.8525, 0.88 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "Py" \n')              

           if (i == 3):
              if (t <= 3):              
                 texturas.write("@    string 0.8525, 0.84 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "D" \n')
              if (t > 3):              
                 texturas.write("@    string 0.8525, 0.84 \n")
                 texturas.write("@    string color 1 \n")
                 texturas.write(f'@    string def "Pz" \n')

       texturas.write("@with string \n")
       texturas.write("@    string on \n")
       texturas.write("@    string 0.1, 0.96 \n")
       texturas.write(f'@    string def "E(eV)" \n')
       texturas.write("@with string \n")
       texturas.write("@    string on \n")

       if (Dimensao == 1):
          texturas.write("@    string 0.66, 0.017 \n")
          texturas.write(f'@    string def "(2pi/Param.)" \n')
       if (Dimensao == 2):
          texturas.write("@    string 0.70, 0.017 \n")
          texturas.write(f'@    string def "(1/Angs.)" \n')
       if (Dimensao == 3):
          texturas.write("@    string 0.73, 0.017 \n")
          texturas.write(f'@    string def "(1/nm)" \n')

       texturas.write("@with g0 \n")
       texturas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
       texturas.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

       escala_x = (x_final - x_inicial)/5
       escala_y = (y_final - y_inicial)/5

       texturas.write(f'@    xaxis  tick major {escala_x:.2f} \n')
       texturas.write(f'@    yaxis  tick major {escala_y:.2f} \n')        

       for i in range (1,(3+1)):
          
           if (i == 1):
              grac='s0'; color = cor[4]        # Cor (Azul) do Orbital S ou Px.
           if (i == 2):
              grac='s1'; color = cor[5]        # Cor (Vermelho) do Orbital P ou Py.
           if (i == 3):
              grac='s2'; color = cor[6]        # Cor (Verde) do Orbital D ou Pz.

           texturas.write(f'@    {grac} type xysize \n')
           texturas.write(f'@    {grac} symbol 1 \n')
           texturas.write(f'@    {grac} symbol color {color} \n')
           texturas.write(f'@    {grac} symbol fill color {color} \n')
           texturas.write(f'@    {grac} symbol fill pattern 1 \n')
           texturas.write(f'@    {grac} line type 0 \n')
           texturas.write(f'@    {grac} line color {color} \n')
        
       texturas.write("@type xysize")
       texturas.write(" \n")

#-----------------------------------------------------------------------
    num_tot = n_procar*(nk*nb)
#-----------------------------------------------------------------------

    if (t == 1):
       temp = open("temp/Temp_orb-S_Excluir.txt", "r")           
    if (t == 2):
       temp = open("temp/Temp_orb-P_Excluir.txt", "r")
    if (t == 3):
       temp = open("temp/Temp_orb-D_Excluir.txt", "r")
    if (t == 4):
       temp = open("temp/Temp_orb-Px_Excluir.txt", "r")
    if (t == 5):
       temp = open("temp/Temp_orb-Py_Excluir.txt", "r")
    if (t == 6):
       temp = open("temp/Temp_orb-Pz_Excluir.txt", "r")
      
#-----------------------------------------------------------------------

    for j in range (1,(num_tot+1)):
        VTemp = temp.readline().split()
        comp = float(VTemp[0]); auto_valor = float(VTemp[1]); raio = float(VTemp[2])
        if (raio > 0.0):
           texturas.write(f'{comp} {auto_valor} {raio} \n')
          
    texturas.write(" \n")
  
    temp.close()        

#-----------------------------------------------------------------------

    if (t == 3 or t == 6):
      
       # Plot da Estrutura de Bandas.
       for Band_n in range (1,(nb+1)):
           texturas.write(" \n")
           for i in range (1,(n_procar+1)):
               for point_k in range (1,(nk+1)):
                   texturas.write(f'{xx[i][point_k]} {y[i][point_k][Band_n]} 0.0 \n')

#-----------------------------------------------------------------------

       # Destacando a Energia de Fermi, no plot das Texturas.
       texturas.write(" \n")
       if (destacar_efermi == 1):
          texturas.write(f'{xx[1][1]} 0.0 0.0 \n')
          texturas.write(f'{xx[n_procar][point_f]} 0.0 0.0 \n')

#-----------------------------------------------------------------------

       # Destacando pontos-k de interesse na Estrutura de Bandas.
       if (destacar_pontos_k == 1):
          for loop in range (1,(contador2+1)):
              texturas.write(" \n")
              texturas.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
              texturas.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

#-----------------------------------------------------------------------

       texturas.close()

#-----------------------------------------------------------------------

############## Excluindo os arquivos temporarios gerados ###############

if (lorbit == 10):
   os.remove("temp/Temp_orb-S_Excluir.txt")
   os.remove("temp/Temp_orb-P_Excluir.txt")
   os.remove("temp/Temp_orb-D_Excluir.txt")

if (lorbit > 10):
   os.remove("temp/Temp_orb-S_Excluir.txt")
   os.remove("temp/Temp_orb-P_Excluir.txt")
   os.remove("temp/Temp_orb-D_Excluir.txt")
   os.remove("temp/Temp_orb-Px_Excluir.txt")
   os.remove("temp/Temp_orb-Py_Excluir.txt")
   os.remove("temp/Temp_orb-Pz_Excluir.txt")

os.rmdir("temp")

#-----------------------------------------------------------------
print(" ")
print("======================= Concluido =======================")
#-----------------------------------------------------------------

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################