from tkinter import E
import graphics as gf
from time import sleep
import urna as ur
import resultados as re

def VotoBranco():
    LISTA_BRANCO = []

    voto_branco = gf.Text(gf.Point(260, 200), f'VOTO EM BRANCO')
    voto_branco.setSize(30)
    voto_branco.setStyle("bold")
    LISTA_BRANCO.append(voto_branco)

    linha_horizontal = gf.Line(gf.Point(20, 305), gf.Point(520, 305))
    LISTA_BRANCO.append(linha_horizontal)

    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_BRANCO.append(aperte_tecla)

    return(LISTA_BRANCO)

def Governadortela():
    governador_tela = []

    quadrado_esquerda = gf.Rectangle(gf.Point(70, 160), gf.Point(110, 200))
    quadrado_direita = gf.Rectangle(gf.Point(120, 160), gf.Point(160, 200))
    governador_tela.append(quadrado_direita)
    governador_tela.append(quadrado_esquerda)


    voto_para = gf.Text(gf.Point(120, 100),"SEU VOTO PARA:\nGovernador")
    voto_para.setSize(14)
    voto_para.setOutline("BLACK")
    voto_para.setFace("helvetica")
    governador_tela.append(voto_para)
    
    return(governador_tela)


def Presidentetela():
    presidente_tela = []

    quadrado_esquerda = gf.Rectangle(gf.Point(70, 160), gf.Point(110, 200))
    quadrado_direita = gf.Rectangle(gf.Point(120, 160), gf.Point(160, 200))
    presidente_tela.append(quadrado_direita)
    presidente_tela.append(quadrado_esquerda)

    

    voto_para = gf.Text(gf.Point(120, 100),"SEU VOTO PARA:\nPresidente")
    voto_para.setSize(14)
    voto_para.setOutline("BLACK")
    voto_para.setFace("helvetica")
    presidente_tela.append(voto_para)
   
    return(presidente_tela)



def preinfo(voto):
    preinfo = []
    arq = open('candidatos_pres.csv', 'r', encoding = 'UTF-8') 
    conteudo = arq.read()
    lista = conteudo.split('\n')
    for item in lista:
        final = item.split(';')
        preinfo.append(final)
    arq.close()
    
    for lista in preinfo:
        if voto == lista[0]:
            return(lista)

    return('Voto Nulo')

def exibenulo():
    exibenulo = []
    voto_nulo = gf.Text(gf.Point(260, 200), f'VOTO EM NULO')
    voto_nulo.setSize(30)
    voto_nulo.setStyle("bold")
    exibenulo.append(voto_nulo)
    
    linha_horizontal = gf.Line(gf.Point(20, 305), gf.Point(520, 305))
    exibenulo.append(linha_horizontal)
    
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    exibenulo.append(aperte_tecla)

    return(exibenulo)

def govinfo(voto):
    govinfo = []
    arq = open('candidatos_gov.csv', 'r', encoding = 'UTF-8')
    conteudo = arq.read()
    lista = conteudo.split('\n')
    for item in lista:
        final = item.split(';')
        govinfo.append(final)
    arq.close()
    
    for item in govinfo:
        if voto in item:
            return(item)
    return('Voto Nulo')


def Contagemgov(voto):
    arquivo = open("contagem/governadores.csv", "r",  encoding="utf-8")
    conteudo_contagem = arquivo.readlines()
    arquivo.close()

    #Lista vazia que vai virar uma lista com sublistas:
    nova_lista = []

    for item in conteudo_contagem:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    #Adicionando um voto no respectivo candidato:
    for item in nova_lista:
        if voto == item[0]:
            numero = int(item[1])
            numero += 1
            item[1] = str(numero)

    #Criando uma string que será adicionada ao arquivo:
    string_arquivo = ""

    #Concatenando o que é necessário na string:
    for item in nova_lista:
        string_arquivo += item[0]
        string_arquivo += ";"
        string_arquivo += item[1]
        string_arquivo += "\n"

    #Modificando o arquivo:
    arquivo = open("contagem/governadores.csv", "w")
    arquivo.write(string_arquivo)
    arquivo.close()



def Contagempre(voto):
    arquivo = open("contagem/presidentes.csv", "r",  encoding="utf-8")
    conteudo_contagem = arquivo.readlines()
    arquivo.close()

    #Lista vazia que vai virar uma lista com sublistas:
    nova_lista = []

    for item in conteudo_contagem:
        linha = item[0:-1] #-> removendo o \n e pegando uma linha
        uma_lista = linha.split(";") #-> fazendo cada elemento virar um item de uma lista
        nova_lista.append(uma_lista) #-> adicionando essa lista em uma lista maior

    #Adicionando um voto no respectivo candidato:
    for item in nova_lista:
        if voto == item[0]:
            numero = int(item[1])
            numero += 1
            item[1] = str(numero)

    #Criando uma string que será adicionada ao arquivo:
    string_arquivo = ""

    #Concatenando o que é necessário na string:
    for item in nova_lista:
        string_arquivo += item[0]
        string_arquivo += ";"
        string_arquivo += item[1]
        string_arquivo += "\n"

    #Modificando o arquivo:
    arquivo = open("contagem/presidentes.csv", "w")
    arquivo.write(string_arquivo)
    arquivo.close()
    
def InformacoesGovernador(lista):
   
    nome_governador = lista[1]
    partido_governador = lista[2]
    vice_governador = lista[3]
    foto_governador = lista[4]
    foto_vice = lista[5]
    
    LISTA_INFORMACOES = []
    info_nome = gf.Text(gf.Point(50, 215), f'Nome:')
    info_nome.setStyle("bold")
    LISTA_INFORMACOES.append(info_nome)
    info_partido = gf.Text(gf.Point(55, 245), f'Partido:')
    info_partido.setStyle("bold")
    LISTA_INFORMACOES.append(info_partido)
    info_vice = gf.Text(gf.Point(92, 275), f'Vice-Governador:')
    info_vice.setStyle("bold")
    LISTA_INFORMACOES.append(info_vice)
    #
    num = len(nome_governador) * 3.5 #-> variável para saber qual a distância cada nome vai ter do "Nome:"
    nome_candidato = gf.Text(gf.Point(86+num, 215), f'{nome_governador}') #-> nome do candidato, recebido como parâmetro
    LISTA_INFORMACOES.append(nome_candidato)
    #
    num = len(partido_governador) * 3.9 #-> variável para saber qual a distância cada nome vai ter do "Partido:"
    partido_candidato = gf.Text(gf.Point(93+num, 245), f'{partido_governador}') #-> partido do candidato
    LISTA_INFORMACOES.append(partido_candidato)
    #
    num = len(vice_governador) * 3.6 #-> variável para saber qual a distância cada nome vai ter do "Vice-governador:"
    vice_governador = gf.Text(gf.Point(168+num, 275), f'{vice_governador}') #-> nome do vice
    LISTA_INFORMACOES.append(vice_governador)

    #Imagem do governador:
    foto_governador = gf.Image(gf.Point(430, 95), f"ImagemGovernadores/{foto_governador}")
    LISTA_INFORMACOES.append(foto_governador)
    governador = gf.Text(gf.Point(430, 170), "Governador") #-> mensagem que fica abaixo da foto
    governador.setSize(8)
    LISTA_INFORMACOES.append(governador)
    #Imagem do vice-governador:
    foto_vice = gf.Image(gf.Point(430, 230), f"ImagemGovernadores/{foto_vice}")
    LISTA_INFORMACOES.append(foto_vice)
    vice = gf.Text(gf.Point(430, 300), "Vice-Governador") #-> mensagem que fica abaixo da foto
    vice.setSize(7)
    LISTA_INFORMACOES.append(vice)
    #
    linha_horizontal = gf.Line(gf.Point(20, 308), gf.Point(423, 308))
    LISTA_INFORMACOES.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_INFORMACOES.append(aperte_tecla)

    return(LISTA_INFORMACOES)


def InformacoesPresidente(lista):
    
    nome_presidente = lista[1]
    partido_presidente = lista[2]
    vice_presidente = lista[3]
    foto_presidente = lista[4]
    foto_vice = lista[5]
    
    LISTA_INFORMACOES = []
    info_nome = gf.Text(gf.Point(50, 215), f'Nome:')
    info_nome.setStyle("bold")
    LISTA_INFORMACOES.append(info_nome)
    info_partido = gf.Text(gf.Point(55, 245), f'Partido:')
    info_partido.setStyle("bold")
    LISTA_INFORMACOES.append(info_partido)
    info_vice = gf.Text(gf.Point(92, 275), f'Vice-Presidente:')
    info_vice.setStyle("bold")
    LISTA_INFORMACOES.append(info_vice)
    #
    num = len(nome_presidente) * 3.5 #-> variável para saber qual a distância cada nome vai ter do "Nome:"
    nome_candidato = gf.Text(gf.Point(86+num, 215), f'{nome_presidente}') #-> nome do candidato, recebido como parâmetro
    LISTA_INFORMACOES.append(nome_candidato)
    #
    num = len(partido_presidente) * 3.9 #-> variável para saber qual a distância cada nome vai ter do "Partido:"
    partido_candidato = gf.Text(gf.Point(93+num, 245), f'{partido_presidente}') #-> partido do candidato
    LISTA_INFORMACOES.append(partido_candidato)
    #
    num = len(vice_presidente) * 3.6 #-> variável para saber qual a distância cada nome vai ter do "Vice-Presidente:"
    vice_presidente = gf.Text(gf.Point(168+num, 275), f'{vice_presidente}') #-> nome do vice
    LISTA_INFORMACOES.append(vice_presidente)
    #Imagem do presidente:
    foto_pre = gf.Image(gf.Point(430, 95), f"ImagemPresidentes/{foto_presidente}")
    LISTA_INFORMACOES.append(foto_pre)
    presidente = gf.Text(gf.Point(430, 170), "Presidente") #-> mensagem que fica abaixo da foto
    presidente.setSize(8)
    LISTA_INFORMACOES.append(presidente)
    #Imagem do vice-presidente:
    foto_vice = gf.Image(gf.Point(430, 230), f"ImagemPresidentes/{foto_vice}")
    LISTA_INFORMACOES.append(foto_vice)
    vice = gf.Text(gf.Point(430, 300), "Vice-Presidente") #-> mensagem que fica abaixo da foto
    vice.setSize(7)
    LISTA_INFORMACOES.append(vice)
    #
    linha_horizontal = gf.Line(gf.Point(20, 308), gf.Point(423, 308))
    LISTA_INFORMACOES.append(linha_horizontal)
    aperte_tecla = gf.Text(gf.Point(260, 325), f'Aperte a tecla CONFIRMA para CONFIRMAR o voto.\n Aperte a tecla CORRIGE para REINICIAR o voto.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    LISTA_INFORMACOES.append(aperte_tecla)

    return(LISTA_INFORMACOES)

def Encerrar(win):
    
    texto = gf.Text(gf.Point(120,130), "DIGITE A SENHA:")
    texto.setSize(16)
    texto.draw(win)

    aperte_tecla = gf.Text(gf.Point(260, 277), f'Aperte a tecla CONFIRMA para VALIDAR a senha.\n Aperte a tecla CORRIGE para REINICIAR a senha.\n\n\n\n\n\n\nAperte a tecla BRANCO para VOLTAR para a votação.')
    aperte_tecla.setSize(7)
    aperte_tecla.setFace("helvetica")
    aperte_tecla.setStyle("bold")
    aperte_tecla.draw(win)

    QUADRADOS = QuadradosEncerrar()
    for item in QUADRADOS:
        item.draw(win)

    ASTERISCOS = AsteriscosEncerrar()

    senha = "123456"
    tentativa_senha = ""

    ValidarSenha = True
    while ValidarSenha:
        clique = win.getMouse()

        TECLA = ur.verifica_tecla(clique)

        if len(TECLA) == 1:

            if len(tentativa_senha) < 6:
                tentativa_senha += TECLA
            if len(tentativa_senha) == 1:
                ASTERISCOS[0].draw(win)
            if len(tentativa_senha) == 2:
                ASTERISCOS[1].draw(win)
            if len(tentativa_senha) == 3:
                ASTERISCOS[2].draw(win)
            if len(tentativa_senha) == 4:
                ASTERISCOS[3].draw(win)
            if len(tentativa_senha) == 5:
                ASTERISCOS[4].draw(win)
            if len(tentativa_senha) == 6:
                ASTERISCOS[5].draw(win)

        if len(TECLA) > 1:
            if TECLA == "confirma":
                
                if tentativa_senha == senha:
                    for item in ASTERISCOS:
                        item.undraw()

                    for item in QUADRADOS:
                        item.undraw()

                    texto.undraw()

                    aperte_tecla.undraw()

                    re.ResultadosGovernamentais()
                    re.ResultadosPresidenciais()
                    win.close()
                else:
                    tentativa_senha = ""

                    for item in ASTERISCOS:
                        item.undraw()

            if TECLA == "corrige":

                tentativa_senha = ""

                for item in ASTERISCOS:
                    item.undraw()
                
            if TECLA == "branco":
                for item in ASTERISCOS:
                    item.undraw()
                for item in QUADRADOS:
                    item.undraw()
                
                texto.undraw()

                aperte_tecla.undraw()

                return(ur.main(win, "Governador", ["",""]))
    


def QuadradosEncerrar():
    QUADRADOS = []
    QUADRADOS.append(gf.Rectangle(gf.Point(115, 170), gf.Point(155, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(165, 170), gf.Point(205, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(215, 170), gf.Point(255, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(265, 170), gf.Point(305, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(315, 170), gf.Point(355, 210)))
    QUADRADOS.append(gf.Rectangle(gf.Point(365, 170), gf.Point(405, 210)))
    return(QUADRADOS)


def AsteriscosEncerrar():
    ASTERISCOS = []
    ASTERISCOS.append(gf.Text(gf.Point(135, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(185, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(235, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(285, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(335, 195), "*"))
    ASTERISCOS.append(gf.Text(gf.Point(385, 195), "*"))
    for item in ASTERISCOS:
        item.setSize(25)

    return(ASTERISCOS)