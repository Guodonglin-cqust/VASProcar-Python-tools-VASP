
print ("")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Versao 4.006 (02/09/2021) %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
print ("Autor: Augusto de Lelis Araújo - INFIS/UFU (Uberlandia/MG)")
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

entrada = open("input_Localizacao.txt", "r")

for i in range(6):
    VTemp = entrada.readline()
Dimensao = int(VTemp) 

for i in range(3):
    VTemp = entrada.readline()
peso_total = float(VTemp)                                              # Tamanho/Peso das esferas do grafico.

for i in range(3):
    VTemp = entrada.readline()
Destacado = float(VTemp)                                               # Contribuicao mínima a ser plotada.

# for i in range(5):
#     VTemp = entrada.readline()                                         # 0 para Plotar todas as Bandas.
# esc = int(VTemp)   # ions analisados                                   # 1 para Plotar Bandas selecionadas.

# if (esc != 0 and esc != 1):
#    esc = 0

# if (esc == 1):
#    for i in range(3):
#        VTemp = entrada.readline()
#    Band_i = int(VTemp)                                                 # Banda inicial a ser Plotada. 
#
#    for i in range(3):
#        VTemp = entrada.readline()
#    Band_f = int(VTemp)                                                 # Banda final a ser Plotada.

esc = 0
esc_b = 1
destacar_efermi = 1
destacar_pontos_k = 1

#-----------------------------------------------------------------------

################### Obtendo o nº de arquivos PROCAR: ###################

try: f = open('PROCAR'); f.close(); n_procar = 1
except: 0 == 0
try: f = open('PROCAR.1'); f.close(); n_procar = 1
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

####################### Leitura do Arquivo PROCAR ######################

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
   print (" ")
   
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

contcar.close()

#-----------------------------------------------------------------------
# Obtendo os rótulos dos ions presentes no arquivo CONTCAR.
#-----------------------------------------------------------------------

contcar = open("CONTCAR", "r")

for i in range(6):
    VTemp = contcar.readline().split() 
types = len(VTemp)                                                     # Obtenção do número de diferentes tipos de ions que compoem a rede.

#----------------------------------------------

label = [0]*(types+1)
ion_label = [0]*(ni+1)
rotulo = [0]*(ni+1)
rotulo_temp = [0]*(ni+1)

#----------------------------------------------

for i in range (1,(types+1)):
    label[i] = VTemp[(i-1)]                                            # Obtenção dos rótulos/abreviações que rotulam cada tipo de ion da rede.

VTemp = contcar.readline().split()                                    

for i in range (1,(types+1)):            
    ion_label[i] = int(VTemp[(i-1)])                                   # Obtenção do número de ions correspondentes a cada rótulo/abreviação.

contcar.close()

#----------------------------------------------

contador = 0

for i in range (1,(types+1)):
    number = ion_label[i]
    for j in range (1,(number+1)):
        contador += 1
        rotulo[contador] = label[i]

#----------------------------------------------------------------------

if (esc == 0):
   Band_i = 1                                                          # Banda inicial a ser Plotada.
   Band_f = nb                                                         # Banda final a ser Plotada.
   point_i = 1                                                         # Ponto-k inicial a ser Plotado.
   point_f = nk                                                        # Ponto-k final a ser Plotado.

nbb = (Band_f - Band_i) + 1

#-----------------------------------------------------------------------

# Inicialização de vetores e matrizes

atomo = [0]*(ni+1)
Contrib = [0]*(ni+1)
ABC = [0]*(ni+1)
Reg = [0]*(ni+1)
u = [0]*4
           
#-----------------------------------------------------------------------

VTemp = entrada.readline()
VTemp = entrada.readline()

for i in range (1,(ni+1)):
    ABC[i] = "C"

VTemp = entrada.readline().split()
loop = int(VTemp[0])    

for i in range (1,(loop+1)):
    VTemp = entrada.readline().split()
    loop_i = int(VTemp[0]); loop_f = int(VTemp[1]); loop_cha = VTemp[2]
    if (loop_i > ni or loop_f > ni):
       print("==========================================================")
       print("O arquivo Localizacao.txt esta configurado incorretamente.")
       print("==========================================================")
       print(" ")
    for i in range (loop_i,(loop_f+1)):
        ABC[i] = loop_cha

#--------------
entrada.close()
#--------------
      
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



print (" ")
print ("Rodando: ##############################################")
print ("####### Rodando: ######################################")
print ("############### Rodando: ##############################")
print ("####################### Rodando: ######################")
print ("############################### Rodando: ##############")
print ("####################################### Rodando: ######")
print ("############################################## Rodando:")
print (" ")
print (" ")

Band_antes  = (Band_i - 1)                                             # Bandas que nao serao plotadas.
Band_depois = (Band_f + 1)                                             # Bandas que nao serao plotadas.

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

#-----------------------------------------------------------------------
temp = open("Temp.txt", "w")
contribuicao = open("Contribuicao_das_Regiões.txt", "w")
#-----------------------------------------------------------------------

########################## Loop dos PROCAR #############################

n_point_k = 0
energ = 0.0

################# Inicialização de Vetores e Matrizes: #################
                                              
xx = [[0]*(nk+1) for i in range(n_procar+1)]
kx = [[0]*(nk+1) for i in range(n_procar+1)]
ky = [[0]*(nk+1) for i in range(n_procar+1)]
kz = [[0]*(nk+1) for i in range(n_procar+1)]
separacao = [[0]*(nk+1) for i in range(n_procar+1)]
y = [[[0]*(nb+1) for i in range(nk+1)] for j in range(n_procar+1)]

#----------------------------------------------------------------------

for wp in range (1,(n_procar+1)):
      
    contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
    contribuicao.write(f'PROCAR {wp} \n')
    contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
    contribuicao.write(" \n")

    if (wp == 1 and n_procar == 1):
       procar = open("PROCAR", "r") 
    if (wp == 1 and n_procar != 1):
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
      
######################## Loop dos Pontos_k ############################
                                                                      # Observacao: No VASP k_b1, k_b2 e k_b3 correspondem as coordenadas diretas de cada ponto-k na ZB, 
    for point_k in range(1, (nk+1)):                                  # suas coordenadas cartesianas sao obtidas por meio das relacoes abaixo que nos fornecem kx = Coord_X, 
                                                                      # ky = Coord_Y e kz = Coord_Z, entretanto, devemos nos lembrar que estas coordenadas kx, ky e kz estao 
        VTemp = procar.readline().split()                             # em unidades de 2pi/Parametro.
        k_b1 = float(VTemp[3])
        k_b2 = float(VTemp[4])
        k_b3 = float(VTemp[5]) 
        
        VTemp = procar.readline()
        
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(f'K_Point {point_k} \n')
        contribuicao.write("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% \n")
        contribuicao.write(" \n")
      
################ Distancia de separacao entre os pontos-k ##############

        Coord_X = ((k_b1*B1x) + (k_b2*B2x) + (k_b3*B3x))
        Coord_Y = ((k_b1*B1y) + (k_b2*B2y) + (k_b3*B3y))
        Coord_Z = ((k_b1*B1z) + (k_b2*B2z) + (k_b3*B3z))

        kx[wp][point_k] = Coord_X       
        ky[wp][point_k] = Coord_Y
        kz[wp][point_k] = Coord_Z  

        if (wp == 1) and (point_k == 1):
           comp = 0.0
           xx[wp][point_k] = comp 

        if (wp != 1) or (point_k != 1):
           delta_X = Coord_X_antes - Coord_X
           delta_Y = Coord_Y_antes - Coord_Y
           delta_Z = Coord_Z_antes - Coord_Z
           comp = (delta_X**2 + delta_Y**2 + delta_Z**2)**0.5
           comp = comp + comp_antes
           xx[wp][point_k] = comp

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

########################### Loop das Bandas ############################

        for Band_n in range (1, (nb+1)):

            Band_nn = float(Band_n)                                    # Converte a variavel inteira (Band_n) para o tipo real.

            if (esc_b == 1):
               criterio_2 = (Band_n/1.0)

            if (esc_b != 1):
               criterio_2 = (Band_n/2.0)

            int_crit_2 = int(criterio_2)                               # Retorna a parte inteira do numero real (criterio_2).
            resto_crit_2 = (criterio_2 % 1.0)                          # Retorna a parte fracionaria do numero real (criterio_2).
          
            if (esc_b == 1) or (esc_b == 2):                           # (esc_b == 1) Condicao para plotar/analisar todas as bandas (pares e impares).
               rest = 0.0                                              # (esc_b == 2) Condicao para plotar/analisar somente as bandas pares.
               
            if (esc_b == 3):
               rest = 0.5                                              # (esc_b == 3) Condicao para plotar/analisar somente as bandas impares.

            if (Band_n > Band_antes and Band_n < Band_depois and resto_crit_2 == rest):
               VTemp = procar.readline().split()
               energ =  float(VTemp[4])
            
            if (Band_n == Band_i):
               contribuicao.write("==================================================== \n")

            contribuicao.write(f'Banda {Band_n} \n')
            contribuicao.write("==================================================== \n")

########################## Ajuste das energias #########################

            if (wp == 1):                                              # y(1,1,1)                                 
               dE  = (Efermi)*(-1)
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 2):
               if (point_k == point_i) and (Band_n == Band_i):         # y(2,1,1)
                  dE  = y[1][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 3):
               if (point_k == point_i) and (Band_n == Band_i):         # y(3,1,1)
                  dE  = y[2][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 4):
               if (point_k == point_i) and (Band_n == Band_i):         # y(4,1,1)
                  dE  = y[3][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = float(energ) + flost(dE)
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 5):
               if (point_k == point_i) and (Band_n == Band_i):         # y(5,1,1)
                  dE  = y[4][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 6):
               if (point_k == point_i) and (Band_n == Band_i):         # y(6,1,1)
                  dE  = y[5][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 7):
               if (point_k == point_i) and (Band_n == Band_i):         # y(7,1,1)
                  dE  = y[6][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 8):
               if (point_k == point_i) and (Band_n == Band_i):         # y(8,1,1)
                  dE  = y[7][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 9):
               if (point_k == point_i) and (Band_n == Band_i):         # y(9,1,1)
                  dE  = y[8][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

            if (wp == 10):
               if (point_k == point_i) and (Band_n == Band_i):         # y(10,1,1)
                  dE  = y[9][point_f][Band_i] - energ
               y[wp][point_k][Band_n] = energ + dE
               auto_valor = y[wp][point_k][Band_n]

########################################################################

            if (energ_max < auto_valor):                               # Calculo do maior auto-valor de energia.
               energ_max = auto_valor

            if (energ_min > auto_valor):                               # Calculo do menor auto-valor de energia.
               energ_min = auto_valor
              
            VTemp = procar.readline()
            VTemp = procar.readline()  
          
            orb_total = 0.0
            Lado_A = 0.0
            Lado_B = 0.0
            Centro = 0.0
            Prop_A = 0.0
            Prop_B = 0.0
            Prop_C = 0.0
            Soma = 0.0
            Soma_A = 0.0
            Soma_B = 0.0
            Soma_C = 0.0
            
############################ Loop dos ions #############################

#====================== Lendo o Orbital Total ==========================

            for ion_n in range (1, (ni+1)):
                atomo[ion_n] = ion_n
                temp_sm = ABC[ion_n]
                Reg[ion_n] = ABC[ion_n]

                if (temp_sm == "A"):
                   if (lorbit >= 11):
                      VTemp = procar.readline().split()
                      ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                      dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                      VTemp = procar.readline().split() 
                      ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Lado_A = Lado_A + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_A = Soma_A + Contrib[ion_n]

                if (temp_sm == "B"):
                   if (lorbit >= 11):
                       VTemp = procar.readline().split()
                       ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                       dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                       VTemp = procar.readline().split() 
                       ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Lado_B = Lado_B + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_B = Soma_B + Contrib[ion_n]

                if (temp_sm == "C"):
                   if (lorbit >= 11):
                       VTemp = procar.readline().split()
                       ion = int(VTemp[0]); s = float(VTemp[1]); py = float(VTemp[2]); pz = float(VTemp[3]); px = float(VTemp[4])
                       dxy = float(VTemp[5]); dyz = float(VTemp[6]); dz2 = float(VTemp[7]); dxz = float(VTemp[8]); dx2 = float(VTemp[9]); tot = float(VTemp[10])
                   if (lorbit == 10):
                       VTemp = procar.readline().split() 
                       ion = int(VTemp[0]); s = float(VTemp[1]); p = float(VTemp[2]); d = float(VTemp[3]); tot = float(VTemp[4])
                   #-----------------------------
                   Centro = Centro + tot
                   orb_total = orb_total + tot
                   Contrib[ion_n] = tot
                   Soma_C = Soma_C + Contrib[ion_n]

#-----------------------------------------------------------------------

            peso_inicial = 0.0

            if (orb_total != 0.0):
               Prop_A = ((Lado_A/orb_total) + peso_inicial)*peso_total
               Prop_B = ((Lado_B/orb_total) + peso_inicial)*peso_total
               Prop_C = ((Centro/orb_total) + peso_inicial)*peso_total
            if (orb_total == 0.0):
               Prop_A = 0.0
               Prop_B = 0.0

            temp.write(f'{comp} {auto_valor} {Prop_A} {Prop_B} {Prop_C} \n')
      
#-----------------------------------------------------------------------
            if (orb_total != 0.0):
               Soma_A = (Soma_A/orb_total)*100
               Soma_B = (Soma_B/orb_total)*100
               Soma_C = (Soma_C/orb_total)*100
            if (orb_total == 0.0):
               Soma_A = 0.0
               Soma_B = 0.0
               Soma_C = 0.0

            contribuicao.write(f'Regiao A = {Soma_A:7,.3f}% \n')
            contribuicao.write(f'Regiao B = {Soma_B:7,.3f}% \n')
            contribuicao.write(f'Regiao C = {Soma_C:7,.3f}% \n')
            contribuicao.write("=================== \n")
            
#-----------------------------------------------------------------------

            for j in range (1,(ni+1)):
               rotulo_temp[j] = rotulo[j]

            nj = (ni - 1)
                     
            for k in range (1,(nj+1)):
                wy = (ni - k)
                for l in range (1,(wy+1)):
                    if (Contrib[l] < Contrib[l+1]):
                     tp1 = Contrib[l]
                     Contrib[l] = Contrib[l+1]
                     Contrib[l+1] = tp1
                     #--------------------
                     tp2 = atomo[l]
                     atomo[l] = atomo[l+1]
                     atomo[l+1] = tp2
                     #--------------------                    
                     tp3 = Reg[l]
                     Reg[l] = Reg[l+1]
                     Reg[l+1] = tp3
                     #--------------------
                     tp4 = rotulo_temp[l]
                     rotulo_temp[l] = rotulo_temp[l+1]
                     rotulo_temp[l+1] = tp4                     

            for ion_n in range (1,(ni+1)):
                Contrib[ion_n] = (Contrib[ion_n]/orb_total)*100
                Soma = Soma + Contrib[ion_n]
                
                if (Reg[ion_n] == "A"):
                   palavra = "(Regiao A)"
                if (Reg[ion_n] == "B"):
                   palavra = "(Regiao B)"
                if (Reg[ion_n] == "C"):
                   palavra = "(Regiao C)"

                contribuicao.write(f'{rotulo_temp[ion_n]:>2}: ion {atomo[ion_n]:<3} | Contribuicao: {Contrib[ion_n]:6,.3f}% | Soma: {Soma:>7,.3f}% | {palavra} \n')

            contribuicao.write(" \n")

#-----------------------------------------------------------------------

#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%% Analisandos os Orbitais %%%%%%%%%%%%%%%%%%%%%%%%%%%
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

            VTemp = procar.readline()

#***********************************************************************
#     Condicao para calculo com acoplamento Spin-Orbita.
#***********************************************************************

            if (SO == 2):
#================================ Sx ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()

#================================ Sy ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()

#================================ Sz ===================================

               for ion_n in range (1, (ni+1)):
                   VTemp = procar.readline()

               VTemp = procar.readline()


#============= Pulando as linhas referente a fase (LORBIT 12) ==========

               if (lorbit == 12):
                  temp2 = ((2*ni) + 2)
                  for i in range (1, (temp2 + 1)):
                      VTemp = procar.readline()

               if (lorbit != 12):
                  VTemp = procar.readline()
              
               if (Band_n < Band_f):
                  contribuicao.write("==================================================== \n")

#==================== Bandas excluidas do calculo ======================

            if (Band_n <= Band_antes and Band_n >= Band_depois and resto_crit_2 == rest): # Continuacao do if que regula as Bandas que serao plotadas ou nao.          

               if (lorbit == 12):                                      # Valido somente para LORBIT = 12.
                  if (SO == 1):                                        # Para calculo sem acoplamento Spin-Orbita.
                     temp3 = 6 + 3*ni
                  if (SO == 2):                                        # Para calculo com acoplamento Spin-Orbita.
                     temp3 = 9 + 6*ni

               if (lorbit != 12):                                      # Valido somente para LORBIT = 1O ou 11.
                  if (SO == 1):                                        # Para calculo sem acoplamento Spin-Orbita.
                     temp3 = 5 + ni
                  if (SO == 2):                                        # Para calculo com acoplamento Spin-Orbita.
                     temp3 = 8 + 4*ni

               for i in range (1,(temp3+1)):                           # Esta parte do codigo pula/exclui as Bandas de energia em cada ponto K, que nao foram selecionadas para serem plotadas.
                   VTemp = procar.readline()                               

#================== Ignorar linhas ao final de cada K point ============

        if (point_k < nk):
            VTemp = procar.readline()

        
    #-----------------------------------------------------------------------
    # Fim do laço/loop dos pontos-k ----------------------------------------
    #-----------------------------------------------------------------------

#-----------------------------------------------------------------------
# Fim do laço/loop dos procar ------------------------------------------
#-----------------------------------------------------------------------

    procar.close()

temp.close()
contribuicao.close()

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
# y_final   = y_final   + delta

############ Plot das Bandas no arquivo "Estrutura_de_Bandas.agr" ######

# Instruções para o GRACE ler o arquivo "Estrutura_de_Bandas.agr" #####

bandas = open("Estrutura_de_Bandas.agr", "w")

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
bandas.write("@    view 0.1, 0.075, 0.6, 0.95 \n")

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
   bandas.write(f'{xx[n_procar][nk]} 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas.

if (destacar_pontos_k == 1):
   for loop in range (1,(contador2+1)):
       bandas.write(" \n")
       bandas.write(f'{dest_pk[loop]} {energ_min} \n')
       bandas.write(f'{dest_pk[loop]} {energ_max} \n')

# Destacando alguns pontos-K de interesse, na Estrutura de Bandas.

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

bandas.close()

#-----------------------------------------------------------------------

print (" ")
print ("########################################################")
print ("############# Processando os Resultados ################")
print ("########################################################")
print (" ")

########################################################################
################## Agora sera escrito o arquivo de saida ###############
########################################################################

localizacao = open("Localizacao_dos_estados.agr", "w")

######## Plot da Localizacao no arquivo "Localizacao_dos_estados.agr" ##

localizacao.write("# Grace project file \n")
localizacao.write("# \n")
localizacao.write("@version 50122 \n")
localizacao.write("@with string \n")
localizacao.write("@    string on \n")
localizacao.write("@    string 0.1, 0.96 \n")
localizacao.write(f'@    string def "E(eV)" \n')
localizacao.write("@with string \n")
localizacao.write("@    string on \n")

if (Dimensao == 1):
   localizacao.write("@    string 0.66, 0.017 \n")
   localizacao.write(f'@    string def "(2pi/Param.)" \n')
if (Dimensao == 2):
   localizacao.write("@    string 0.70, 0.017 \n")
   localizacao.write(f'@    string def "(1/Angs.)" \n')
if (Dimensao == 3):
   localizacao.write("@    string 0.73, 0.017 \n")
   localizacao.write(f'@    string def "(1/nm)" \n')

localizacao.write("@with g0 \n")
localizacao.write(f'@    world {x_inicial}, {y_inicial}, {x_final}, {y_final} \n')
localizacao.write("@    view 0.1, 0.075, 0.8, 0.95 \n")

escala_x = (x_final - x_inicial)/5
escala_y = (y_final - y_inicial)/5

localizacao.write(f'@    xaxis  tick major {escala_x:.2f} \n')
localizacao.write(f'@    yaxis  tick major {escala_y:.2f} \n')

# Obs.: Codigo das cores
# Codigo de cores para a localizacao dos estados nas regioes A, B e C
# Branco=0, Preto=1, Vermelho=2, Verde=3, Azul=4, Amarelo=5, Marrom=6, Cinza=7
# Violeta=8, Cyan=9, Magenta=10, Laranja=11, Indigo=12, Marron=13, Turquesa=14

cor_A = 4
cor_B = 2
cor_C = 3

for i in range (1,(3+1)):
    if (i == 1):
       grac='s0'; color = cor_A
    if (i == 2):
       grac='s1'; color = cor_B
    if (i == 3):
       grac='s2'; color = cor_C

    localizacao.write(f'@    {grac} type xysize \n')
    localizacao.write(f'@    {grac} symbol 1 \n')
    localizacao.write(f'@    {grac} symbol color {color} \n')
    localizacao.write(f'@    {grac} symbol fill color {color} \n')
    localizacao.write(f'@    {grac} symbol fill pattern 1 \n')
    localizacao.write(f'@    {grac} line type 0 \n')
    localizacao.write(f'@    {grac} line color {color} \n')

localizacao.write("@type xysize \n")
# localizacao.write(" \n")

#-----------------------------------------------------------------------

wm = 1
wn = 3

for t in range (wm,(wn+1)):

    if (t == 1):
       print ("Analisando a Localizacao dos Estados (Regiao A)")
    if (t == 2):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao B)")
    if (t == 3):
       print (" ")
       print ("Analisando a Localizacao dos Estados (Regiao C)")

#-----------------------------------------------------------------------
    num_tot = n_procar*(nk*nbb)
#-----------------------------------------------------------------------

    temp = open("Temp.txt", "r")

#-----------------------------------------------------------------------

    for j in range (1,(num_tot+1)):
        VTemp = temp.readline().split()
        cp = float(VTemp[0]); av = float(VTemp[1]); u[1] = float(VTemp[2]); u[2] = float(VTemp[3]); u[3] = float(VTemp[4]);   
        if (u[t] > Destacado):
           localizacao.write(f'{cp} {av} {u[t]} \n')

    localizacao.write(" \n")

    temp.close()

###################### Plot da Estrutura de Bandas ######################

for Band_n in range (Band_i,(Band_f+1)):
    localizacao.write(" \n")
    for i in range (1,(n_procar+1)):
        for point_k in range (1,(nk+1)):
            localizacao.write(f'{xx[i][point_k]} {y[i][point_k][Band_n]} 0.0 \n')

# Destacando a Energia de Fermi na Estrutura de Bandas.
      
if (destacar_efermi == 1):
   localizacao.write(" \n")
   localizacao.write(f'{xx[1][1]} 0.0 0.0 \n')
   localizacao.write(f'{xx[n_procar][nk]} 0.0 0.0 \n')

# Destacando pontos-k de interesse na estrutura de Bandas.

if (destacar_pontos_k == 1):
   for loop in range (1,(contador2+1)):
       localizacao.write(" \n")
       localizacao.write(f'{dest_pk[loop]} {energ_min} 0.0 \n')
       localizacao.write(f'{dest_pk[loop]} {energ_max} 0.0 \n')

# Destacando alguns pontos-K de interesse, na Estrutura de Bandas.

if (n_procar > 1):
   wr = n_procar + 1
   for loop in range (1,(wr+1)):
       localizacao.write(" \n")
       if (loop != wr):
          localizacao.write(f'{xx[loop][1]} {energ_min} 0.0 \n')
          localizacao.write(f'{xx[loop][1]} {energ_max} 0.0 \n')
       if (loop == wr):
          localizacao.write(f'{xx[n_procar][nk]} {energ_min} 0.0 \n')
          localizacao.write(f'{xx[n_procar][nk]} {energ_max} 0.0 \n')

#-----------------------------------------------------------------------
localizacao.close()
#-----------------------------------------------------------------------

temp = open("Temp.txt", "w")
temp.close()

############################################################################################################################################################################################
############################################################################################################################################################################################
#######
####### FIM DO CÓDIGO ######################################################################################################################################################################
#######
############################################################################################################################################################################################
############################################################################################################################################################################################
