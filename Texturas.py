
print ("")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Versao 4.006 (02/09/2021) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Autor: Augusto de Lelis Araújo - INFIS/UFU (Uberlândia/MG)")
print ("e-mail: augusto-lelis@outlook.com %%%%%%%%%%%%%%%%%%%%%%%%")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("")



############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 1: OBTENÇÃO DE INFORMAÇÕES DO SISTEMA ########################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################

print ("#######################################################")
print ("############ Lendo o arquivo de input #################")
print ("#######################################################")
print ("")

################################################

entrada = open("input_Texturas.txt", "r")

for i in range(6):
    VTemp = entrada.readline()
Dimensao = int(VTemp)                          # Unidade de medida adotada no eixo-k (2pi/Param, 1/Angs ou 1/nm).

for i in range(7):
    VTemp = entrada.readline()
e = int(VTemp)                                 # Projecoes a serem analisadas.

for i in range(3):
    VTemp = entrada.readline()
peso_total = float(VTemp)                      # Tamanho/peso das esferas nos graficos de projeções.

for i in range(5):
    VTemp = entrada.readline()
esc = int(VTemp)                               # Escolha se serão Plotados/Analisados todos os ions ou não, nas projeções.

esc_b = 1                                      # Plotar todas as bandas (tanto com numeração par quanto com numeração ímpar) !!! REMOVER ESTA OPÇÃO DO CÓDIGO !!!
destacar_efermi = 1                            # Destacar o nível de fermi nos gráficos.
destacar_pontos_k = 1                          # Destacar pontos-k nos gráficos.
peso_inicial = 0.0                             # Menor tamanho de esfera nos gráficos de projeções.

entrada.close() 

################################################

# Obs.: Codigo das cores
# Branco=0, Preto=1, Vermelho=2, Verde=3, Azul=4, Amarelo=5, Marrom=6, Cinza=7
# Violeta=8, Cyan=9, Magenta=10, Laranja=11, Indigo=12, Marron=13, Turquesa=14
                                                                        
cor = [1]*10   # Inicialização do vetor cor

cor[1] = 1    # Cor da componente Nula do Spin (Preto)            
cor[2] = 2    # Cor da componente Up do Spin   (Vermelho)         
cor[3] = 4    # Cor da componente Down do Spin (Azul)
cor[4] = 4    # Cor do Orbital S (Azul)
cor[5] = 2    # Cor do Orbital P (Vermelho)
cor[6] = 3    # Cor do Orbital D (Verde)
cor[7] = 4    # Cor do Orbital Px (Azul)
cor[8] = 2    # Cor do Orbital Py (Vermelho)
cor[9] = 3    # Cor do Orbital Pz (Verde)


####### Obtendo o nº de arquivos PROCAR: #######

try: f = open('PROCAR'); f.close(); n_procar = 1
except: 0 == 0
try: f = open("PROCAR.1"); f.close(); n_procar = 1
except: 0 == 0
try: f = open('PROCAR.2'); f.close(); n_procar = 2
except: 0 == 0
try: f = open('PROCAR.3'); f.close(); n_procar = 3
except: 0 == 0
try: f = open('PROCAR.4'); f.close(); n_procar = 4
except: 0 == 0
try: f = open('PROCAR.5'); f.close(); n_procar = 5
except: 0 == 0
try: f = open('PROCAR.6'); f.close(); n_procar = 6
except: 0 == 0
try: f = open('PROCAR.7'); f.close(); n_procar = 7
except: 0 == 0
try: f = open('PROCAR.8'); f.close(); n_procar = 8
except: 0 == 0
try: f = open('PROCAR.9'); f.close(); n_procar = 9
except: 0 == 0
try: f = open('PROCAR.10'); f.close(); n_procar = 10
except: 0 == 0

################################################

print ("#######################################################")
print ("########## Analisando o arquivo OUTCAR ################")
print ("######## Buscando informacoes do Sistema ##############")
print ("#######################################################")
print ("")

outcar = open("OUTCAR", "r")
inform = open("informacoes.txt", "w")

################################################

palavra = 'Dimension'                          # Dimension e uma palavra presente em uma linha anterior as linhas que contem a informacao sobre o número de pontos-k (nk), bandas (nb) e ions (ni).

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
nk = int(VTemp[3])
nb = int(VTemp[14])

VTemp = outcar.readline().split()
ni = int(VTemp[11])

################################################

#-----------------------------------------------------------------------
# Verificacao se o calculo foi realizado com ou sem o acoplamento SO
#-----------------------------------------------------------------------

palavra = 'ICHARG'                             # ICHARG e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel ISPIN.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
ispin = int(VTemp[2])                          # Leitura do valor associado a variavel ISPIN.

if ispin == 2:
   print ("--------------------------------------------------------")
   print ("--------------------------------------------------------")
   print ("Este programa não foi compilado para analisar um cálculo")
   print ("com polarização de Spin (ISPIN = 2)")
   print ("********************************************************")
   print ("Modifique o códifo fonte, ou refaça seu cálculo")
   print ("********************************************************")
   print ("--------------------------------------------------------")
   print ("--------------------------------------------------------")
   
################################################

palavra = 'LNONCOLLINEAR'                      # LNONCOLLINEAR e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel LSORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lsorbit = VTemp[2]                             # Leitura do valor associado a variavel LSORBIT.

inform.write("---------------------------------------------------- \n")

if (lsorbit == "F"):
   SO = 1
   inform.write("LSORBIT = .FALSE. (Calculo sem acoplamento SO) \n")
if (lsorbit == "T"):
   SO = 2
   inform.write("LSORBIT = .TRUE. (Calculo com acoplamento SO) \n")

#-----------------------------------------------------------------------
# Verificacao do numero de eletrons do sistema.
#----------------------------------------------------------------------- 
 
palavra = 'VCA'                                # VCA e uma palavra presente em uma linha anterior a linha que contem a informacao sobre a variavel NELECT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
n_eletrons = float(VTemp[2])                          # Leitura do valor associado a variavel NELECT.

inform.write("---------------------------------------------------- \n")

inform.write(f'nº de Pontos-k = {nk};  nº de Bandas = {nb} \n')
inform.write(f'nº de ions = {ni};  nº de eletrons = {n_eletrons} \n')

#-----------------------------------------------------------------------
# Verificacao do LORBIT utilizado para a geracao do arquivo PROCAR.
#-----------------------------------------------------------------------
 
palavra = 'LELF'                               # LELF e uma palavra presenta em uma linha anterior a linha que contem a informacao sobre a variavel LORBIT.

for line in outcar:   
    if palavra in line: 
       break

VTemp = outcar.readline().split()
lorbit = int(VTemp[2])                              # Leitura do valor associado a variavel LORBIT.

inform.write("--------------------------------------------------- \n")
inform.write(f'LORBIT = {lorbit};  ISPIN = {ispin} (sem polarizacao de spin) \n')
inform.write("--------------------------------------------------- \n")

################################################

outcar.close() 
outcar = open("OUTCAR", "r") 

#-----------------------------------------------------------------------
# Busca da Energia de Fermi do sistema.
#-----------------------------------------------------------------------

palavra = 'average'                            # average e uma palavra presente em uma linha um pouco anterior a linha que contem a informacao sobre a variavel E-fermi.
number = 0                                     # number representa qual linha contem a informacao sobre a variavel E-fermi.

for line in outcar:
    number += 1
  
    if palavra in line: 
       break

palavra = 'E-fermi'

for line in outcar:
    number += 1
     
    if palavra in line: 
       break

#-----------------------------------------------

outcar.close() 
outcar = open("OUTCAR", "r") 

#-----------------------------------------------

for i in range(number):
    VTemp = outcar.readline().split()

Efermi = float(VTemp[2])                              # Leitura do valor associado a variavel E-fermi.

inform.write(f'Energia de fermi = {Efermi} eV \n')
inform.write("--------------------------------------------------- \n")

################################################

#-----------------------------------------------------------------------
# Verificando quais bandas de energia correspondem as bandas de valencia
# e conducao, bem como do respectivo GAP de energia.
# Esta verificacao somente faz sentido para calculos realizados em um
# unico passo, visto que o arquivo CONTCAR analisado pode ou nao conter
# a regiao de menor GAP do sistema.
# Esta verificacao tambem nao faz sentido para sistemas metalicos.
#-----------------------------------------------------------------------

VTemp = outcar.readline(); VTemp = outcar.readline()

menor_n2 = -1000.0
maior_n2 = +1000.0
number = 0

for i in range(nk):
    number += 1
    
    VTemp = outcar.readline()
    VTemp = outcar.readline()
    for j in range(nb):
        VTemp = outcar.readline().split()
        n1 = int(VTemp[0])
        n2 = float(VTemp[1])
        n3 = float(VTemp[2])
        if (n3 > 0.0):
           if (n2 > menor_n2):
              menor_n2 = n2
              n1_valencia = n1
              k1 = number
        if (n3 == 0.0):
           if (n2 < maior_n2):
              maior_n2 = n2
              n1_conducao = n1
              k2 = number
        GAP = (maior_n2 - menor_n2)
    VTemp = outcar.readline() 

inform.write(f'Ultima Banda ocupada = {n1_valencia} \n')
inform.write(f'Primeira Banda vazia = {n1_conducao} \n')

if (k1 == k2):
   inform.write(f'GAP (direto) = {GAP} eV  -  Kpoint {k1} \n')
if (k1 != k2):
   inform.write(f'GAP (indireto) = {GAP} eV  //  Kpoints {k1} e {k2} \n')

inform.write("---------------------------------------------------- \n")


#-----------------------------------------------------------------------
# Busca da Energia total do sistema.
#-----------------------------------------------------------------------

palavra = 'FREE'                               # FREE e uma palavra presente em uma linha que fica quatro linhas anteriores a linha que contem a informacao sobre a variavel (free energy TOTEN).
number = 0                                     # number representa qual linha contem a informacao sobre a variavel (free energy TOTEN).

for line in outcar:
    number += 1
     
    if palavra in line: 
       break

for i in range(3):
    VTemp = outcar.readline()
    
VTemp = outcar.readline().split()
energ_tot = float(VTemp[3])                    # Leitura do valor associado a variavel NELECT.

inform.write(f'free energy TOTEN = {energ_tot} eV \n')
inform.write("--------------------------------------------------- \n")

#-----------------------------------------------------------------------
# Buscando os valores de Magnetizacao.
#-----------------------------------------------------------------------

if (SO == 2):
   temp_xk = 4 + ni

#------------------------- Magentizacao (X): ---------------------------

   palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
   number = 0 

   for line in outcar:
       number += 1
     
       if palavra in line: 
          break

   for i in range(temp_xk):
       VTemp = outcar.readline()

   VTemp = outcar.readline().split()
   mag_s_x = float(VTemp[1])
   mag_p_x = float(VTemp[2])
   mag_d_x = float(VTemp[3])
   mag_tot_x = float(VTemp[4])

#------------------------- Magentizacao (y): ---------------------------

   palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
   number = 0 

   for line in outcar:
       number += 1
     
       if palavra in line: 
          break

   for i in range(temp_xk):
       VTemp = outcar.readline()

   VTemp = outcar.readline().split()
   mag_s_y = float(VTemp[1])
   mag_p_y = float(VTemp[2])
   mag_d_y = float(VTemp[3])
   mag_tot_y = float(VTemp[4])

#------------------------- Magentizacao (z): ---------------------------

   palavra = 'magnetization'                   # magnetization e uma palavra presente em uma linha que fica acima das linhas que contem a informacao sobre a magnetização do sistema.
   number = 0 

   for line in outcar:
       number += 1
     
       if palavra in line: 
          break

   for i in range(temp_xk):
       VTemp = outcar.readline()

   VTemp = outcar.readline().split()
   mag_s_z = float(VTemp[1])
   mag_p_z = float(VTemp[2])
   mag_d_z = float(VTemp[3])
   mag_tot_z = float(VTemp[4])

#-----------------------------------------------

inform.write(" \n")
inform.write("################# Magnetizacao: ##################### \n")
inform.write(f'Eixo X:  total = {mag_tot_x:.4f} \n')
inform.write(f'Eixo Y:  total = {mag_tot_y:.4f} \n')
inform.write(f'Eixo Z:  total = {mag_tot_z:.4f} \n')
inform.write("##################################################### \n")
inform.write(" \n")

#-----------------------------------------------

outcar.close()

#######################################################################
##################### Leitura do Arquivo CONTCAR ######################
#######################################################################
 
contcar = open("CONTCAR", "r") 

#-----------------------------------------------

VTemp = contcar.readline().split()
VTemp = contcar.readline().split()

Parametro = float(VTemp[0])                                 # Leitura do Parametro de rede do sistema.

A1 = contcar.readline().split()
A1x = float(A1[0]); A1y = float(A1[1]); A1z = float(A1[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A1) da celula unitaria no espaco real.

A2 = contcar.readline().split()
A2x = float(A2[0]); A2y = float(A2[1]); A2z = float(A2[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A2) da celula unitaria no espaco real.

A3 = contcar.readline().split()
A3x = float(A3[0]); A3y = float(A3[1]); A3z = float(A3[2])  # Leitura das coordenadas (X, Y e Z) do vetor primitivo (A3) da celula unitaria no espaco real.

#-----------------------------------------------------------------------

contcar.close()

#-----------------------------------------------------------------------
#------------- Determinacao do Parametro de Rede como sendo o ----------
#----------- menor valor entre o modulo dos vetores A1, A2 e A3 --------
#-----------------------------------------------------------------------

A1x = A1x*Parametro; A1y = A1y*Parametro; A1z = A1z*Parametro
A2x = A2x*Parametro; A2y = A2y*Parametro; A2z = A2z*Parametro
A3x = A3x*Parametro; A3y = A3y*Parametro; A3z = A3z*Parametro

Parametro_1 = ((A1x*A1x) + (A1y*A1y) + (A1z*A1z))**0.5
Parametro = Parametro_1

Parametro_2 = ((A2x*A2x) + (A2y*A2y) + (A2z*A2z))**0.5
if (Parametro_2 < Parametro):
   Parametro = Parametro_2

Parametro_3 = ((A3x*A3x) + (A3y*A3y) + (A3z*A3z))**0.5
if (Parametro_3 < Parametro):
   Parametro = Parametro_3

A1x = A1x/Parametro; A1y = A1y/Parametro; A1z = A1z/Parametro
A2x = A2x/Parametro; A2y = A2y/Parametro; A2z = A2z/Parametro
A3x = A3x/Parametro; A3y = A3y/Parametro; A3z = A3z/Parametro

#------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("***** Vetores Primitivos da Rede Cristalina ********* \n")
inform.write(f'****  A1 = Param.({A1x}, {A1y}, {A1z}) \n')
inform.write(f'****  A2 = Param.({A2x}, {A2y}, {A2z}) \n')
inform.write(f'****  A3 = Param.({A3x}, {A3y}, {A3z}) \n')
inform.write(f'****  Param. = {Parametro} Angs. \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#------------------------------------------------------------

ss1 = A1x*((A2y*A3z) - (A2z*A3y))
ss2 = A1y*((A2z*A3x) - (A2x*A3z))
ss3 = A1z*((A2x*A3y) - (A2y*A3x))
ss =  ss1 + ss2 + ss3                                        # Eu apenas divide esta soma em tres partes, uma vez que ela e muito longa, e ultrapassava a extensao da linha.

B1x = ((A2y*A3z) - (A2z*A3y))/ss                             # Para compreender estas operacoes sobre as componentes X, Y e Z dos vetores primitvos da rede
B1y = ((A2z*A3x) - (A2x*A3z))/ss                             # cristalina (A1, A2 e A3), vc deve executar a operacao padrao de construcao dos vetores
B1z = ((A2x*A3y) - (A2y*A3x))/ss                             # primitivos da rede rec¡proca com base nos vetores primitvos da rede cristalina.
B2x = ((A3y*A1z) - (A3z*A1y))/ss                             # Tal operacao se encontra disponivel em qualquer livro de estado solido.
B2y = ((A3z*A1x) - (A3x*A1z))/ss
B2z = ((A3x*A1y) - (A3y*A1x))/ss
B3x = ((A1y*A2z) - (A1z*A2y))/ss
B3y = ((A1z*A2x) - (A1x*A2z))/ss
B3z = ((A1x*A2y) - (A1y*A2x))/ss

#------------------------------------------------------------

inform.write("***************************************************** \n")
inform.write("***** Vetores Primitivos da Rede Reciproca ********** \n")
inform.write(f'****  B1 = 2pi/Param.({B1x}, {B1y}, {B1z}) \n')
inform.write(f'****  B2 = 2pi/Param.({B2x}, {B2y}, {B2z}) \n')
inform.write(f'****  B3 = 2pi/Param.({B3x}, {B3y}, {B3z}) \n')
inform.write(f'****  Param. = {Parametro} Angs. \n')
inform.write("***************************************************** \n")
inform.write(" \n")

#------------------------------------------------------------

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



############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 2: EXTRAÇÃO DOS RESULTADOS ###################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################



if (lorbit == 10):
   if (e == -99) or (e == 100):
      Orbital_S = open("Temp_orb-S_Excluir.txt", "w")
      Orbital_P = open("Temp_orb-P_Excluir.txt", "w")
      Orbital_D = open("Temp_orb-D_Excluir.txt", "w")

if (lorbit > 10):
   if (e == -99) or (e == 100):
      Orbital_Px = open("Temp_orb-Px_Excluir.txt", "w")
      Orbital_Py = open("Temp_orb-Py_Excluir.txt", "w")
      Orbital_Pz = open("Temp_orb-Pz_Excluir.txt", "w")
      Orbital_S  = open("Temp_orb-S_Excluir.txt", "w")
      Orbital_P  = open("Temp_orb-P_Excluir.txt", "w")
      Orbital_D  = open("Temp_orb-D_Excluir.txt", "w")
        
if (SO == 2):
   if (e == 99) or (e == 100):
      Spin_Sx = open("Temp_Spin_Sx_Excluir.txt", "w")
      Spin_Sy = open("Temp_Spin_Sy_Excluir.txt", "w")
      Spin_Sz = open("Temp_Spin_Sz_Excluir.txt", "w")

#-----------------------------------------------------------------------

if (esc == 0) or (esc == 1):                                           # Para esc = 0 ou 1, todas as Bandas e K_Points sao plotados.
   Band_i = 1
   Band_f = nb
   point_i = 1
   point_f = nk
        
if (esc == 0):                                                         # Para esc = 0 ou 1, todos os ions sao analisados.
   ion_i = 1
   ion_f = ni                                                     

#-----------------------------------------------------------------------

if (esc == 1):

   sim_nao = ["nao"]*(ni + 1)                                          # Inicialização do vetor sim_nao
   
   entrada = open("ions_selecionados.txt", "r")

   VTemp = entrada.readline().split()
   loop = int(VTemp[0])

   for j in range(loop):

       VTemp = entrada.readline().split(); loop_i = int(VTemp[0]); loop_f = int(VTemp[1])

       if (loop_i > ni) or (loop_f > ni):
          print ("")
          print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
          print ("ERRO: Corrija o arquivo de entrada (ions_selecionados.txt)")
          print ("      existe mais atómos definidos do que na rede")
          print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
          print ("")

          break
       
       for i in range(loop_i, (loop_f + 1)):
           sim_nao[i] = "sim"
          
entrada.close()

#-----------------------------------------------------------------------

print ("")
print ("Rodando: ##############################################")
print ("####### Rodando: ######################################")
print ("############### Rodando: ##############################")
print ("####################### Rodando: ######################")
print ("############################### Rodando: ##############")
print ("####################################### Rodando: ######")
print ("############################################## Rodando:")
print ("")
print ("")

# Band_antes   = (Band_i  - 1)       # Bandas que nao serao plotadas.
# Band_depois  = (Band_f  + 1)       # Bandas que nao serao plotadas.
# point_antes  = (point_i - 1)       # K_points que nao serao plotados.
# point_depois = (point_f + 1)       # K_points que nao serao plotados.
# ion_antes  = (ion_i - 1)       # ions que nao serao analisados.
# ion_depois = (ion_f + 1)       # ions que nao serao analisados.

energ_max = -1000.0
energ_min = +1000.0

#-----------------------------------------------------------------------

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

#----------------------------------------------------------------------

########################## Loop dos PROCAR #############################

wp = 0
n_point_k = 0

################# Inicialização de Vetores e Matrizes: #################
                                              
xx = [[0]*(nk+1) for i in range(n_procar+1)]
kx = [[0]*(nk+1) for i in range(n_procar+1)]
ky = [[0]*(nk+1) for i in range(n_procar+1)]
kz = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]    

for L0 in range(1, (n_procar+1)):

    wp += 1   

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
      
######################### Loop dos Pontos_k ############################
                                                                      # Observacao: No VASP k_b1, k_b2 e k_b3 correspondem as coordenadas diretas de cada ponto-k na ZB, 
    for point_k in range(1, (nk+1)):                                  # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X, 
                                                                      # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        VTemp = procar.readline().split()                             # em unidades de 2pi/Parametro.
        k_b1 = float(VTemp[3])
        k_b2 = float(VTemp[4])
        k_b3 = float(VTemp[5]) 
        
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

#######################################################################

        if (n_procar == 1):
           print("Analisando o Ponto_k",point_k)

        if (n_procar > 1):
           print("Analisando o Ponto_k",point_k,"do PROCAR",wp)

        if (point_k == nk):
           print("===================================")

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
            spin_Sx = 0.0
            spin_Sy = 0.0
            spin_Sz  = 0.0            
            
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

                   if (e == -99) or (e == 100):
                      orb_S = orb_S + s
                      orb_P = orb_P + p
                      orb_D = orb_D + d

                   if (lorbit > 10):
                      if (e == -99) or (e == 100):
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

                      if (e == -99) or (e == 100):
                         orb_S = orb_S + s
                         orb_P = orb_P + p
                         orb_D = orb_D + d
             
                      if (lorbit > 10):
                         if (e == -99) or (e == 100):
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

            #-----------------------------------------------------------------------
            # Fim Parcial do laço/loop dos ions ------------------------------------
            #-----------------------------------------------------------------------

            VTemp = procar.readline()

            if (SO == 2):                                                          # Condicao para calculo com acoplamento Spin-orbita
            
#=======================================================================
#===================== Lendo a componente Sx do Spin ===================
#=======================================================================
               for ion_n in range (1, (ni+1)):
#-----------------------------------------------------------------------
                  if (e == 99) or (e == 100):
                     if (esc == 0):                                     # Lendo todos ions da rede.
                        if (lorbit >= 11):
                           VTemp = procar.readline().split()
                           ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                           dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsx = float(VTemp[10])
                           
                        if (lorbit == 10):
                           VTemp = procar.readline().split() 
                           ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsx = float(VTemp[4])
                        #----------------------
                        spin_Sx = spin_Sx + totsx
#-----------------------------------------------------------------------
                     if (esc == 1):                                     # Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                        temp_sn = sim_nao[ion_n]
                        if (temp_sn == "sim"):
                           if (lorbit >= 11):
                              VTemp = procar.readline().split()
                              ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                              dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsx = float(VTemp[10])
                           if (lorbit == 10):
                              VTemp = procar.readline().split() 
                              ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsx = float(VTemp[4])
                        #----------------------
                        spin_Sx = spin_Sx + totsx
                        #----------------------
                        if (temp_sn == "nao"):
                           VTemp = procar.readline()
#-----------------------------------------------------------------------
                  if (e != 99) and (e != 100):
                     VTemp = procar.readline()
               #-----------------------------------------------------------------------
               # Fim Parcial do laço/loop dos ions ------------------------------------
               #-----------------------------------------------------------------------
               VTemp = procar.readline()

#=======================================================================
#===================== Lendo a componente Sy do Spin ===================
#=======================================================================
               for ion_n in range (1, (ni+1)):
#-----------------------------------------------------------------------
                  if (e == 99) or (e == 100):
                     if (esc == 0):                                     # Lendo todos ions da rede.
                        if (lorbit >= 11):
                           VTemp = procar.readline().split()
                           ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                           dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsy = float(VTemp[10])
                           
                        if (lorbit == 10):
                           VTemp = procar.readline().split() 
                           ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsy = float(VTemp[4])
                        #----------------------
                        spin_Sy = spin_Sy + totsy
#-----------------------------------------------------------------------
                     if (esc == 1):                                     # Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                        temp_sn = sim_nao[ion_n]
                        if (temp_sn == "sim"):
                           if (lorbit >= 11):
                              VTemp = procar.readline().split()
                              ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                              dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsy = float(VTemp[10])
                           if (lorbit == 10):
                              VTemp = procar.readline().split() 
                              ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsy = float(VTemp[4])
                        #----------------------
                        spin_Sy = spin_Sy + totsy
                        #----------------------
                        if (temp_sn == "nao"):
                           VTemp = procar.readline()
#-----------------------------------------------------------------------
                  if (e != 99) and (e != 100):
                     VTemp = procar.readline()
               #-----------------------------------------------------------------------
               # Fim Parcial do laço/loop dos ions ------------------------------------
               #-----------------------------------------------------------------------
               VTemp = procar.readline()

#=======================================================================
#===================== Lendo a componente Sz do Spin ===================
#=======================================================================             
               for ion_n in range (1, (ni+1)):
#-----------------------------------------------------------------------
                  if (e == 99) or (e == 100):
                     if (esc == 0):                                     # Lendo todos ions da rede.
                        if (lorbit >= 11):
                           VTemp = procar.readline().split()
                           ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                           dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsz = float(VTemp[10])
                           
                        if (lorbit == 10):
                           VTemp = procar.readline().split() 
                           ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsz = float(VTemp[4])
                        #----------------------
                        spin_Sz = spin_Sz + totsz
#-----------------------------------------------------------------------
                     if (esc == 1):                                     # Lendo os ions selecionados no arquivo (ions_selecionados.txt).
                        temp_sn = sim_nao[ion_n]
                        if (temp_sn == "sim"):
                           if (lorbit >= 11):
                              VTemp = procar.readline().split()
                              ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                              dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); totsz = float(VTemp[10])
                           if (lorbit == 10):
                              VTemp = procar.readline().split() 
                              ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); totsz = float(VTemp[4])
                        #----------------------
                        spin_Sz = spin_Sz + totsz
                        #----------------------
                        if (temp_sn == "nao"):
                           VTemp = procar.readline()
#-----------------------------------------------------------------------
                  if (e != 99) and (e != 100):
                     VTemp = procar.readline()
               #-----------------------------------------------------------------------
               # Fim Parcial do laço/loop dos ions ------------------------------------
               #-----------------------------------------------------------------------
               VTemp = procar.readline()          
 
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%% Escrita das Texturas/Projeções em um arquivo temporario %%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%             

               if (e == -99) or (e == 100):
                   
                   orb_S = ((orb_S/orb_total) + peso_inicial)*peso_total
                   Orbital_S.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_S:>17,.12f} \n')    # Escrita do Orbital_S em um arquivo temporario.                      
                   orb_P = ((orb_P/orb_total) + peso_inicial)*peso_total
                   Orbital_P.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_P:>17,.12f} \n')    # Escrita do Orbital_P em um arquivo temporario.
                   orb_D = ((orb_D/orb_total) + peso_inicial)*peso_total 
                   Orbital_D.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_D:>17,.12f} \n')    # Escrita do Orbital_D em um arquivo temporario.

               if (lorbit > 10):
                  if (e == -99) or (e == 100):
                     orb_Px = ((orb_Px/orb_total) + peso_inicial)*peso_total
                     Orbital_Px.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Px:>17,.12f} \n')    # Escrita do Orbital_Px em um arquivo temporario.
                     orb_Py = ((orb_Py/orb_total) + peso_inicial)*peso_total
                     Orbital_Py.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Py:>17,.12f} \n')    # Escrita do Orbital_Py em um arquivo temporario.
                     orb_Pz = ((orb_Pz/orb_total) + peso_inicial)*peso_total
                     Orbital_Pz.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{orb_Pz:>17,.12f} \n')    # Escrita do Orbital_Pz em um arquivo temporario.
   
# $$$$$$$$$$$ Aparentemente o valor dos spins nao estao normalizados como ocorre para os orbitais. $$$$$$$$$$$
# $$$$$$$$$$$ Verificar se esta normalizacao e necessaria. $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

               if (e == 99) or (e == 100):
                  spin_Sx = (spin_Sx + peso_inicial)*peso_total
                  Spin_Sx.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{spin_Sx:>17,.12f} \n')    # Escrita da componente Sx do Spin em um arquivo temporario.                
                  spin_Sy = (spin_Sy + peso_inicial)*peso_total
                  Spin_Sy.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{spin_Sy:>17,.12f} \n')    # Escrita da componente Sy do Spin em um arquivo temporario.
                  spin_Sz = (spin_Sz + peso_inicial)*peso_total
                  Spin_Sz.write(f'{comp:>17,.12f}{auto_valor:>17,.12f}{spin_Sz:>17,.12f} \n')    # Escrita da componente Sz do Spin em um arquivo temporario.

#============= Pulando as linhas referente a fase (LORBIT 12) ==========

               if (lorbit == 12):
                  temp2 = ((2*ni) + 2)
                  for i in range (1, (temp2 + 1)):
                      VTemp = procar.readline()

               if (lorbit != 12):
                  VTemp = procar.readline()
                
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

inform = open("informacoes.txt", "r")

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

inform.close()

#-----------------------------------------------------------------------

procar.close()

if (e == -99) or (e == 100):
   Orbital_S.close()
   Orbital_P.close()
   Orbital_D.close()

if (lorbit > 10):
   if (e == -99) or (e == 100):
      Orbital_Px.close()
      Orbital_Py.close()
      Orbital_Pz.close()

if (SO == 2):
   if (e == 99) or (e == 100):      
      Spin_Sx.close()
      Spin_Sy.close()
      Spin_Sz.close()
      


############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### BLOCO 2: PLOT DAS BANDAS E PROJEÇÕES ###############################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################



################## Parametros para ajustes dos Graficos ################

bandas = open("Estrutura_de_Bandas.agr", "w")

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
      
for Band_n in range (1,(nb+1)):
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

if (destacar_pontos_k == 1):
   for loop in range (1,(contador2+1)):
        bandas.write(" \n")
        bandas.write(f'{dest_pk[loop]} {energ_min} \n')
        bandas.write(f'{dest_pk[loop]} {energ_max} \n')

bandas.close()

########################################################################

#-----------------------------------------------------------------------
if (e != 77):                                                          # Lembrando que a opcao e = 77 faz com que somente a Estrutura de Bandas seja plotada.
#-----------------------------------------------------------------------

   print (" ")
   print ("########################################################")
   print ("############# Processando os Resultados ################")
   print ("########################################################")
   print (" ")

########################################################################
################## Agora sera escrito o arquivo de saída ###############
########################################################################

   if (e !=99 and e != -99 and e != 100):
      wm = 1; wn = 1
   if (e == 99):                                # Spin (Sx, Sy e Sz)
      wm = 1; wn = 3                              
   if (e == -99 and lorbit == 10):              # Orbitais (S, P, D)
      wm = 4; wn = 6            
   if (e == -99 and lorbit > 10):               # Orbitais (S, P, D) e (Px, Py, Pz)
      wm = 4; wn = 9            
   if (e == 100 and lorbit == 10):              # Spin (Sx, Sy e Sz)  //  Orbitais (S, P, D)
      wm = 1; wn = 6            
   if (e == 100 and lorbit > 10):               # Spin (Sx, Sy e Sz)  //  Orbitais (S, P, D) e (Px, Py, Pz)
      wm = 1; wn = 9            


   for t in range (wm,(wn+1)):                   # Loop para a analise das Projecoes
        
#-----------------------------------------------------------------------

       if (e == 99 and t == 1) or (e == 100 and t == 1):
          texturas = open("Textura_Spin_Sx.agr", "w") 
       if (e == 99 and t == 2) or (e == 100 and t == 2):
          texturas = open("Textura_Spin_Sy.agr", "w")
       if (e == 99 and t == 3) or (e == 100 and t == 3):
          texturas = open("Textura_Spin_Sz.agr", "w")

       if (e == -99 and t == 4) or (e == 100 and t == 4):
          texturas = open("Orbitais_S_P_D.agr", "w") 
       if (e == -99 and t == 7) or (e == 100 and t == 7):
          texturas = open("Orbitais_Px_Py_Pz.agr", "w") 

#-----------------------------------------------------------------------

       if (e == 99 and t == 1):
          print ("Analisando a Projecao Sx do Spin")
       if (e == 99 and t == 2):
          print (" ")
          print ("Analisando a Projecao Sy do Spin")
       if (e == 99 and t == 3):
          print (" ")
          print ("Analisando a Projecao Sz do Spin")
          
       if (e == -99 and t == 4):
          print ("Analisando a Projecao do Orbital S")
       if (e == -99 and t == 5):
          print (" ")
          print ("Analisando a Projecao do Orbital P")
       if (e == -99 and t == 6):
          print (" ")
          print ("Analisando a Projecao do Orbital D")
       if (e == -99 and t == 7):
          print (" ")
          print ("Analisando a Projecao do Orbital Px")
       if (e == -99 and t == 8):
          print (" ")
          print ("Analisando a Projecao do Orbital Py")
       if (e == -99 and t == 9):
          print (" ")
          print ("Analisando a Projecao do Orbital Pz")

       if (e == 100 and t == 1):
          print ("Analisando a Projecao Sx do Spin")
       if (e == 100 and t == 2):
          print (" ")
          print ("Analisando a Projecao Sy do Spin")
       if (e == 100 and t == 3):
          print (" ")
          print ("Analisando a Projecao Sz do Spin")
       if (e == 100 and t == 4):
          print (" ")
          print ("Analisando a Projecao do Orbital S")
       if (e == 100 and t == 5):
          print (" ")
          print ("Analisando a Projecao do Orbital P")
       if (e == 100 and t == 6):
          print (" ")
          print ("Analisando a Projecao do Orbital D")
       if (e == 100 and t == 7):
          print (" ")
          print ("Analisando a Projecao do Orbital Px")
       if (e == 100 and t == 8):
          print (" ")
          print ("Analisando a Projecao do Orbital Py")
       if (e == 100 and t == 9):
          print (" ")
          print ("Analisando a Projecao do Orbital Pz")

#-----------------------------------------------------------------------

################### Plot das Texturas nos arquivos ".agr" ##############

       if (e == -99 or e == 99 or e == 100) and (t <= 4 or t == 7):

          texturas.write("# Grace project file \n")
          texturas.write("# \n")
          texturas.write("@version 50122 \n")
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

              if (i == 1 and t <= 3):
                 grac='s0'; color = cor[2]          # Cor da componente Up dos Spins Sx, Sy e Sz.
              if (i == 2 and t <= 3):
                 grac='s1'; color = cor[3]          # Cor da componente Down dos Spins Sx, Sy e Sz.
              if (i == 3 and t <= 3):
                 grac='s2'; color = cor[1]          # Cor da componente Nula dos Spins Sx, Sy e Sz.
          
              if (i == 1 and t > 3):
                 grac='s0'; color = cor[t]          # Cor do Orbital S ou Px.
              if (i == 2 and t > 3):
                 grac='s1'; color = cor[t+1]        # Cor do Orbital P ou Py.
              if (i == 3 and t > 3):
                 grac='s2'; color = cor[t+2]        # Cor do Orbital D ou Pz.

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

       if (t <= 3):                            # Loop para a leitura dos valores Up, Down e Nulo das componentes de Spin (Sx, Sy e Sz).
          controle = 3                                    
       if (t > 3):
          controle = 1                         # Loop para a leitura dos valores nao-nulos dos Orbitais.

       for i in range (1,(controle+1)):

           if (e == 99 and t == 1) or (e == 100 and t == 1):
              temp = open("Temp_Spin_Sx_Excluir.txt", "r")
           if (e == 99 and t == 2) or (e == 100 and t == 2):
              temp = open("Temp_Spin_Sy_Excluir.txt", "r")
           if (e == 99 and t == 3) or (e == 100 and t == 3):
              temp = open("Temp_Spin_Sz_Excluir.txt", "r")
           if (e == -99 and t == 4) or (e == 100 and t == 4):
              temp = open("Temp_orb-S_Excluir.txt", "r")           
           if (e == -99 and t == 5) or (e == 100 and t == 5):
              temp = open("Temp_orb-P_Excluir.txt", "r")
           if (e == -99 and t == 6) or (e == 100 and t == 6):
              temp = open("Temp_orb-D_Excluir.txt", "r")
           if (e == -99 and t == 7) or (e == 100 and t == 7):
              temp = open("Temp_orb-Px_Excluir.txt", "r")
           if (e == -99 and t == 8) or (e == 100 and t == 8):
              temp = open("Temp_orb-Py_Excluir.txt", "r")
           if (e == -99 and t == 9) or (e == 100 and t == 9):
              temp = open("Temp_orb-Pz_Excluir.txt", "r")
      
#-----------------------------------------------------------------------

           if (t <= 3):
              for j in range (1,(num_tot+1)):
                  VTemp = temp.readline().split()
                  comp = float(VTemp[0]); auto_valor = float(VTemp[1]); raio = float(VTemp[2])
                  if (i == 1 and raio > 0.0):
                     texturas.write(f'{comp} {auto_valor} {raio} \n')
                  if (i == 2 and raio < 0.0):
                     texturas.write(f'{comp} {auto_valor} {raio} \n')
                  if (i == 3 and raio == 0.0):
                     texturas.write(f'{comp} {auto_valor} {raio} \n')
           if (t > 3):
              for j in range (1,(num_tot+1)):
                  VTemp = temp.readline().split()
                  comp = float(VTemp[0]); auto_valor = float(VTemp[1]); raio = float(VTemp[2])
                  if (raio > 0.0):
                     texturas.write(f'{comp} {auto_valor} {raio} \n')
          
           texturas.write(" \n")
      
           temp.close()        

#-----------------------------------------------------------------------

       if (t <= 3 or t == 6 or t == 9):
      
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

# Reduzindo o tamanho dos arquivos temporarios gerados.

if (lorbit == 10):
   if (e == -99) or (e == 100):
      Orbital_S = open("Temp_orb-S_Excluir.txt", "w")
      Orbital_P = open("Temp_orb-P_Excluir.txt", "w")
      Orbital_D = open("Temp_orb-D_Excluir.txt", "w")

if (lorbit > 10):
   if (e == -99) or (e == 100):
      Orbital_Px = open("Temp_orb-Px_Excluir.txt", "w")
      Orbital_Py = open("Temp_orb-Py_Excluir.txt", "w")
      Orbital_Pz = open("Temp_orb-Pz_Excluir.txt", "w")
      Orbital_S  = open("Temp_orb-S_Excluir.txt", "w")
      Orbital_P  = open("Temp_orb-P_Excluir.txt", "w")
      Orbital_D  = open("Temp_orb-D_Excluir.txt", "w")
        
if (SO == 2):
   if (e == 99) or (e == 100):
      Spin_Sx = open("Temp_Spin_Sx_Excluir.txt", "w")
      Spin_Sy = open("Temp_Spin_Sy_Excluir.txt", "w")
      Spin_Sz = open("Temp_Spin_Sz_Excluir.txt", "w")

if (e == -99) or (e == 100):
   Orbital_S.close()
   Orbital_P.close()
   Orbital_D.close()

if (lorbit > 10):
   if (e == -99) or (e == 100):
      Orbital_Px.close()
      Orbital_Py.close()
      Orbital_Pz.close()

if (SO == 2):
   if (e == 99) or (e == 100):      
      Spin_Sx.close()
      Spin_Sy.close()
      Spin_Sz.close()

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################