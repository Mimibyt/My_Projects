import datetime

with open("sistema.log", "r", encoding="utf-8") as arquivo:
    linhas = arquivo.readlines()


encontradas_error = []
encontradas_success = []
dic_hora_error = {}
dic_hora_success = {}
print("Analisando o arquivo de log...")


def analisar():
    for numero, linha in enumerate(linhas, start=1):
        if "falha ao conectar ao servidor" in linha.lower():
            encontradas_error.append((numero, linha.strip()))
            partes = linha.split(" ")
            horario_completo = partes[1]
            horario = horario_completo.split(":")[0]
            if horario in dic_hora_error:
                dic_hora_error[horario] = dic_hora_error[horario] + 1
            else:
                dic_hora_error[horario] = 1
        if "usuário autenticado com sucesso" in linha.lower():
            encontradas_success.append((numero, linha.strip()))
            encontradas_error.append((numero, linha.strip()))
            partes = linha.split(" ")
            horario_completo = partes[1]
            horario = horario_completo.split(":")[0]
            if horario in dic_hora_success:
                dic_hora_success[horario] = dic_hora_success[horario] + 1
            else:
                dic_hora_success[horario] = 1


analisar()


if encontradas_error:
    print(f"{len(encontradas_error)} falha(s) de conexão encontrada(s):")
    for numero, linha in encontradas_error:
        print(f"Linha {numero}: {linha}")
else:
        print("Nenhuma falha de conexão encontrada.")

if encontradas_success:        
    print(f"{len(encontradas_success)} Usuário(s) autenticado(s) com sucesso.")
    for numero, linha in encontradas_success:
        print(f"Linha {numero}: {linha}")
else:
        print("Nenhum usuário autenticado com sucesso encontrado.")
