Analisador de Logs de Sistema

Projeto em Python que lê um arquivo de log e identifica falhas de conexão e autenticações bem-sucedidas, mostrando em qual linha cada ocorrência aparece.

Criei este projeto para praticar Python e, ao mesmo tempo, treinar uma tarefa comum em Help Desk e Suporte Técnico: ler logs para entender o que aconteceu com um sistema.

O que o programa faz hoje
Lê um arquivo de log linha por linha
Identifica falhas de conexão com o servidor
Identifica autenticações bem-sucedidas
Mostra a quantidade e a linha de cada ocorrência
Avisa quando não encontra nada, em vez de terminar sem mensagem
Formato de log esperado

Cada linha segue o padrão data hora NÍVEL mensagem:

2026-03-01 15:32:01 ERROR Falha ao conectar ao servidor
2026-03-01 15:32:15 INFO Usuário autenticado com sucesso
Como executar

Requisitos: Python 3 instalado.

Baixe ou clone este repositório
Coloque o arquivo sistema.log na mesma pasta do script
Execute:
bash
python leitordeerror.py
Exemplo de saída
Analisando o arquivo de log...
1 falha(s) de conexão encontrada(s):
Linha 1: 2026-03-01 15:32:01 ERROR Falha ao conectar ao servidor
1 Usuário(s) autenticado(s) com sucesso.
Linha 2: 2026-03-01 15:32:15 INFO Usuário autenticado com sucesso

Com um log que não contém nenhuma das duas ocorrências:

Analisando o arquivo de log...
Nenhuma falha de conexão encontrada.
Nenhum usuário autenticado com sucesso encontrado.
Próximos passos
 Identificar o motivo de cada falha (por exemplo: timeout, credenciais incorretas)
 Reconhecer outros tipos de erro além de conexão e autenticação
 Contar as ocorrências por horário do dia
 Gerar um relatório com gráfico
O que aprendi
<!--## O que aprendi

- A importância da atenção aos detalhes, pois tive erros simples que passavam despercebidos.
- Estou começando a aprender como os arquivos interagem com o código. -->
Autor

Micael Alves Barbosa Estudante de Análise e Desenvolvimento de Sistemas, em busca da primeira oportunidade em Help Desk / Suporte Técnico.

LinkedIn
