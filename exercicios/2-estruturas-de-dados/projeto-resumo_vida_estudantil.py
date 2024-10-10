# Nesse exercício coletaremos dados de uma estudante, armazenaremos em um dicionário e imprimiremos na tela esse dados em um formato amigável.

# 1. Solicite a estudante os seguintes dados: nome, ano que conheceu o LinkedIn, ano atual e os cursos realizados no LinkedIn Learning separados por virgula em ordem cronológica
# 2. Armazene esses dados em um dicionário
# 3. Imprima na tela uma string com as informações de nome, ano_conheceu_linkedin, total de anos transcurridos, total de cursos realizados e (apenas) o primeiro e último curso.
#
# Meu segundo script Python:
#!/usr/bin/env python3
print("Olá! Siga as instruções a seguir para realizar o cadastro da sua matrícula de Pós-Graduação técnica.")
matricula01={}
matricula01['nome_aluno']=input("Informe seu nome completo: ")
matricula01['idade_aluno']=int(input("Informe sua idade atual (somente números): "))
matricula01['ano_matricula']=int(input("Confirme o ano vigente em que você está realizando essa matrícula: "))
matricula01['curso']=input("Informe o nome do curso que você irá cursar: ")
disciplinas=input("Informe a(s) disciplina(s) que você irá cursar no seu primeiro semestre (separe utilizando vírgula e espaço): ")
matricula01['disciplinas']=disciplinas.split(', ')
total_disciplinas=len(matricula01['disciplinas'])
formacoes_tecnicas=input("Informe, em ordem cronológica, as formações técnicas que você realizou (da mais antiga para a mais recente) e separe utilizando vírgula e espaço: ")
matricula01['formacoes_tecnicas']=formacoes_tecnicas.split(', ')
matricula01['ano_ultima_graduacao']=int(input("Informe o ano em que você concluiu sua última graduação: "))
total_anos_entre_estudos=matricula01['ano_matricula']-matricula01['ano_ultima_graduacao']
print(f'''Segue sua matrícula preenchida:
Nome: {matricula01['nome_aluno']}
Idade: {matricula01['idade_aluno']} anos
Ano vigente da matrícula: {matricula01['ano_matricula']}
Curso: {matricula01['curso']}
Disciplinas: {matricula01['disciplinas']}
Quantidade de disciplinas: {total_disciplinas}
Tempo desde sua última graduação: {total_anos_entre_estudos} ano(s)
Formação técnica mais recente: {matricula01['formacoes_tecnicas'][-1]}
Formação técnica mais antiga: {matricula01['formacoes_tecnicas'][0]}''')