# Criaremos um script que imprimirá na tela o total de horas que uma pessoa estudou durante um determinado período:
# 1. Crie uma variável chamada "nome" e, usando o método input(), atribua a ela um nome;
# 2. Crie uma variável chamada "total_dias" e, usando o método input(), solicite o total de dias dedicados ao estudo por semana;
# 3. Crie uma variável chamada "total_horas" e, usanod o método input(), solicite a média de horas estudada por dia;
# 4. Crie uma variável chamada "curso" e, usando o método input(), solicite o título do curso desejado;
# 5. Imprima na tela uma frase informando o nome da estudante, o total_dias dedicados aos estudos, o total horas semanais e o curso.
#
# Meu primeiro script Python:
#!/usr/bin/env python3
print("Olá! Siga as instruções a seguir para receber um resumo da sua semana de estudos.")
nome=input("Digite seu nome: ")
total_dias=int(input("Quantos dias você estudou nessa semana? "))
total_horas=int(input("Em média, quantas horas por dia você estudou? "))
curso=input("Qual o nome do curso que você está estudando? ")
print(f'''Resumo da sua semana de estudos:
{nome} estudou {total_dias} dia(s), {total_horas} hora(s) por dia, totalizando {total_dias*total_horas} hora(s) de estudo na semana, do curso '{curso}'.''')