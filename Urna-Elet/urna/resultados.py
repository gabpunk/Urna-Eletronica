def CandidatosPresi():
    arquivo = open("candidatos_pres.csv", "r", encoding="utf-8")
    conteudo = arquivo.read()
    arquivo.close()

    govinfo = []
    lista = conteudo.split('\n')
    for item in lista:
        final = item.split(';')
        govinfo.append(final)

    candidatos = []

    for item in lista:
        um_teste = item.split(";")
        candidatos.append(um_teste)

    candidatos = candidatos[1:]

    candidatos_final = []

    for item in candidatos:
        teste = item[:-3]
        candidatos_final.append(teste)

    return(candidatos_final[:-1])

def ResultadosPresidenciais():
    arquivo = open("contagem/presidentes.csv", "r", encoding="utf-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []

    for item in conteudo:
        linha = item[0:-1] 
        uma_lista = linha.split(";") 
        lista.append(uma_lista) 
    total_votos = 0

    for item in lista:
        numero = int(item[1])
        total_votos += numero

    lista_porcentagem = []

    for item in lista:
        if int(item[1]) > 0:
            porcentagem = int(item[1]) / total_votos * 100
            lista_porcentagem.append(f"{item[0]};{porcentagem:.2f}%")
        else:
            lista_porcentagem.append(f"{item[0]};0.00%")

    porcentagem = []

    for item in lista_porcentagem:
        uma_lista = item.split(";")
        porcentagem.append(uma_lista)


    outra_lista = []

    candidatos = CandidatosPresi()

    n = 2
    for item in candidatos:

        uma_lista = []

        string = porcentagem[n][0]
        uma_lista.append(string)
        
        uma_lista.append(item[1])
        uma_lista.append(item[2])

        uma_lista.append(lista[n][1])

        string = porcentagem[n][1]
        uma_lista.append(string)

        outra_lista.append(uma_lista)

        n += 1
    

    porcentagem_nulo = lista_porcentagem[0].split(";")
    porcentagem_branco = lista_porcentagem[1].split(";")

    string_resultado = ""

    n = 0
    for item in outra_lista:
        for i in item:
            string_resultado += i
            string_resultado += ";"

        string_resultado += "\n"

    string_resultado += f'Votos Nulos: {lista[0][1]} ({porcentagem_nulo[1]})\n'
    string_resultado += f'Votos Brancos: {lista[1][1]} ({porcentagem_branco[1]})\n'
    string_resultado += f'Total de Votos: {total_votos}\n'

    arquivo = open("resultado_presidenciais.csv", "w", encoding="utf-8")
    arquivo.write(string_resultado)
    arquivo.close()











def CandidatosGover():
    arquivo = open("candidatos_gov.csv", "r", encoding="utf-8")
    conteudo = arquivo.read()
    arquivo.close()

    govinfo = []
    lista = conteudo.split('\n')
    for item in lista:
        final = item.split(';')
        govinfo.append(final)

    candidatos = []

    for item in lista:
        um_teste = item.split(";")
        candidatos.append(um_teste)

    candidatos = candidatos[1:]

    candidatos_final = []

    for item in candidatos:
        teste = item[:-3]
        candidatos_final.append(teste)

    return(candidatos_final[:-1])



def ResultadosGovernamentais():
    arquivo = open("contagem/governadores.csv", "r", encoding="utf-8")
    conteudo = arquivo.readlines()
    arquivo.close()

    lista = []

    for item in conteudo:
        linha = item[0:-1] 
        uma_lista = linha.split(";") 
        lista.append(uma_lista) 

    total_votos = 0

    for item in lista:
        numero = int(item[1])
        total_votos += numero

    lista_porcentagem = []

    for item in lista:
        if int(item[1]) > 0:
            porcentagem = int(item[1]) / total_votos * 100
            lista_porcentagem.append(f"{item[0]};{porcentagem:.2f}%")
        else:
            lista_porcentagem.append(f"{item[0]};0.00%")

    porcentagem = []

    for item in lista_porcentagem:
        uma_lista = item.split(";")
        porcentagem.append(uma_lista)

    outra_lista = []

    candidatos = CandidatosGover()

    n = 2
    for item in candidatos:

        uma_lista = []
   
        uma_lista.append(item[0])
        uma_lista.append(item[1])
        uma_lista.append(item[2])
        uma_lista.append(lista[n][1])

        if porcentagem[n][0] != "BRANCO" and porcentagem[n][0] != "NULO":
            string = porcentagem[n][1]
            uma_lista.append(string)

        outra_lista.append(uma_lista)

        n += 1
    

    porcentagem_nulo = lista_porcentagem[0].split(";")
    porcentagem_branco = lista_porcentagem[1].split(";")

    string_resultado = ""

    n = 0
    for item in outra_lista:
        for i in item:
            string_resultado += i
            string_resultado += ";"

        string_resultado += "\n"

    string_resultado += f'Votos Nulos: {lista[0][1]} ({porcentagem_nulo[1]})\n'
    string_resultado += f'Votos Brancos: {lista[1][1]} ({porcentagem_branco[1]})\n'
    string_resultado += f'Total de Votos: {total_votos}\n'

    arquivo = open("resultado_governamentais.csv", "w", encoding="utf-8")
    arquivo.write(string_resultado)
    arquivo.close()

