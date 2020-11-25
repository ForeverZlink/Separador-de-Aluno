manha={'2001':[],'2002':[],'2003':[],'2004':[]}
tarde={''}
cont=0
while True:
    cont+=1
    aluno=str(input('Nome do aluno:')).strip()
    matricula=int(input('Número da matricula:'))
    data_de_nascimento=int(input('Data de nascimento:'))
    mes_de_nascimento=int(input('Mês de nascimento:'))
    ano_de_nascimento=int(input('Ano de nascimento:'))
    escolha=int(input('Manha ou tarde(0 para manhã e 1 para de tarde):'))
    if escolha == 0 and cont<40:
        if len(manha)<=10:
            manha['2001'].append([aluno,matricula,data_de_nascimento,mes_de_nascimento,ano_de_nascimento])
        elif len(manha)<=20:
            manha['2002'].append([aluno,matricula,data_de_nascimento,mes_de_nascimento,ano_de_nascimento])
        elif len(manha)<=30:
            manha['2003'].append([aluno,matricula,data_de_nascimento,mes_de_nascimento,ano_de_nascimento])
        else:
            manha['2004'].append([aluno,matricula,data_de_nascimento,mes_de_nascimento,ano_de_nascimento])
            

