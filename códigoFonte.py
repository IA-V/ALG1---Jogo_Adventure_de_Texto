#Jogo Adventure de texto!

chaveLos = ['Uma chave cuja alça tem o formato de um losango e coloração azulada. Está um pouco desgastada!']
chaveMac = ['Uma chave cuja alça tem o formato do que parece ser uma maçã e coloração avermelhada. Está muito desgastada!']
faca = ['Uma faca pouco enferrujada. Talvez ainda seja útil para algo!']
blocos = ['Um bloco de pedra com formato retangular.']
objDesconhecido = ['Pequeno objeto que emite uma luz misteriosa']
bilhete = ['O castelo está dividido em térreo e primeiro andar. No térreo, encontram-se uma sala à [E]squerda, uma sala à [D]ireita, uma escadaria ao norte e a entrada principal ao [S]ul. No [1]º andar, há uma sala ao [N]orte, uma à [E]squerda, uma à [D]ireita e a escadaria ao [S]ul.']

descs =['Térreo - Salão Principal\n- Este salão parece não ter nada de interessante. Talvez eu deva entrar nas salas ao meu redor!', 'Térreo - Sala à Direita\n- Nessa sala tem um número escrito em uma de suas paredes: "7". Há também uma mesa encostada na parede à esquerda, com alguns livros e uma chave cuja alça tem coloração azulada e está um pouco desgastada, lembrando um losango!', 'Térreo - Sala à Esquerda\n- Esta sala parece ser o aposento de alguém! Há duas estantes de livros e uma mesa redonda no meio, com um livro aberto. Vejo um pequeno mecanismo na parede à minha direita, ao lado de uma das estantes, e um bilhete acima dele! Talvez eu deva chegar mais perto para observá-lo melhor!', 'Primeiro Andar - Corredor\n- Hm... Como o Salão Principal, este corredor não parece muito interessante! Melhor verificar as salas aqui em cima... ou voltar ao térreo!', 'Primeiro Andar - Sala à Direita\n- Esta sala está meio escura, mas ainda é possível enxergar o que está aqui. Há uma mesa e uma cadeira encostadas na parede à minha frente e uma pequena prateleira na parede à minha direita. Nesta prateleira há um pequeno bloco de pedra com formato retangular.', 'Primeiro Andar - Sala à Esquerda\n- Aqui tem outro número escrito na parede: "15". Há também uma outra chave, em cima de uma mesa retangular no meio da sala, mas parece estar muito desgastada! Sua alça lembra uma maçã... ou será outra coisa? Além disso, há mais um bloco de pedra aqui, ao lado da chave!', 'Primeiro Andar - Sala ao Norte\n- Pelo que consigo ver, há algumas estantes de madeira aqui. A que está à direita tem uma faca e mais um bloco de pedra! A que está à esquerda contém um pequeno objeto desconhecido que emite uma luz misteriosa!']

blocoUm = ['bloco 1', 'x']
blocoDois = ['bloco 2', 'x']
blocoTres = ['bloco 3', 'x']
E = ['E', 'bilhete']
D = ['D', 'chave do losango']
poemaUmE = '''   Diamante
                        
                            O amor seria fogo ou ar
                            em movimento, chama ao vento;
                            e no entanto é tão duro amar
                            este amor que o seu elemento
                            deve ser terra: diamante,
                            já que dura e fura e tortura
                            e fica tanto mais brilhante
                            quanto mais se atrita, e fulgura,
                            ao que parece, para sempre:
                            e às vezes volta a ser carvão
                            a rutilar incandescente
                            onde é mais funda a escuridão;
                            e volta indecente esplendor
                            e loucura e tesão e dor.'''
umE = ['1E', 'chave da maça', 'bloco 1']
umD = ['1D', 'bloco 2']
poemaUmN = '''   Lenta, Descansa a Onda que a Maré Deixa
                        
                            Lenta, descansa a onda que a maré deixa. 
                            Pesada cede. Tudo é sossegado. 
                            Só o que é de homem se ouve. 
                            Cresce a vinda da lua. 

                            Nesta hora, Lídia ou Neera ou Cloe, 
                            Qualquer de vós me é estranha, que me inclino 
                            Para o segredo dito 
                            Pelo silêncio incerto. 

                            Tomo nas mãos, como caveira, ou chave 
                            De supérfluo sepulcro, o meu destino, 
                            E ignaro o aborreço 
                            Sem coração que o sinta.'''
umN = ['1N', 'faca', 'objeto desconhecido', 'bloco 3']

portaSecretaAberta = [False]
salaSecretaAberta = [False]
portaUmNAberta = [False]
portaUmEAberta = [False]
countTerreo = [1]
countD = [0]
countE = [0]
countPrimeiroAndar = [0]
countUmD = [0]
countUmE = [0]
countUmN = [0]

localAtual = ['terreo']
direcoesPossiveis = ['E', 'D', 'N', 'S']

inventario = []
locais = [E, D, umE, umD, umN]

def ehNumero(value):
    try:
         float(value)
    except ValueError:
         return False
    return True

def sair():
  while True:
    print('Tem certeza que quer sair? (sim ou nao)')
    escolha = input('\n')
    if escolha == 'sim':
      exit()
    elif escolha == 'nao':
      break
    else:
      print('Comando inválido!')

def interacaoPortaUmN(temChave):
  while True:
    if temChave:
      print('- Devo usar a(s) chave(s) que tenho? (sim ou nao)')
      escolhaChave = input('\n')
      if escolhaChave == 'sim':
        print('Chave(s):')
        for i in range(0, len(inventario)):
          if inventario[i] == 'chave do losango' or inventario[i] == 'chave da maça':
            print(inventario[i], end='\t')
        chave = input('\n')
        if chave == 'chave da maça':
          portaUmNAberta[0] = True
          print('A porta ao norte foi destrancada!')
          return ['E', 'D', 'N', 'S']
        elif chave == 'chave do losango':
          print('Esta chave não pode ser usada aqui!')
        else:
          print('Comando inválido!\n')
      elif escolhaChave == 'nao':
        return ['E', 'D', 'N', 'S']
      else:
        print('Comando inválido!\n')
    else:
      return ['E', 'D', 'N', 'S']

def interacaoPortaUmE(temChave):
  while True:
    if temChave:
      print('- Devo usar a(s) chave(s) que tenho? (sim ou nao)')
      escolhaChave = input('\n')
      if escolhaChave == 'sim':
        print('Chave(s):')
        for i in range(0, len(inventario)):
          if inventario[i] == 'chave do losango' or inventario[i] == 'chave da maça':
            print(inventario[i], end='\t')
        chave = input('\n')
        if chave == 'chave do losango':
          portaUmEAberta[0] = True
          print('A porta a oeste foi destrancada!')
          return ['E', 'D', 'N', 'S']
        elif chave == 'chave da maça':
          print('Esta chave não pode ser usada aqui!')
        else:
          print('Comando inválido!\n')
      elif escolhaChave == 'nao':
        return ['E', 'D', 'N', 'S']
      else:
        print('Comando inválido!\n')
    else:
      return ['E', 'D', 'N', 'S']

def movimentoNorte():
    if 'N' in direcoesPossiveis:
        print('Você se movimentou para o norte!')
        if localAtual[0] == 'terreo':
            localAtual[0] = 'primeiro andar'
            return ['E', 'D', 'N', 'S']
        elif localAtual[0] == 'D':
            if salaSecretaAberta[0]:
                print('\nAo entrar na sala secreta, você tem a visão de um tipo de código desconhecido:\n\thttps://www.youtube.com/watch?v=oHg5SJYRHA0\n- Vou escrevê-lo num papel quando eu retornar à minha casa. Tentarei decifrá-lo. Caso não consiga, o deixarei anotado para alguém, no futuro, tentar decifrá-lo também!')
                return ['X', 'X', 'N', 'S']
            else:
                print('Não é possível se mover para o norte!')
                return ['X', 'X', 'X', 'S']
        elif localAtual[0] == 'primeiro andar':
          if portaUmNAberta[0]:
            localAtual[0] = '1N'
            return ['X', 'X', 'X', 'S']
          else:
            temChave = False
            if 'chave do losango' not in inventario and 'chave da maça' not in inventario:
              print('- A porta está trancada e não tenho chave alguma em meu inventário, mas há um poema pendurado na maçaneta. Devo ler o poema agora? (sim ou nao)')
            elif 'chave do losango' in inventario and 'chave da maça' in inventario or ('chave do losango' in inventario or 'chave da maça' in inventario):
              temChave = True
              print('- A porta está trancada, mas há um poema pendurado na maçaneta. Devo ler o poema agora? (sim ou nao)')
            while True:
                escolha = input()
                if escolha == 'sim':
                  print(poemaUmN)
                  return interacaoPortaUmN(temChave)
                elif escolha == 'nao':
                  return interacaoPortaUmN(temChave)
                else:
                   print('Comando inválido!')
              
    else:
      print('Não é possível se mover para o norte!')
      return direcoesPossiveis

def movimentoSul():
    if 'S' in direcoesPossiveis:
      print('Você se movimentou para o sul!')
      if localAtual[0] == 'terreo':
          if portaSecretaAberta[0]:
            sair()
          else:
            print('- Não vou sair desse castelo antes de encontrar aquele tesouro!')
            return ['E', 'D', 'N', 'S']
              
      elif localAtual[0] == 'D' or localAtual[0] == 'E' or localAtual[0] == 'primeiro andar':
          localAtual[0] = 'terreo'
          return ['E', 'D', 'N', 'S']
              
      elif localAtual[0] == '1E' or localAtual[0] == '1D' or localAtual[0] == '1N':
          localAtual[0] = 'primeiro andar'
          return ['E', 'D', 'N', 'S']
              
      elif localAtual[0] == 'sala secreta':
          localAtual[0] = 'D'
          return ['X', 'X', 'N', 'S']
    else:
      print('Não é possível se mover para o sul!')
      return direcoesPossiveis

def movimentoEsquerda():
    if 'E' in direcoesPossiveis:
      print('Você se movimentou para o oeste!')
      if localAtual[0] == 'terreo':
          localAtual[0] = 'E'
          return ['X', 'D', 'X', 'S']
              
      elif localAtual[0] == 'primeiro andar':
        if portaUmEAberta[0]:
          localAtual[0] = '1E'
          return ['X', 'X', 'X', 'S']
        else:
          temChave = False
          if 'chave do losango' not in inventario and 'chave da maça' not in inventario:
            print('- A porta está trancada e não tenho chave alguma em meu inventário, mas há um poema pendurado na maçaneta. Devo ler o poema agora? (sim ou nao)')
          elif 'chave do losango' in inventario and 'chave da maça' in inventario or ('chave do losango' in inventario or 'chave da maça' in inventario):
            temChave = True
            print('- A porta está trancada, mas há um poema pendurado na maçaneta. Devo ler o poema agora? (sim ou nao)')
          while True:
            escolha = input()
            if escolha == 'sim':
              print(poemaUmE)
              return interacaoPortaUmE(temChave)
            elif escolha == 'nao':
              return interacaoPortaUmE(temChave)
            else:
              print('Comando inválido!\n')    
    else:
      print('Não é possível se mover para oeste!')
      return direcoesPossiveis

def movimentoDireita():
        if 'D' in direcoesPossiveis:
          print('Você se movimentou para o leste!')
          if localAtual[0] == 'primeiro andar':
              localAtual[0] = '1D'
              return ['X', 'X', 'X', 'S']
              
          elif localAtual[0] == 'terreo':
              localAtual[0] = 'D'
              if salaSecretaAberta[0]:
                  return ['X', 'X', 'N', 'S']
              elif 'objeto desconhecido' in inventario:
                while True:
                  print('- Parece que foi desta sala que veio aquele barulho estranho!  Parece que está vindo de trás dessa parede em minha frente! Devo usar o  objeto desconhecido nela? (sim ou nao)')
                  escolha = input()
                  if escolha == 'sim':
                    salaSecretaAberta[0] = True
                    print('Sala secreta descoberta!')
                    return ['X', 'X', 'N', 'S']
                  elif escolha == 'nao':
                    return ['X', 'X', 'X', 'S']
                  else:
                    print('Comando inválido!')
              else:
                return ['X', 'X', 'X', 'S']
          elif localAtual[0] == 'E':
              if portaSecretaAberta[0]:
                  print('Parabéns!!! Você encontrou o tesouro escondido do castelo abandonado! Obrigado por jogar!')
                  while True:
                    escolha = input('Deseja continuar andando pelo castelo?\n\n')
                    if escolha == 'sim':
                      return direcoesPossiveis
                    elif escolha == 'nao':
                      exit()
                    else:
                      print('Comando inválido!')
              else:
                  print('\n- Este pequeno mecanismo na parede parece precisar que três blocos sejam encaixados nele!', end=' ')
                  print('\n\t[D] [1E] [1N]\n\t[B1][B2] [B3]')
                  if 'bloco 1' not in inventario and 'bloco 2' not in inventario and 'bloco 3' not in inventario:
                    print('- Não tenho nada que possa ser encaixado aqui!')
                    return ['X', 'D', 'X', 'S']
                  else:
                    while True:
                      print('\n- Devo usar o(s) bloco(s) que tenho aqui? (sim ou nao)')
                      escolha = input()
                      if escolha == 'sim':
                        blocosNumerados = 0
                        if 'bloco 1' in inventario:
                          if blocoUm[1] != 'x':
                            print('\nColocar bloco 1 no primeiro encaixe? (sim ou nao)')
                            escolhaUmB = input()
                            if escolhaUmB == 'sim':
                              print('Bloco 1 posicionado!')
                              blocosNumerados += 1
                            else:
                              print('Bloco não posicionado!')
                          else:
                            print('\nO bloco 1 não está numerado!\nBloco não posicionado!')
                        if 'bloco 2' in inventario:
                          if blocoDois[1] != 'x':
                            print('\nColocar bloco 2 no segundo encaixe? (sim ou nao)')
                            escolhaDoisB = input()
                            if escolhaDoisB == 'sim':
                              print('Bloco 2 posicionado!')
                              blocosNumerados += 1
                            else:
                              print('Bloco não posicionado!')
                          else:
                            print('\nO bloco 2 não está numerado!\nBloco não posicionado!')
                        if 'bloco 3' in inventario:
                          if blocoTres[1] != 'x':
                            print('\nColocar bloco 3 no primeiro encaixe? (sim ou nao)')
                            escolhaTresB = input()
                            if escolhaTresB == 'sim':
                              print('Bloco 3 posicionado!')
                              blocosNumerados += 1
                            else:
                              print('Bloco não posicionado!')
                          else:
                            print('\nO bloco 3 não está numerado!\nBloco não posicionado!')
                        if blocosNumerados == 3:
                          if blocoUm[1] == 7 and blocoDois[1] == 15 and blocoTres[1] == 5:
                            portaSecretaAberta[0] = True
                            print('\nA porta secreta da sala à esquerda foi destrancada!\n')
                            return ['X', 'D', 'X', 'S']
                          else:
                            print('\n- Nada aconteceu! A numeração dos blocos deve estar incorreta!\n')
                        else:
                          print('\n- O mecanismo não faz nada sem os blocos necessários! Creio que sem os três blocos numerados corretamente, não conseguirei descobrir o que este mecanismo faz!\n')
                      elif escolha == 'nao':
                        return ['X', 'D', 'X', 'S']
                      else:
                        print('Comando inválido!')
                  return ['X', 'D', 'X', 'S']
        else:
          print('Não é possível se mover para leste!')
          return direcoesPossiveis

def pegar():
  if localAtual[0] == 'terreo' or localAtual[0] == 'primeiro andar':
    print('Não há itens para serem coletados aqui!')
  else:
    for i in locais:
      if localAtual[0] == i[0]:
          while True:
              print('\nItem(ns):')
              for j in range(1, len(i)):
                print(i[j], end='\t')
              print()
              item = input('\n(Digite o nome do item a ser pego ou digite "cancelar" para cancelar esta ação!)\n')
              if item == 'cancelar':
                  break
              elif item in i:
                  if item == 'objeto desconhecido':
                    print('\nDe repente soa um barulho alto e estranho que parece vir de alguma das salas do térreo!')
                  if len(inventario) < 6:
                    if item in D:
                      D.remove(item)
                    elif item in E:
                      E.remove(item)
                    elif item in umD:
                      umD.remove(item)
                    elif item in umE:
                      umE.remove(item)
                    elif item in umN:
                      umN.remove(item)
                    inventario.append(item)
                    print()
                    print(item + ' foi adicionado(a) ao inventário!')
                  else:
                      print("O inventário está cheio!")
              else:
                  print('Este item não se encontra na sala atual!')
    
def inventarioVazio():
  if len(inventario) == 0:
    return True
  return False

def mostraInventario():
  if inventarioVazio():
    print('O inventário está vazio!')
  else:
    print(inventario)

def olhar():
  while True:
    if inventarioVazio():
      print('O inventário está vazio!')
      break
    else:
      print('Qual item você deseja olhar? (digite "cancelar" para cancelar esta ação!)')
      print(inventario)
      item = input('\n')
      if item == 'bilhete':
        print(bilhete)
      elif item == 'chave do losango':
        print(chaveLos)
      elif item == 'chave da maça':
        print(chaveMac)
      elif item == 'bloco 1' or item == 'bloco 2' or item == 'bloco 3':
        print(blocos)
        if 'faca' in inventario:
          print('\n- Talvez eu possa esculpir algum número neste bloco com a faca que encontrei!')
          if item == 'bloco 1' and blocoUm[1] != 'x':
            print('\n{} possui um número esculpido: {}\n'.format(item, blocoUm[1]))
          elif item == 'bloco 2' and blocoDois[1] != 'x':
            print('\n{} possui um número esculpido: {}\n'.format(item, blocoDois[1]))
          elif item == 'bloco 3' and blocoTres[1] != 'x':
            print('\n{} possui um número esculpido: {}\n'.format(item, blocoTres[1]))
          print('Deseja esculpir no bloco? (sim ou nao)')
          escolha = input('\n')
          if escolha == 'sim':
            while True:
              print('Digite o número:')
              num = input('\n')
              if ehNumero(num):
                if item == 'bloco 1':
                  blocoUm[1] = num
                  print('Número esculpido com sucesso!\n')
                elif item == 'bloco 2':
                  blocoDois[1] = num
                  print('Número esculpido com sucesso!\n')
                elif item == 'bloco 3':
                  blocoTres[1] = num
                  print('Número esculpido com sucesso!\n')
              else:
                print('Valor inválido!')
          elif escolha == 'nao':
            print()
          else:
            print('Comando inválido!')
      elif item == 'faca':
        print(faca)
      elif item == 'objeto desconhecido':
        print(objDesconhecido)
      elif item == 'cancelar':
        break
      else:
        print('Este item não está em seu inventário!')

def descartar():
  while True:
    if inventarioVazio():
      print('O seu inventário está vazio!')
      break
    print('Item a ser descartado? (digite "cancelar" para cancelar esta ação!)')
    print(inventario)
    item = input('\n')
    if item == 'cancelar':
      break
    elif item in inventario:
      inventario.remove(item)
      print('Item descartado com sucesso!')
    else:
      print('Este item não está em seu inventário!')

def localizacao():
  if localAtual[0] == 'terreo':
    print(descs[0])
  elif localAtual[0] == 'D':
    print(descs[1])
  elif localAtual[0] == 'E':
    print(descs[2])
  elif localAtual[0] == 'primeiro andar':
    print(descs[3])
  elif localAtual[0] == '1D':
    print(descs[4])
  elif localAtual[0] == '1E':
    print(descs[5])
  elif localAtual[0] == '1N':
    print(descs[6])

  print('\nMovimentos possíveis:')
  for i in direcoesPossiveis:
    if i == 'E':
      print('Oeste', end=' ')
    elif i == 'D':
      print('Leste', end=' ')
    elif i == 'N':
      print('Norte', end=' ')
    elif i == 'S':
      print('Sul', end=' ')
  print()
    
def ajuda():
  print('\nComandos:\n-pegar: lista os itens coletáveis de determinada sala e permite adicioná-los ao inventário (basta digitar o nome de algum dos itens disponíveis;)\n-olhar: dependendo dos itens presentes no inventário, pode ou não apenas descrever o item selecionado;\n-norte: movimenta o personagem para frente;\n-sul: movimenta o personagem para trás;\n-leste: movimenta o personagem para a direita;\n-oeste: movimenta o personagem para a esquerda;\n-inventario: exibe os itens presentes no inventário, se houver algum;\n-descartar: remove algum item do inventário, se ele não estiver vazio (ATENÇÃO: quando descartado, um item não pode ser recuperado!);\n-localizacao: exibe a descrição da sua atual posição e os movimentos que podem ser feitos;\n-sair: para a execução do jogo;\n-ajuda: exibe os comandos disponíveis e dá uma pequena descrição.')

def comando(comandoString):
    if comandoString == "pegar":
        pegar()
    elif comandoString == "olhar":
        olhar()
    elif comandoString == 'norte':
        return movimentoNorte()
    elif comandoString == 'sul':
        return movimentoSul()
    elif comandoString == 'leste':
        return movimentoDireita()
    elif comandoString == 'oeste':
        return movimentoEsquerda()
    elif comandoString == 'inventario':
      mostraInventario()
    elif comandoString == 'descartar':
      descartar()
    elif comandoString == 'localizacao':
      localizacao()
    elif comandoString == 'ajuda':
      ajuda()
    elif comandoString == 'sair':
      sair()
    else:
      print('Comando inválido!')

print('Bem vindo ao jogo Caça ao Tesouro Medieval! Você é um caçador de recompensas da era medieval, mas ficou sabendo de um tesouro antigo que está escondido num Castelo Abandonado numa cidade distante e decidiu buscá-lo por conta própria. Você viajou até esta cidade, encontrou o castelo e agora está dentro dele, tentando encontrar aquele tesouro!\n(Digite "ajuda" para conhecer os comandos do jogo!)\n')
input('Pressione ENTER para iniciar!\n')
print(descs[0])

while True:
    com = input('\n')
    if com == 'norte' or com == 'sul' or com == 'leste' or com == 'oeste':
        direcoesPossiveis = comando(com)
        print()
        if localAtual[0] == 'terreo' and countTerreo[0] == 0:
          print(descs[0])
          countPrimeiroAndar[0] += 1
        elif localAtual[0] == 'D' and countD[0] == 0:
          print(descs[1])
          countD[0] += 1
        elif localAtual[0] == 'E' and countE[0] == 0:
          print(descs[2])
          countE[0] += 1
        elif localAtual[0] == 'primeiro andar' and countPrimeiroAndar[0] == 0:
          print(descs[3])
          countPrimeiroAndar[0] += 1
        elif localAtual[0] == '1D' and countUmD[0] == 0:
          print(descs[4])
          countUmD[0] += 1
        elif localAtual[0] == '1E' and countUmE[0] == 0:
          print(descs[5])
          countUmE[0] += 1
        elif localAtual[0] == '1N' and countUmN[0] == 0:
          print(descs[6])
          countUmN[0] += 1
    else:
        comando(com)
