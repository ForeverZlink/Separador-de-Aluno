from modulos import leiaint,tabela,validaçao

manha={'2001':[],'2002':[],'2003':[],'2004':[]}
tarde={'2005':[],'2006':[],'2007':[],'2008':[]}
cont=0
infomações={}
while True:
    cont+=1
    infomações['aluno']=str(input('Nome do aluno:')).strip()
    infomações['matricula']=leiaint('Número da matricula:')
    infomações['data_de_nascimento']=leiaint('Data de nascimento:')
    infomações['mes_de_nascimento']=leiaint('Mês de nascimento:')
    infomações['ano_de_nascimento']=leiaint('Ano de nascimento:')
    escolha=leiaint('Manha ou tarde(0 para manhã e 1 para de tarde):')
    escolha2=leiaint('1 para sair do programa 0 para continuar:')
    
    validaçao(infomações,escolha)
    if escolha == 0 and len(manha)<=40:
        turno='manha'
        if len(manha)<=10:
            manha['2001'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        elif len(manha)<=20:
            manha['2002'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        elif len(manha)<=30:
            manha['2003'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        else:
            manha['2004'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
    if escolha2==0 and len(tarde)<=40:
        turno='tarde'
        if len(tarde)<=10:
            tarde['2005'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        elif len(tarde)<=20:
            tarde['2006'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        elif len(tarde)<=30:
            tarde['2007'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
        else:
            tarde['2008'].append({'aluno':aluno,'matricula':matricula,'data_de_nascimento':data_de_nascimento,'mesdenascimento':mes_de_nascimento,'ano de nascimento':ano_de_nascimento,'turno':turno})
    if escolha2 == 1:
        break

tabela(manha)
