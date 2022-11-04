import graphics as gf
import pygame
import time
import listas_gp as br
import resultados as rr
win = gf.GraphWin( "Urna Eletrônica", 790,380)

guardar_voto = []

#verificar clique
def verifica_tecla(clique):
  if clique.getX() > 550 and clique.getX() < 595 and clique.getY()  > 70 and clique.getY() <100:
    return '1'
  if clique.getX() > 620 and clique.getX() < 670 and clique.getY()  > 70 and clique.getY() <100:
    return '2'
  if clique.getX() > 700 and clique.getX() < 740 and clique.getY()  > 70 and clique.getY() <100:
    return'3'
  if clique.getX() > 550 and clique.getX() < 590 and clique.getY()  > 120 and clique.getY() <150:
    return'4'
  if clique.getX() > 620 and clique.getX() < 670 and clique.getY()  > 120 and clique.getY() <150:
    return'5'
  if clique.getX() > 700 and clique.getX() < 740 and clique.getY()  > 120 and clique.getY() <150:
    return'6'
  if clique.getX() > 550 and clique.getX() < 590 and clique.getY()  > 170 and clique.getY() <200:
    return'7'
  if clique.getX() > 620 and clique.getX() < 670 and clique.getY()  > 170 and clique.getY() <200:
    return'8'
  if clique.getX() > 700 and clique.getX() < 740 and clique.getY()  > 170 and clique.getY() <200:
    return'9'
  if clique.getX() > 620 and clique.getX() < 670 and clique.getY()  > 220 and clique.getY() <250:
    return'0'
  if clique.getX() > 530 and clique.getX() < 590 and clique.getY()  > 270 and clique.getY() <320:
    return'branco'
  if clique.getX() > 620 and clique.getX() < 670 and clique.getY()  > 280 and clique.getY() <310:
    return'corrige'
  if clique.getX() > 700 and clique.getX() < 760 and clique.getY()  > 280 and clique.getY() <320:
    return'confirma'
  if clique.getX() > 50 and clique.getX() < 100 and clique.getY() > 330 and clique.getY() <365:
    return'encerra'
  else:
    return ''

#função principal
def main(win, cargo, guardar_voto):
    win.setBackground("#F5F5DC")
    telaX(win)
    botoes(win)
    
    print(guardar_voto)   
    
    voto = "" #variável voto
    if cargo == 'Governador':
      telaI = br.Governadortela()

    if cargo == 'Presidente':
      telaI = br.Presidentetela()
    for item in telaI:
      item.draw(win)


    #Laço de repetição principal do código:
    digitos = []
    telavotos = gf.Text(gf.Point(100,100), f'')
    telavotos2 = gf.Text(gf.Point(100,100), f'')
    digitos.append(telavotos2)
    digitos.append(telavotos)


    for item in digitos:
      item.draw(win)
   
   #enquanto o programa roda
    while True:
      clique = win.getMouse()
      tecla = verifica_tecla(clique)
    
      #botão corrige
      num = ('1,2,3,4,5,6,7,8,9,0')
      if tecla in num and len(voto) < 2:
        voto += tecla
        
        if len(voto) == 1:
          digitos[0] = gf.Text(gf.Point(90,180), f'{voto[0]}')

        if len(voto) == 2:
          digitos[1] = gf.Text(gf.Point(140,180), f'{voto[1]}')

        for item in digitos:
          item.undraw()
          item.draw(win)
        
      if tecla == 'corrige' and len(voto) > 1: 
        for item in digitos:
          item.undraw()
        digitos[0] = gf.Text(gf.Point(0,0), f"")
        digitos[1] = gf.Text(gf.Point(0,0), f"")
        voto = ''

      #botão encerrar
      if tecla == 'encerra':

        #limpando tela        
        telaI[0].undraw()
        telaI[1].undraw()
        
        #salvando resultados
        rr.ResultadosGovernamentais()
        rr.ResultadosPresidenciais()
        
        br.Encerrar(win)
      
      #botão branco
      if tecla == 'branco' and len(voto) == 0:
        telaI[0].undraw()
        telaI[1].undraw()
        Branco = br.VotoBranco()
      
        for item in Branco:
          item.draw(win)
        validar = True
     
        while validar:
          clique = win.getMouse()
          tecla = verifica_tecla(clique)
          
          if tecla == 'corrige':
            for item in Branco:
              item.undraw()
            telaI[0].undraw()
            telaI[1].undraw() 
            validar = False
          
          #confirma branco
          if tecla == 'confirma':
        
            for item in Branco:
              item.undraw()
            
            #contabilizar branco com csv
            if cargo == 'Governador':
              guardar_voto.append('BRANCO')
              main(win, 'Presidente', guardar_voto)
                
          
            if cargo == 'Presidente':
              br.Contagemgov(guardar_voto[0])
              br.Contagempre('BRANCO')
              main(win, 'Governador', [])
              
      
      #voto nulo e confirma
      if len(voto) == 2:

        if cargo == "Presidente":
          validacao = br.preinfo(voto)
        if cargo == "Governador":
          validacao = br.govinfo(voto)

        if validacao == "Voto Nulo":
          nulo = br.exibenulo()

          for item in nulo:
            item.draw(win)

          valida = True
          while valida:
           clique = win.getMouse()
           tecla = verifica_tecla(clique)
           if tecla == 'corrige':

            for item in nulo:
              item.undraw()              

            for item in digitos:
              item.undraw()
            digitos[0] = gf.Text(gf.Point(0,0), f"")
            digitos[1] = gf.Text(gf.Point(0,0), f"")
            voto = ''
            
            valida = False
           if tecla == 'confirma':
            for item in nulo:
              item.undraw()
            
            if cargo == 'Governador':
              guardar_voto.append('NULO')
              main(win, 'Presidente', guardar_voto)  
            
           
            if cargo == 'Presidente':
              br.Contagemgov(guardar_voto[0])
              br.Contagempre('NULO')
              main(win, 'Governador', [])
              

        #caso o numero exista
        else:
          if cargo == 'Governador':
            INFORMACOES = br.InformacoesGovernador(validacao)
            for item in INFORMACOES:
              item.draw(win)
          
          if cargo == 'Presidente':
            INFORMACOES = br.InformacoesPresidente(validacao)
            for item in INFORMACOES:
              item.draw(win)

          ##########

          valida = True
          while valida:
            clique = win.getMouse()
            tecla = verifica_tecla(clique)
            if tecla == 'corrige':

              for item in nulo:
                item.undraw()              

              for item in digitos:
                item.undraw()
              digitos[0] = gf.Text(gf.Point(0,0), f"")
              digitos[1] = gf.Text(gf.Point(0,0), f"")
              voto = ''
            
              valida = False

            if tecla == 'confirma':
              for item in INFORMACOES:
                item.undraw()
              
              if cargo == 'Governador':
                guardar_voto.append(voto)
                main(win, 'Presidente', guardar_voto)  
              
            
              if cargo == 'Presidente':
                br.Contagemgov(guardar_voto[0])
                br.Contagempre(voto)
                main(win, 'Governador', [])


#função definir tela
def telaX(win):
  telaprincipal = gf.Rectangle(gf.Point(20,20), gf.Point(500,360))
  telaprincipal.setFill('white')
  telaprincipal.draw(win)
  digitos = gf.Rectangle(gf.Point(520,30), gf.Point(770,350))
  digitos.setFill('grey')
  digitos.draw(win)

#função desenhar o teclado
def botoes(win):

    numeroum = gf.Text(gf.Point(570,90), "1")
    numeroum.draw(win)

    numerodois = gf.Text(gf.Point(645,90),"2")
    numerodois.draw(win)
     
    numerotres = gf.Text(gf.Point(720,90),"3")
    numerotres.draw(win)

    numeroquatro= gf.Text(gf.Point(570,140),"4")
    numeroquatro.draw(win)

    numerocinco = gf.Text(gf.Point(645,140),"5")
    numerocinco.draw(win)
    
    numeroseis = gf.Text(gf.Point(720,140),"6")
    numeroseis.draw(win)

    numerosete = gf.Text(gf.Point(570,190),"7")
    numerosete.draw(win)

    numerooito = gf.Text(gf.Point(645,190),"8")
    numerooito.draw(win)

    numeronove = gf.Text(gf.Point(720,190),"9")
    numeronove.draw(win)

    numerozero = gf.Text(gf.Point(645,240), "0")
    numerozero.draw(win)

    branco = gf.Text(gf.Point(560,300),"BRANCO")
    branco.draw(win)

    corrige = gf.Text(gf.Point(645,300), "CORRIGE")
    corrige.draw(win)

    confirma = gf.Text(gf.Point(725,300), "CONFIRMA")
    confirma.draw(win)

    encerra = gf.Text(gf.Point(65, 350), "ENCERRA")
    encerra.draw(win)
    


#chamar urna
if __name__ == "__main__":
    main(win, 'Governador', guardar_voto)