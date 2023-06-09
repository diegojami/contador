import time
import csv

# define o cabeçalho da planilha
header = ['Atividade', 'Horas']

# cria uma lista para armazenar as atividades
atividades = []

# função para iniciar o cronômetro
def iniciar_cronometro():
    input('Pressione enter para iniciar o cronômetro...')
    start_time = time.time()
    input('Pressione enter para parar o cronômetro...')
    end_time = time.time()
    tempo_gasto = round(end_time - start_time, 2)
    descricao_atividade = input('Descreva a atividade: ')
    # adiciona a atividade à lista
    atividades.append([descricao_atividade, tempo_gasto])
    print(f'Tempo gasto na atividade "{descricao_atividade}": {tempo_gasto} segundos')
    input('Pressione enter para continuar...')

# função para exportar a planilha
def exportar_planilha():
    with open('horas_trabalhadas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerows(atividades)
    print('Planilha exportada com sucesso!')

# loop principal do programa
while True:
    print('\n*** Sistema de Controle de Horas de Trabalho ***\n')
    print('Escolha uma opção:')
    print('1 - Iniciar cronômetro')
    print('2 - Exportar planilha de horas trabalhadas')
    print('3 - Sair')
    opcao = input('Opção: ')
    if opcao == '1':
        iniciar_cronometro()
    elif opcao == '2':
        exportar_planilha()
    elif opcao == '3':
        print('Concluido)')
