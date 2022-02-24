from datetime import  date, time, datetime, timedelta

def working_date():
    data_atual = date.today()
    print(data_atual.strftime('%d/%m/%Y'))
    print(data_atual.strftime('%A %B %Y'))

def working_time():
    horario = time(hour=15, minute=18, second=30)
    print(horario.strftime('%H:%M:%S'))
    print(type(horario))

def working_datetime():
    data_atual = datetime.now()
    print('Data Atual: {}'.format(data_atual))
    print('Data Convertida: {}'.format(data_atual.strftime('%d/%m/%Y')))
    print('Data Completa: {}'.format(data_atual.strftime('%d/%m/%Y %H:%M:%S')))
    print('Data Fulllll: {}'.format(data_atual.strftime('%c')))
    print('Data Half: {}'.format(data_atual.weekday()))
    print('Data Alterada: {}'.format(data_atual - timedelta(days=365, hours=16)))

    tupla = ('Segunda', 'Terça', 'Quarta', 'Quinta', 'Sexta', 'Sábado', 'Domingo')
    print(tupla[data_atual.weekday()])

if __name__ =='__main__':
    # working_date()
    # working_time()
    working_datetime()
