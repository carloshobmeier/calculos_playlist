
import os
import time


# FUNÇÕES

# limpar a tela do terminal
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# atraso para facilitar a leitura
def dormir():
    time.sleep(0.3)


# variáveis

quantidade_dados = 0

escolha_velocidade = ''
velocidade_reproducao = 1

total_horas = 0
total_minutos = 0
total_segundos = 0

horas_parciais = 0
minutos_parciais = 0
segundos_parciais = 0

tempo_total_em_horas = 0


# Boas vindas
limpar_tela()
print("\nSOFTWARE PARA CÁLCULO DE TEMPO DE PLAYLIST.")
dormir()
print("\nResponda as seguintes perguntas:\n")
dormir()

quantidade_itens = int(input("- Quantos itens tem na playlist: "))


# possível aceleração de velocidade:
escolha_velocidade = input("- Você vai assistir a playlist com alteração de velocidade [s/_]: ")
if escolha_velocidade ==  's' or escolha_velocidade == 'S' or escolha_velocidade == 'sim' or escolha_velocidade == "Sim":
    velocidade_reproducao = input("- Qual a velocidade em que irá assistir (ex: 1.8): ")
    velocidade_reproducao = velocidade_reproducao.replace(",", ".") # tratamento caso o usuário digite com vírgula
    velocidade_reproducao = float(velocidade_reproducao)


# informe quais serão os dados fornecidos:
informar_horas = input("\n- Você vai informar dados de hora [s/_]: ")
informar_minutos = input("- Você vai informar dados de minutos [s/_]: ")
informar_segundos = input("- Você vai informar dados de segundos [s/_]: ")


# avalia quantos dados serão passados:
if informar_horas == 's' or informar_horas == 'S' or informar_horas == 'sim' or informar_horas == "Sim":
    quantidade_dados += 1
if informar_minutos == 's' or informar_minutos == 'S' or informar_minutos == 'sim' or informar_minutos == "Sim":
    quantidade_dados += 1
if informar_segundos == 's' or informar_segundos == 'S' or informar_segundos == 'sim' or informar_segundos == 'Sim':
    quantidade_dados += 1


# tratamento para saída do que deve ser informado:
if informar_horas == 's' or informar_horas == 'S' or informar_horas == 'sim' or informar_horas == "Sim":
    dado_horas = " Horas "
else:
    dado_horas = " "
if informar_minutos == 's' or informar_minutos == 'S' or informar_minutos == 'sim' or informar_minutos == "Sim":
    dado_minutos = " Minutos "
else:
    dado_minutos = " "
if informar_segundos == 's' or informar_segundos == 'S' or informar_segundos == 'sim' or informar_segundos == 'Sim':
    dado_segundos = " Segundos "
else:
    dado_segundos = " "


# impressão de relatório do que será feito:
total_dados = quantidade_dados * quantidade_itens
dormir()
print("\nA quantidade total de dados a serem digitados será:", total_dados)
dormir()
print("\nVocê informará", quantidade_dados, "dados por entrada. A saber:")
dormir()
print(f"{dado_horas}{dado_minutos}{dado_segundos}\n")    


# laço para alimentar os dados:
for cont in range(quantidade_itens):
    print(f"\n---ITEM {cont + 1}---")
    if informar_horas == 's' or informar_horas == 'S' or informar_horas == 'sim' or informar_horas == "Sim":
        horas_parciais = int(input(f"Horas: "))
        total_horas += horas_parciais
    if informar_minutos == 's' or informar_minutos == 'S' or informar_minutos == 'sim' or informar_minutos == "Sim":
        minutos_parciais = int(input(f"Minutos: "))
        total_minutos += minutos_parciais
    if informar_segundos == 's' or informar_segundos == 'S' or informar_segundos == 'sim' or informar_segundos == 'Sim':
        segundos_parciais = int(input(f"Segundos: "))
        total_segundos += segundos_parciais


# lógica para conversão de tempo sem aceleração:

# converte o total geral para horas:
tempo_total_em_horas = total_horas + (total_minutos / 60) + (total_segundos / 60 / 60)
tempo_total_guardado_em_horas = tempo_total_em_horas

# chegando no valor inteiro em horas
horas_inteiras = int(tempo_total_em_horas)

#chegando no valor inteiro em minutos
resto_horas = tempo_total_em_horas - horas_inteiras
minutos_convertidos = resto_horas * 60
minutos_inteiros = (int(minutos_convertidos))

# chegando no valor inteiro em segundos
resto_minutos = minutos_convertidos - minutos_inteiros
segundos_convertidos = resto_minutos * 60
segundos_inteiros = int(segundos_convertidos)


# articulando o plural/singular da saída:
concordancia_horas = ''
concordancia_minutos = ''
concordancia_segundos = ''
if horas_inteiras == 1:
    concordancia_horas = 'hora'
else:
    concordancia_horas = 'horas'
if minutos_inteiros == 1:
    concordancia_minutos = 'minuto'
else:
    concordancia_minutos = 'minutos'
if segundos_inteiros == 1:
    concordancia_segundos = 'segundo'
else:
    concordancia_segundos = 'segundos'


# impressão do resultado final dos cálculos sem aceleração:

# com velocidade padrão
print("\n\n------VELOCIDADE NORMAL-----")
print(f"\t{horas_inteiras} {concordancia_horas} \n\t{minutos_inteiros} {concordancia_minutos} \n\t{segundos_inteiros} {concordancia_segundos}")
print("----------------------------\n")



# lógica para conversão de tempo com aceleração:

if velocidade_reproducao > 1:

    # converte o total geral para horas:
    tempo_total_em_horas = tempo_total_guardado_em_horas  # resgata o tempo total expresso em horas
    tempo_total_em_horas = tempo_total_em_horas / velocidade_reproducao  # atualiza o tempo total em horas de acordo com a velocidade

    tempo_ganho = tempo_total_guardado_em_horas - tempo_total_em_horas  # armazena a diferença total em horas entre sem e com aceleração

    # chegando no valor inteiro em horas
    horas_inteiras = int(tempo_total_em_horas)

    #chegando no valor inteiro em minutos
    resto_horas = tempo_total_em_horas - horas_inteiras
    minutos_convertidos = resto_horas * 60
    minutos_inteiros = (int(minutos_convertidos))

    # chegando no valor inteiro em segundos
    resto_minutos = minutos_convertidos - minutos_inteiros
    segundos_convertidos = resto_minutos * 60
    segundos_inteiros = int(segundos_convertidos)


    # articulando o plural/singular da saída:
    concordancia_horas = ''
    concordancia_minutos = ''
    concordancia_segundos = ''
    if horas_inteiras == 1:
        concordancia_horas = 'hora'
    else:
        concordancia_horas = 'horas'
    if minutos_inteiros == 1:
        concordancia_minutos = 'minuto'
    else:
        concordancia_minutos = 'minutos'
    if segundos_inteiros == 1:
        concordancia_segundos = 'segundo'
    else:
        concordancia_segundos = 'segundos'

    # impressão do resultado final dos cálculos com aceleração:

    # com velocidade padrão
    print("\n----VELOCIDADE ACELERADA----")
    print(f"\t{horas_inteiras} {concordancia_horas} \n\t{minutos_inteiros} {concordancia_minutos} \n\t{segundos_inteiros} {concordancia_segundos}")
    print("----------------------------\n")


    # cálculo do tempo ganho com a aceleração:

    # converte o total geral para horas:
    tempo_total_em_horas = tempo_ganho

    # chegando no valor inteiro em horas
    horas_inteiras = int(tempo_total_em_horas)

    #chegando no valor inteiro em minutos
    resto_horas = tempo_total_em_horas - horas_inteiras
    minutos_convertidos = resto_horas * 60
    minutos_inteiros = (int(minutos_convertidos))

    # chegando no valor inteiro em segundos
    resto_minutos = minutos_convertidos - minutos_inteiros
    segundos_convertidos = resto_minutos * 60
    segundos_inteiros = int(segundos_convertidos)


    # articulando o plural/singular da saída:
    concordancia_horas = ''
    concordancia_minutos = ''
    concordancia_segundos = ''
    if horas_inteiras == 1:
        concordancia_horas = 'hora'
    else:
        concordancia_horas = 'horas'
    if minutos_inteiros == 1:
        concordancia_minutos = 'minuto'
    else:
        concordancia_minutos = 'minutos'
    if segundos_inteiros == 1:
        concordancia_segundos = 'segundo'
    else:
        concordancia_segundos = 'segundos'

    # impressão do resultado final dos cálculos com aceleração:

    # com velocidade padrão
    print("\n--------TEMPO GANHO---------")
    print(f"\t{horas_inteiras} {concordancia_horas} \n\t{minutos_inteiros} {concordancia_minutos} \n\t{segundos_inteiros} {concordancia_segundos}")
    print("----------------------------\n")



# lógica para conversão de tempo com desaceleração:

if velocidade_reproducao < 1:

    # converte o total geral para horas:
    tempo_total_em_horas = tempo_total_guardado_em_horas  # resgata o tempo total expresso em horas
    tempo_total_em_horas = tempo_total_em_horas / velocidade_reproducao  # atualiza o tempo total em horas de acordo com a velocidade

    tempo_perdido = tempo_total_em_horas - tempo_total_guardado_em_horas   # armazena a diferença total em horas entre sem e com desaceleração

    # chegando no valor inteiro em horas
    horas_inteiras = int(tempo_total_em_horas)

    #chegando no valor inteiro em minutos
    resto_horas = tempo_total_em_horas - horas_inteiras
    minutos_convertidos = resto_horas * 60
    minutos_inteiros = (int(minutos_convertidos))

    # chegando no valor inteiro em segundos
    resto_minutos = minutos_convertidos - minutos_inteiros
    segundos_convertidos = resto_minutos * 60
    segundos_inteiros = int(segundos_convertidos)


    # articulando o plural/singular da saída:
    concordancia_horas = ''
    concordancia_minutos = ''
    concordancia_segundos = ''
    if horas_inteiras == 1:
        concordancia_horas = 'hora'
    else:
        concordancia_horas = 'horas'
    if minutos_inteiros == 1:
        concordancia_minutos = 'minuto'
    else:
        concordancia_minutos = 'minutos'
    if segundos_inteiros == 1:
        concordancia_segundos = 'segundo'
    else:
        concordancia_segundos = 'segundos'

    # impressão do resultado final dos cálculos com desaceleração:

    # com velocidade padrão
    print("\n---VELOCIDADE DESACELERADA---")
    print(f"\t{horas_inteiras} {concordancia_horas} \n\t{minutos_inteiros} {concordancia_minutos} \n\t{segundos_inteiros} {concordancia_segundos}")
    print("---------------------------\n")


    # cálculo do tempo perdido com a desaceleração:

    # converte o total geral para horas:
    tempo_total_em_horas = tempo_perdido

    # chegando no valor inteiro em horas
    horas_inteiras = int(tempo_total_em_horas)

    #chegando no valor inteiro em minutos
    resto_horas = tempo_total_em_horas - horas_inteiras
    minutos_convertidos = resto_horas * 60
    minutos_inteiros = (int(minutos_convertidos))

    # chegando no valor inteiro em segundos
    resto_minutos = minutos_convertidos - minutos_inteiros
    segundos_convertidos = resto_minutos * 60
    segundos_inteiros = int(segundos_convertidos)


    # articulando o plural/singular da saída:
    concordancia_horas = ''
    concordancia_minutos = ''
    concordancia_segundos = ''
    if horas_inteiras == 1:
        concordancia_horas = 'hora'
    else:
        concordancia_horas = 'horas'
    if minutos_inteiros == 1:
        concordancia_minutos = 'minuto'
    else:
        concordancia_minutos = 'minutos'
    if segundos_inteiros == 1:
        concordancia_segundos = 'segundo'
    else:
        concordancia_segundos = 'segundos'

    # impressão do resultado final dos cálculos com aceleração:

    # com velocidade padrão
    print("\n-------TEMPO PERDIDO--------")
    print(f"\t{horas_inteiras} {concordancia_horas} \n\t{minutos_inteiros} {concordancia_minutos} \n\t{segundos_inteiros} {concordancia_segundos}")
    print("----------------------------\n")
