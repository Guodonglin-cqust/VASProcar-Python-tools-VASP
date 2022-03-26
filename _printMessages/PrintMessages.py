
def authors_information():
    print(" ")
    print("##########################################################################")
    print("# VASProcar -- https://github.com/Augusto-Dlelis/VASProcar-Tools-Python ##")
    print("# Autores: ###############################################################")
    print("# ===================================================================== ##")
    print("# Augusto de Lelis Araujo                                               ##")
    print("# Federal University of Uberlandia (Uberlândia/MG - Brazil)             ##")
    print("# e-mail: augusto-lelis@outlook.com                                     ##")
    print("# ===================================================================== ##")
    print("# Renan da Paixão Maciel                                                ##")
    print("# Uppsala University (Uppsala/Sweden)                                   ##")
    print("# e-mail: renan.maciel@physics.uu.se                                    ##")
    print("##########################################################################")
    print(" ")

def minimal_requirement_to_run():
    print("###############################################################")
    print("## Arquivos básicos: CONTCAR, OUTCAR e PROCAR -------------- ##")
    print("## Dependendo do calculo: DOSCAR, LOCPOT ou WAVECAR -------- ##")
    print("###############################################################")   
    print(" ")
    print("###############################################################")
    print("## Observacao: --------------------------------------------- ##")
    print("## Alguma configuracoes do codigo podem ser alteradas no     ##")
    print("## arquivo ''_configuracoes.py'', como por exemplo o formato ##")
    print("## de saida (.png, .pdf, .eps) dos Plot via Matplotlib       ##")
    print("###############################################################")
    print(" ")
    
def wait():
    print("##############################################################")
    print("# Obtendo informacoes da rede e do calculo efetuado: ======= #")
    print("##############################################################")
    print(".........................")
    print("... Espere um momento ...")
    print(".........................")
    print(" ")

def general_info_part1():  
   print("##############################################################")
   print("################### O que deseja calcular? ###################")
   print("##############################################################")
   print("## [1] Estrutura de Bandas (Plot 2D, 3D, isosuperficie,     ##")
   print("##                   Superficie de Fermi e Curvas de Nivel) ##")
   print("## ======================================================== ##")    
    
def print_SO_information():
   print("## -------------------------------------------------------- ##")
   print("## Plot 2D das Componentes Sx|Sy|Sz em [k-points, E(eV)]    ##")
   print("## [2] Padrao   --   [-2] Personalizado                     ##")
   print("## -------------------------------------------------------- ##")
   print("## Projecoes 2D|3D|Isosuperficie das Componentes Sx|Sy|Sz   ##")
   print("## e dos vetores SiSj e SxSySz                              ##")
   print("## [21] Padrao  --   [-21] Personalizado                    ##")
   print("## ======================================================== ##")
   print("## Plot das Componentes Sx|Sy|Sz ao longo de uma dada Banda ##")
   print("## e Curva de Nivel (Energia constante).                    ##")
   print("## [22] Padrao  --   [-22] Personalizado                    ##")
   print("## ======================================================== ##")
  
def general_info_part2():   
   print("## Projecao dos Orbitais S, P e D (Plot 2D):                ##")       
   print("## [3]: Configuracao Padrao   --   [-3]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## DOS, p-DOS e l-DOS (Plot 2D):                            ##")
   print("## [4]: Configuracao Padrao   --   [-4]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## Projecao da Localizacao dos estados em regioes (Plot 2D) ##")
   print("## [5]: Configuracao Padrao   --   [-5]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## Contribuicao de Orbitais e ions nos estados (Tabela):    ##")
   print("## [6]: Configuracao Padrao   --   [-6]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## Potencial Eletrostatico em X,Y,Z (Plot 2D):              ##")
   print("## [7]: Configuracao Padrao   --   [-7]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## Densidade de Carga Parcial em X,Y,Z (Plot 2D):           ##")
   print("## [8]: Configuracao Padrao   --   [-8]: Personalizado      ##")
   print("## ======================================================== ##")
   print("##           !!!!! EM TESTES - Nao Funcional !!!!!          ##")
   print("## Funcao de Onda em X,Y,Z - Parte Real e Imag. (Plot 2D):  ##")
   print("## [9]: Configuracao Padrao   --   [-9]: Personalizado      ##")
   print("## ======================================================== ##")
   print("## [777] Gerar arquivo KPOINTS (Plano 2D ou Malha 3D na ZB) ##")
   print("## ======================================================== ##")
   print("## [888] Efetuar verificacao e correcao de arquivos do VASP ##")
   print("##############################################################")
