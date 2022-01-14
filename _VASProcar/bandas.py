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

#######################################################
########## Lendo os parâmetros de input ###############
#######################################################

if (leitura == 0 and escolha == -1):
   print ("##############################################################")
   print ("################ Plot da Estrutura de Bandas =================")
   print ("##############################################################") 
   print ("Escolha a dimensao do eixo-k: ================================")
   print ("Utilize 1 para k em unidades de 2pi/Param com Param em Angs. =")
   print ("Utilize 2 para k em unidades de 1/Angs. ======================")
   print ("Utilize 3 para k em unidades de 1/nm. ========================")
   print ("##############################################################") 
   Dimensao = input (" "); Dimensao = int(Dimensao)
   print (" ")

if (leitura == 0 and escolha == 1):
   Dimensao = 1

###########################################################################

if (leitura == 1):
   #----------------------------------------------
   entrada = open("input/input_bandas.txt", "r")
   #----------------------------------------------
   
   for i in range(6):
       VTemp = entrada.readline()
   Dimensao = int(VTemp)

   #--------------
   entrada.close()
   #--------------

###########################################################################    

esc_b = 1                                      # Plotar todas as bandas (tanto com numeração par quanto com numeração ímpar) !!! REMOVER ESTA OPÇÃO DO CÓDIGO !!!
destacar_efermi = 1                            # Destacar o nível de fermi nos gráficos.
destacar_pontos_k = 1                          # Destacar pontos-k nos gráficos.

Band_i = 1
Band_f = nb
point_i = 1
point_f = nk

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
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (2Pi/Param) \n")
if (Dimensao == 2):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/Angs.) \n")
if (Dimensao == 3):
   inform.write("Pontos-k |          Coord. Diretas k1, k2 e k3          |   Separacao (1/nm) \n")

inform.write("         |          K =  k1*B1 + k2*B2 + k3*B3          | \n")
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

    temp = 1.0; number = 0

    for point_k in range(1, (nk+1)):                                  

#######################################################################

        if (n_procar == 1 and point_k == 1):
           print("===========================")
           print("Analisando o arquivo PROCAR")
           print("===========================")

        if (n_procar > 1 and point_k == 1):
           print("==============================")
           print("Analisando o arquivo PROCAR",wp)
           print("==============================")          

#----------------------------------------------------------------------
# Calculando a porcentagem de leitura do arquivo PROCAR ---------------
#----------------------------------------------------------------------

        porc = (point_k/nk)*100        

        if (porc >= temp):
           print(f'Processado {porc:>3,.0f}%')                 
           number += 1
           if (number == 1):
              temp = 10.0
           if (number == 2):
              temp = 25.0
           if (number >= 3):
              temp = temp + 25.0
              
#----------------------------------------------------------------------               
                                                                      
        VTemp = procar.readline().split()                             # Observacao: No VASP k1, k2 e k3 correspondem as coordenadas diretas de cada ponto-k na ZB,                                                         
        k1 = float(VTemp[3])                                        # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X,
        k2 = float(VTemp[4])                                        # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        k3 = float(VTemp[5])                                        # em unidades de 2pi/Parametro.
        
        VTemp = procar.readline()

############### Distancia de separacao entre os pontos-k ##############

        Coord_X = ((k1*B1x) + (k2*B2x) + (k3*B3x))
        Coord_Y = ((k1*B1y) + (k2*B2y) + (k3*B3y))
        Coord_Z = ((k1*B1z) + (k2*B2z) + (k3*B3z))

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

        inform.write(f'{n_point_k:>4}{k1:>19,.12f}{k2:>17,.12f}{k3:>17,.12f}{comp:>19,.14f} \n')

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
            
############################ Loop dos ions #############################

#========================== Lendo os Orbitais ==========================

            for ion_n in range (1, (ni+1)):
                VTemp = procar.readline().split()            

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

palavra = 'Pontos-k |'                          

for line in inform:   
    if palavra in line: 
       break

VTemp = inform.readline()
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

##################### Plot da Estrutura de Bandas: #####################


#-------------------------------------
bandas = open("saida/Bandas.agr", "w")
#-------------------------------------

# Instruções para o GRACE ler o arquivo "Estrutura_de_Bandas.agr" #####

bandas.write("# Grace project file \n")
bandas.write("# \n")
bandas.write("@version 50122 \n")
bandas.write("@with string \n")
bandas.write("@    string on \n")
bandas.write("@    string 0.1, 0.96 \n")
bandas.write(f'@    string def "E(eV)" \n')
bandas.write("@with string \n")
bandas.write("@    string on \n")

if (Dimensao == 1):
   bandas.write("@    string 0.66, 0.017 \n")
   bandas.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   bandas.write("@    string 0.70, 0.017 \n")
   bandas.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   bandas.write("@    string 0.73, 0.017 \n")
   bandas.write(f'@    string def "(1/nm)" \n')

bandas.write("@with g0 \n")
bandas.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
bandas.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5
bandas.write(f'@    xaxis  tick major {escala_x:.2f} \n')
bandas.write(f'@    yaxis  tick major {escala_y:.2f} \n')

##################### Plot da Estrutura de Bandas #####################
      
for Band_n in range (Band_i,(Band_f+1)):
    bandas.write(" \n")
    for j in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            bandas.write(f'{xx[j][point_k]} {y[j][point_k][Band_n]} \n')

# Destacando a Energia de Fermi na Estrutura de Bandas.
      
if (destacar_efermi == 1):
   bandas.write(" \n")
   bandas.write(f'{xx[1][1]} 0.0 \n')
   bandas.write(f'{xx[n_procar][point_f]} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas.

if (n_procar == 1):
   if (destacar_pontos_k == 1):
      for loop in range (1,(contador2+1)):
          bandas.write(" \n")
          bandas.write(f'{dest_pk[loop]} {energ_min} \n')
          bandas.write(f'{dest_pk[loop]} {energ_max} \n')

# Destacando alguns pontos-k de interesse na Estrutura de Bandas.

if (n_procar > 1):
   wr = n_procar + 1
   for loop in range (1,(wr+1)):
       bandas.write(" \n")
       if (loop != wr):
          bandas.write(f'{xx[loop][1]} {energ_min} \n')
          bandas.write(f'{xx[loop][1]} {energ_max} \n')
       if (loop == wr):
          bandas.write(f'{xx[n_procar][nk]} {energ_min} \n')
          bandas.write(f'{xx[n_procar][nk]} {energ_max} \n')        

#-------------
bandas.close()
#-------------

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
