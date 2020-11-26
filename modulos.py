com=0
def tabela(valor):
    print(valor)
    global com
    com+=1
    print(f'           200{com}')
    for turno in valor:
        for sala in turno.values():
            for lista in sala:
                for keys, aluno in lista.items():
                    print(f'{keys:<25}{aluno}')
                print('='*56)



def leiaint(texto):
    while True:
        numero=str(input(texto))
        if numero.isnumeric():
            return int(numero)
        else:
            print('NÃO É NUMERICO! DIGITE NOVAMENTE')
 

def separador_de_salas(valores):
    print(valores)
    vagas_por_turno=10
    contador=0
    conttarde=5
    controle_de_manha=0
    controle_de_tarde=0
    manha={'2000':[],'2001':[],'2002':[],'2003':[],'2004':[]}
    tarde={'2005':[],'2006':[],'2007':[],'2008':[],'200':[]}
    for values in valores:
       if controle_de_manha<=vagas_por_turno and values['turno']==0:
            manha[f'200{contador}'].append(values.copy())
            controle_de_manha+=1
            if controle_de_manha==2 or 4 or 6 or 8 or 10:
                contador+=1

       if controle_de_tarde<=vagas_por_turno and values['turno']==1:
            tarde[f'200{conttarde}'].append(values)
            if controle_de_tarde==2 or 4 or 6 or 8 or 10:
                conttarde+=1
    return manha,tarde



        


