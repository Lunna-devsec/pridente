from tinydb import TinyDB, Query
from datetime import datetime, timedelta
from time import sleep
from classes import add_presidente

def updater(presidente_id):
    # Implemente a lógica de atualização aqui
    print(f'Horário do presidente {presidente_id} atualizado.')

def atualizar_horario(presidente_id):
    # Criar ou abrir o banco de dados
    with TinyDB('testers.json') as db:
        # Acessar a tabela 'presidente'
        tabela_presidente = db.table('presidente')

        # Obter o presidente pelo ID usando o método get
        presidente = tabela_presidente.get(Query().chave == presidente_id)

        # Verificar se o presidente foi encontrado
        if presidente:
            # Atualizar o campo 'time' para o novo valor (hora atual)
            novo_horario = datetime.now().strftime("%H:%M:%S")
            tabela_presidente.update({'time': novo_horario}, Query().chave == presidente_id)
            print(f'Horário do presidente {presidente_id} atualizado para {novo_horario}')
        else:
            print(f'Presidente com ID {presidente_id} não encontrado.')

def robo():
    with TinyDB('testers.json') as db:
        all_presidentes = db.table('presidente').all()

    for presidente in all_presidentes:
        hora_presidente = datetime.strptime(presidente['time'], "%H:%M:%S").time()
        hora_atual = datetime.now().time()

        # Imprimir as horas para debug
        print(f'Hora atual: {hora_atual}, Hora do presidente {presidente["chave"]}: {hora_presidente}')

        # Comparar diretamente os objetos datetime.time
        if hora_presidente < (datetime.combine(datetime.today(), hora_atual) - timedelta(seconds=10)).time():
            # Chame a função updater com o ID do presidente
            updater(presidente["chave"])

if __name__ == '__main__':
    add_presidente()

while True:
    sleep(5)
    robo()
