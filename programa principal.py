from modulos import leiaint,tabela,separador_de_salas,leia_opção,leia_data,leia_mes,leia_ano,linha

cont=0
infomações={}
tudo=[]
while True:
    cont+=1
    linha()
    infomações['aluno']=str(input('Nome do aluno:')).strip()
    infomações['Matricula']=leiaint('Número da matricula:')
    infomações['data_de_nascimento']=leia_data('Data de nascimento:')
    infomações['mes_de_nascimento']=leia_mes('Mês de nascimento:')
    infomações['ano_de_nascimento']=leia_ano('ano de nascimento')
    infomações['Turno']=leia_opção('Manha ou tarde(0 para manhã e 1 para de tarde):')
    escolha2=leia_opção('1 para sair do programa 0 para continuar:')
    linha()
    tudo.append(infomações.copy())
    
    if escolha2 == 1:
        break

alunosseparado=separador_de_salas(tudo)
tabela(alunosseparado)