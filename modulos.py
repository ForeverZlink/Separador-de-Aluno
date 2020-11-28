def linha():
    print('='*40)

def leia_data(texto):
    while True:
        inform=leiaint(texto)
        if inform<31:
            return inform
        else:
            print('Não existe mais do que 31 dias no mês!')
            linha()
def leia_mes(texto):
    while True:
        mes=leiaint(texto)
        if mes<=12:
            return mes
        else:
            print('Não existe mais do que 12 meses! ')
            linha()
def leia_ano(texto):
    from datetime import date
    while True:
        inform=leiaint(texto)
        if inform>date.today().year or inform<1930:
            
            print('Impossivel ter nascido nesse ano!')
            linha()
        else:
            return inform




def leia_opção(text):
    while True:
        numero=leiaint(text)
        
        if numero!= 0 and numero!= 1:
            print('Digite apenas 0 ou 1')
            linha()
        else:
            return numero

def tabela(valor):
    for turno in valor:
        for nomedasala,sala in turno.items():
            if not sala == []:
                print(f'{"Sala":>14}{nomedasala:>1}')
                linha()
            for lista in sala:
                if lista['Turno']==0:
                    lista['Turno']='Manhã'
                else:
                    lista['Turno']='Tarde'
                for keys, aluno in lista.items():
                    print(f'{keys:<25}{aluno}')
                    linha()



def leiaint(texto):
    while True:
        numero=str(input(texto))
        if numero.isnumeric():
            return int(numero)
        else:
            linha()
            print('NÃO É NUMERICO! DIGITE NOVAMENTE')

def separador_de_salas(valores):
    vagas_por_turno=10
    contador=0
    conttarde=5
    capacidade_de_alunos_da_sala_manhã=0
    capacidade_de_alunos_da_sala_tarde=0
    manha={'2000':[],'2001':[],'2002':[],'2003':[],'2004':[]}
    tarde={'2005':[],'2006':[],'2007':[],'2008':[],'200':[]}
    for values in valores:
       if capacidade_de_alunos_da_sala_manhã<=vagas_por_turno and values['Turno']==0:
            manha[f'200{contador}'].append(values.copy())
            capacidade_de_alunos_da_sala_manhã+=1
            if capacidade_de_alunos_da_sala_manhã==2:
                contador+=1
                capacidade_de_alunos_da_sala_manhã=0

       if capacidade_de_alunos_da_sala_tarde<=vagas_por_turno and values['Turno']==1:
            tarde[f'200{conttarde}'].append(values.copy())
            if capacidade_de_alunos_da_sala_tarde==2:
                capacidade_de_alunos_da_sala_tarde=0
                conttarde+=1
    return manha,tarde



        


