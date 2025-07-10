'''
************************************************************************************
Autor: Lucas Gabriel Cerqueira Santos Lima    Matrícula: 22211305
Componente Curricular: MI - Algoritmos
Concluido em: 12/12/2022
Declaro que este código foi elaborado por mim de forma individual e não contém
nenhum trecho de código de colega ou de outro autor, tais como provindos de livros
e apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de
código de outra autoria que não a minha está destacado com uma citação do autor e
a fonte do código, e estou ciente que estes trechos não serão considerados para fins
de avaliação.
************************************************************************************
'''

import os
import time

############## Funções para front end e validações ####################

#Função para decoração ( linhas )
def corda():
    print('<'+'>=<'*50+'>')

#Função que limpa o cmd no windows
#Para funcionar no linux troque "cls" por "clear"
def limpar_cmd(tempo = False):
    if tempo:
        time.sleep(2)
    os.system('cls') or None

#Função para pegar o tamanho da maior palavra em uma lista
#Serve para ajustar os prints
def tamanho_do_maior(*palavras):
    maior = 0
    for palavra in palavras:
        if len(palavra) > maior:
            maior = len(palavra)
    return maior

#Mostra um menu para o usuário
def menu(questao, *opcoes):
    
    maior_opcao = tamanho_do_maior(*opcoes)
    
    corda()
    print(questao)
    corda()

    n = 0
    for opcao in opcoes:
        n += 1
        print(f"{n}. {opcao}", end = (" "*(maior_opcao - len(opcao)))+'  ' if n%2!=0 and len(opcoes) > 4 else "\n")

    escolha = input("\n\n>>> " if n%2!=0 and  len(opcoes) > 4 else '\n>>> ') 

    if not escolha.isdigit() or int(escolha) < 1 or int(escolha) > n:
        print("Escolha inválida!")
        limpar_cmd(True)        
        return menu(questao, *opcoes)    #Volta ao menu
    
    limpar_cmd()
    return int(escolha) -1

#Função para validar um inteiro
def pegar_int():
    n = input('>>> ')
    while not n.isdigit():
        n = input("Somente números!\n>>> ")
    limpar_cmd()
    return int(n)

#Função para pegar a letra de um grupo
def pegar_letra(grupos):
    indice_letra = menu("ESCOLHA UM GRUPO", *grupos.keys())
    letra = list(grupos.keys())[indice_letra]
    return letra

###################### Funções para cadastrar os grupos e os jogos #######################

#Função para escolher oque cadastrar ( grupo ou jogo )
def cadastros(grupos, jogos):
    escolha = menu("CADASTRO", "Grupo", "Jogo", "Voltar")
    if escolha == 0:
        cadastrar_grupos(grupos, jogos)
    elif escolha == 1:
        erro = cadastrar_jogos(grupos, jogos)
    else:
        print("Retornando ao menu inicial...")
        limpar_cmd(True)

#Função para cadastrar os grupos
def cadastrar_grupos(grupos, jogos): #escolhe o grupo para cadastrar e chama a função para inserir as seleções 
    letra = pegar_letra(grupos)

    if len(grupos[letra]) >0:
        print("Este grupo já está cadastrado!\n")
        
    else:
        while len(grupos[letra]) < 4:
            limpar_cmd()
            inserir_selecao(grupos, letra)

        atualizar_partidas(grupos[letra], letra, jogos)   #{a X b: {equipe 1: a, equipe 2: b}}

        print("Cadastro realizado!\n")
    
    print("Retornando ao menu inicial...")
    limpar_cmd(True)
        
#Função para pegar um nome válido de seleção ( não aceita por exemplo: '1234' como seleção)
def pegar_selecao(msg):
    equipe = input(msg).lower()
    while not equipe.replace(' ', '').isalpha():    #permite nome composto. Ex: Coreia Do Sul
        print("Nome inválido!")
        limpar_cmd(True)
        equipe = input(msg).lower()
    return equipe

#Verifica se a seleção já está em algum grupo
def verificar_selecao(selecao, grupos):
    for grupo in grupos:
        if selecao in grupos[grupo]:
            return True, grupo
    
    return False, ""

#Função para inserir as seleções no grupo escolhido
def inserir_selecao(grupos, letra): 

    equipe = pegar_selecao(f"Digite o nome da seleção:\n>>> ").title()

    indisponivel, grupo = verificar_selecao(equipe, grupos)
    if indisponivel:
        print(f"Esta seleção ja está no grupo {grupo}!")
        limpar_cmd(True)
        inserir_selecao(grupos, letra)
    
    else:
        grupos[letra].append(equipe)    #dicionário com chave 'A até H', onde cada chave recebe uma lista com 4 seleções
        limpar_cmd()

#Função para organizar as seleções que irão se enfrentar em um grupo
def atualizar_partidas(equipes, letra, jogos):
    jogos_do_grupo = {}
    jogo = {}
    
    if len(equipes) != 0:
        for i in range(2,3):
            equipe1 = 2
            nome = equipes[equipe1] + " x " + equipes[i+1]
            jogo["equipe 1"] = equipes[equipe1]
            jogo["equipe 2"] = equipes[i+1]
            jogos_do_grupo[nome] = jogo        
            jogo = {}

        for i in range(1,3):
            equipe1 = 1
            nome = equipes[equipe1] + " x " + equipes[i+1]
            jogo["equipe 1"] = equipes[equipe1]
            jogo["equipe 2"] = equipes[i+1]
            jogos_do_grupo[nome] = jogo
            jogo = {}

        for i in range(0,3):
            equipe1 = 0
            nome = equipes[equipe1] + " x " + equipes[i+1]
            jogo["equipe 1"] = equipes[equipe1]
            jogo["equipe 2"] = equipes[i+1]
            jogos_do_grupo[nome] = jogo
            jogo = {}

    jogos[letra] = {}
    for partida in jogos_do_grupo.keys():
        jogos[letra][partida] = jogos_do_grupo[partida]   #{"A": {a X b: {equipe 1: a, equipe 2: b}}}

    if len(jogos[letra]) == 0:
        jogos.pop(letra)
    #{a X b: {equipe 1: a, equipe 2: b}}

#Função para cadastrar os jogos de um grupo
def cadastrar_jogos(grupos, jogos):
    letra = pegar_letra(grupos)
    if letra in jogos.keys():
        para_deletar = []
        partidas = list(jogos[letra].keys())
        for p in partidas:
            if len(jogos[letra][p]) > 2:
                para_deletar.append(p)
        for p in para_deletar:
            partidas.remove(p)
        if len(partidas) == 0:
            print("Todos os jogos deste grupo já foram cadastrados!\n")
            print("Retornando ao menu inicial...")
            limpar_cmd(True)

            return True

        indice_partida = menu("ESCOLHA A PARTIDA", *partidas)
        partida = partidas[indice_partida]

        jogos[letra][partida]['estadio'] = input("Digite o nome do estádio:\n>>> ").title()
        limpar_cmd()
        jogos[letra][partida]['data'] = pegar_data()
        jogos[letra][partida]['horario'] = pegar_hora()
        lancar_resultados(grupos, jogos, letra, partida)
        return False
    
    else:
        return True

#Função para cadastrar o resultado dos jogos
def lancar_resultados(grupos, jogos, letra, jogo):

    dados = list(jogos[letra][jogo].keys())  #pega os dados de um jogo
    dados.remove("equipe 1") #tira o nome das equipes
    dados.remove("equipe 2") # 

    if len(dados) == 0: 
        print("Este jogo não foi cadastrado ainda!")
    elif len(dados) == 5:
        print("O resultado deste jogo ja foi lançado!")  #Existe a opção de editar jogo, aqui é cadastrar
    else:
        gols = pegar_placar(jogos[letra][jogo]['equipe 1'], jogos[letra][jogo]['equipe 2'])
        cartoes = pegar_cartoes(jogos[letra][jogo]['equipe 1'], jogos[letra][jogo]['equipe 2'])
        jogos[letra][jogo]['placar'] = gols
        jogos[letra][jogo]['cartoes'] = cartoes
    
    print("Retornando ao menu inicial...")
    limpar_cmd(True)

################ Funções para pegar as informações dos jogos ##################

#Função para pegar o mês e dia do jogo
def pegar_data():
    
    print("Digite o número do dia: ")
    dia = pegar_int()
    while dia > 31 or dia < 1:
        print("Dia inválido!")
        limpar_cmd(True)
        print("Digite o número do dia: ")
        dia = pegar_int()
    
    print("Digite o número do mês: ")
    mes = pegar_int()
    while mes > 12 or mes < 1:
        print("Mês inválido!")
        limpar_cmd(True)
        print("Digite o número do mês: ")
        mes = pegar_int()
    
    return f'{dia}/{mes}'

#Função para pegar a hora do jogo
def pegar_hora():
    hora = input("Digite a hora do jogo: \n>>> ")
    limpar_cmd()
    while not hora.isdigit() or int(hora) > 23:
        print("Hora inválida!")
        limpar_cmd(True)
        hora = input("Digite a hora do jogo: \n>>> ")
        limpar_cmd()                                                                                                                                  #windowns>linux

    return f'{hora}hrs'

#Função para pegar o placar do jogo
def pegar_placar(selecao1, selecao2):
    print(f"Digite o número de gols - {selecao1}: ")
    gols1 = pegar_int()
    print(f"Digite o número de gols - {selecao2}: ")
    gols2 = pegar_int()
    return f'{gols1} x {gols2}'

#Função para pegar o cartões do jogo
def pegar_cartoes(selecao1, selecao2):
    print(f"Digite o número de cartões amarelo - {selecao1}: ")
    cartoes1 = pegar_int()
    print(f"Digite o número de cartões amarelo - {selecao2}: ")
    cartoes2 = pegar_int()
    return f'{cartoes1} x {cartoes2}'
    
################## Funções para exibir os grupos e os jogos #####################
    
#Função para mostrar os grupos ou os jogos cadastrados
def visualizacoes(grupos, jogos):
    vazio = 0
    escolha = menu("ESCOLHA OQUE VISUALIZAR", "Grupos", "Jogos", "Voltar")

    if escolha == 0:
        for chave in grupos:
            if len(grupos[chave]) > 0:
                corda()
                print(f"°Grupo {chave}\n")
                for time in grupos[chave]:
                    print(f"-> {time}")
                print()
            else:
                vazio +=1
        if vazio == 8:
            print("Ainda não há grupos cadastrados!")
  
    elif escolha == 1:
        if len(jogos) > 0:
            for grupo in jogos:
                n = 0
                corda()
                print(f"\n°Grupo {grupo}\n")
                for partida in jogos[grupo]:
                    n += 1
                    
                    print(f'{n}. {partida} -> ', end  ="")
                    for dado in jogos[grupo][partida]:
                        if dado not in ['equipe 1', "equipe 2"]:
                            print(f'( {dado}: {jogos[grupo][partida][dado]} )', end = " | ")           
                    print('\n')
        else:
            print("Ainda não há jogos cadastrados!")
    
    corda()
    input('Pressione ENTER para continuar...')
    limpar_cmd()

#################### Funções para edição dos grupos e jogos ####################

#Função para escolha do que editar ( grupos ou jogos )
def edicoes(grupos, jogos):
    escolha = menu("ESCOLHA OQUE ALTERAR", "Grupos", "Jogos", "Voltar")
    if escolha == 0:
        editar_grupos(grupos, jogos)     
    elif escolha == 1:
        editar_jogos(grupos, jogos)
    else:
        print("Retornando ao menu inicial...")
        limpar_cmd(True)

#Função para editar um grupo
def editar_grupos(grupos, jogos):
    letra = pegar_letra(grupos)

    if len(grupos[letra]) == 0:
        print("Este grupo ainda não foi cadastrado!")
    
    else:
        acao = menu("ESCOLHA UMA AÇÃO", "Limpar Grupo", "Trocar uma Seleção", "Voltar")
        if acao == 0:
            grupos[letra] = []
            atualizar_partidas(grupos[letra], letra, jogos)
            
        elif acao == 1:
            indice_selecao = menu('ESCOLHA QUAL SELEÇÃO REMOVER', *grupos[letra],'Voltar')
            if indice_selecao!=4:
                selecao = grupos[letra][indice_selecao]
                nova_selecao = pegar_selecao("Digite o nome da nova seleção:\n>>> ").title()
                indisponivel, n_letra = verificar_selecao(nova_selecao, grupos)   #verificar se a nova seleção já está em algum grupo

                if indisponivel:
                    troca = menu(f"SELEÇÃO NO GRUPO {n_letra}!\n\nDeseja Trocar?", "Sim", "Não")
                    if troca == 0:
                        grupos[letra][indice_selecao] = nova_selecao
                        n_indice = grupos[n_letra].index(nova_selecao)
                        grupos[n_letra][n_indice] = selecao
                        atualizar_partidas(grupos[n_letra], n_letra, jogos)
                        atualizar_partidas(grupos[letra], letra, jogos)
                    else:
                        print("Cancelando operação...")
                        limpar_cmd(True)            
                
                else:
                    grupos[letra][indice_selecao] = nova_selecao
                    atualizar_partidas(grupos[letra], letra, jogos)
       
    print("Retornando ao menu inicial...")
    limpar_cmd(True)

#O dicionário de jogos tem esse formato
#{"A": {a x b: {equipe 1: a, equipe 2: b, estadio: e, data: d, ...}, a x c...}}
#Informações que podem ser alteradas -> estadio, data, horario, placar, cartões quando houver 

#Função para editar um jogo
def editar_jogos(grupos, jogos):
    letra = pegar_letra(grupos)

    if len(grupos[letra]) == 0:
        print("Este grupo ainda não foi cadastrado!")

    else:
        partidas = list(jogos[letra].keys())
        indice_jogo = menu("ESCOLHA O JOGO", *partidas)
        jogo = partidas[indice_jogo]

        dados = list(jogos[letra][jogo].keys())
        dados.remove("equipe 1")
        dados.remove("equipe 2")

        if len(dados) == 0: 
            print("Este jogo não tem dados!")

        else:
            acao = menu("OQUE DESEJA FAZER", "Alterar dados", "Apagar dados", "Voltar")
            if acao == 0:
                escolha = menu("ESCOLHA QUAL DADO ALTERAR", *dados, 'Voltar')
                if escolha != 5:

                    dado  = dados[escolha]
                    if dado == "estadio":
                        n_informacao = input("Digite o nome do novo estádio:\n>>> ")
                        jogos[letra][jogo][dado] = n_informacao
                    elif dado == "data":
                        n_informacao = pegar_data()
                        jogos[letra][jogo][dado] = n_informacao
                    elif dado == "horario":
                        n_informacao = pegar_hora()
                        jogos[letra][jogo][dado] = n_informacao
                    elif dado == "placar":
                        n_informacao = pegar_placar(jogos[letra][jogo]['equipe 1'], jogos[letra][jogo]['equipe 2'])
                        jogos[letra][jogo][dado] = n_informacao
                    elif dado == "cartoes":
                        n_informacao = pegar_cartoes(jogos[letra][jogo]['equipe 1'], jogos[letra][jogo]['equipe 2'])
                        jogos[letra][jogo][dado] = n_informacao
            
            elif acao == 1:
                dado = jogos[letra][jogo]
                dado.pop('estadio')
                dado.pop('data')
                dado.pop('horario')
                dado.pop('cartoes')
                dado.pop('placar')
                jogos[letra][jogo] = dado

    print("Retornando ao menu inicial...")
    limpar_cmd(True)

#################### Funções para os requisitos no relatório final ###################

#Função para pegar os gols em uma partida
def pegar_gols(partida):
    time1,time2 = partida['placar'].split(" x ")
    return int(time1), int(time2)

#Função para pegar total de gols por jogo de um grupo
def total_grupo(jogos_grupo):
    total = 0
    for partida in jogos_grupo:
        gols_time1, gols_time2 = pegar_gols(jogos_grupo[partida])
        total += gols_time1+gols_time2
    return total

#Função para calcular as médias
def medias_jogos(jogos):
    medias = []
    media_geral = 0
    qnt_jogos = 0
    for grupo in jogos:
        gols = total_grupo(jogos[grupo])
        media_geral += gols
        qnt_jogos += 6  #por grupo
        medias.append(gols/len(jogos[grupo].keys()))

    media_geral = media_geral/qnt_jogos if qnt_jogos != 0 else 0
    return media_geral, medias

#Função para saber a quantidade de gols de cada time
def gols_time(jogos_grupo, nome):
    total = 0
    for partida in jogos_grupo: #note que partida == timeA X timeB
        if nome in partida:
            gols1, gols2 = pegar_gols(jogos_grupo[partida])
            total += gols1 if jogos_grupo[partida]['equipe 1'] == nome else gols2
    
    return total

#Função para verificar quem fez mais gols
def mais_gols(jogos):
    maior = -1
    jogo = ""
    for grupo in jogos:
        for partida in jogos[grupo]:
            gols1, gols2 = pegar_gols(jogos[grupo][partida])
            if gols1 > maior or gols2 > maior:
                jogo = jogos[grupo][partida]
                if gols1 > gols2:
                    maior = gols1
                else:
                    maior = gols2
    return jogo

#Função para verificar se um time ganhou, perdeu ou empatou
def pontuacao(partida, time):
    gols1, gols2 = pegar_gols(partida)
    if partida['equipe 1'] == time:
        if gols1 > gols2:
            return 3
        elif gols2 == gols1:
            return 1
        else:
            return 0
    
    else:
        if gols2 > gols1:
            return 3
        elif gols2 == gols1:
            return 1
        else:
            return 0

#Função para calcular saldo de gols
def saldo_de_gols(jogos_grupo, nome):
    total = 0
    for partida in jogos_grupo: #note que partida == timeA X timeB
        if nome in partida:
            gols1, gols2 = pegar_gols(jogos_grupo[partida])
            total += gols1-gols2 if jogos_grupo[partida]['equipe 1'] == nome else gols2-gols1
    
    return total

#Função para calcular pontos
def pontos_totais(letra, jogos, selecao):
    pontos = 0
    for partida in jogos[letra]:   
        if selecao in partida: 
            pontos += pontuacao(jogos[letra][partida], selecao)      
    
    return pontos
    
#Função para ver a quantidade de cartões em uma partida
def ler_cartoes(partida):
    time1,time2 = partida['cartoes'].split(" x ")
    return int(time1), int(time2)

#Função para calcular a quantidade de cartões de um time
def quantidade_cartoes(jogos_grupo, nome):
    total = 0
    for partida in jogos_grupo: #note que partida == timeA X timeB
        if nome in partida:
            cartoes1, cartoes2 = ler_cartoes(jogos_grupo[partida])
            total += cartoes1 if partida['equipe 1'] == nome else cartoes2
    
    return total

#Função para verificar qual seleção possui o maior "score"
def classificar(letra, grupo, jogos):
    
    selecao1 = grupo[0] 
    
    for s in range(1, len(grupo)): 
        s1_pontos = pontos_totais(letra, jogos, selecao1)
        s_pontos = pontos_totais(letra, jogos, grupo[s])

        if s1_pontos < s_pontos:  #classifica pela pontuação
            selecao1 = grupo[s]

        elif  s_pontos == s1_pontos:  #classifica pelo saldo de gols
            s1_gols = saldo_de_gols(jogos[letra], selecao1)
            s_gols = saldo_de_gols(jogos[letra], grupo[s])
            if s1_gols < s_gols:
                selecao1 = grupo[s]

            elif s1_gols == s_gols:   #classifica pelos gols marcados
                gols_s1 = gols_time(jogos[letra], selecao1)
                gols_s = gols_time(jogos[letra], grupo[s])
                if gols_s1 < gols_s:
                    selecao1 = grupo[s]

                elif gols_s1 == gols_s:   #classifica pela quantidade de cartoes
                    cartoes_s1 = quantidade_cartoes(jogos[letra], selecao1)
                    cartoes_s = quantidade_cartoes(jogos[letra], grupo[s])
                    if cartoes_s1 < cartoes_s:
                        selecao1 = grupo[s] 
    
    return selecao1

#Função para pegar os classificados
def classificados(letra, grupo, jogos):
    selecoes = grupo.copy()
    primeiro = classificar(letra, selecoes, jogos)
    selecoes.remove(primeiro)
    segundo = classificar(letra, selecoes, jogos)
    
    return primeiro, segundo

#Função que define os confrontos das oitavas
def jogos_das_oitavas(grupos, jogos):
    partidas = []
    times1 = []
    times2 = []

    for grupo in grupos: #separa as duplas
        time1, time2 = classificados(grupo, grupos[grupo], jogos)
        times1.append(time1)
        times2.append(time2)

    #Alternando entre as duplas
    for i in range(len(times1)):
        partidas.append(f"{times1[i]} x {times2[i+1]}" if i %2 == 0 else f"{times1[i]} x {times2[i-1]}")
    
    return partidas

#Função para verificar se todos os resultados ja foram lançados
def liberar_relatorio(jogos):
    for grupo in jogos:
        for partidas in jogos[grupo]:
            if 'placar' not in jogos[grupo][partidas].keys():
                return False
    return True if len(jogos) > 0 else False

#Função para exibir o relatório final
def relatorio(grupos, jogos):

    letras = list(grupos.keys())
    media_geral, medias = medias_jogos(jogos)
    partida = mais_gols(jogos)
    partidas = jogos_das_oitavas(grupos, jogos)

    escolha=menu('QUAL INFORMAÇÃO MOSTRAR','Confrontos das oitavas','Médias de gols','Maior goleada','Todas as informações','Voltar')
    
    if escolha==0:
        corda()
        print("OITAVAS DE FINAL\n")      #Partidas das oitavas
        for i in range(len(partidas)):
            print(f"{i+1} -> {partidas[i]}")
        print()
        corda()

        input('Pressione ENTER para continuar...')
        limpar_cmd()
    
    elif escolha==1:    
        corda()
        print("ESTATÍSTICAS DA FASE DE GRUPO\n")     #Médias de gols
        print(f"Media de gols por jogo: {round(media_geral,2)}")
        for i in range(len(letras)):
            print(f"Média de gols do grupo {letras[i].upper()}: {round(medias[i],2)}")
        print()
        corda()

        input('Pressione ENTER para continuar...')
        limpar_cmd()
    
    elif escolha==2:
        corda()
        print("PARTIDA COM MAIOR GOLEADA\n")
        print(f"{partida['equipe 1'].title()} ({partida['placar'].split(' x ')[0]}) x ({partida['placar'].split(' x ')[1]}) {partida['equipe 2'].title()}")
        print(f"Ocorreu no estádio: {partida['estadio']} às {partida['horario']} do dia {partida['data']}")
        print(f"{partida['equipe 1'].title()} ficou com {partida['cartoes'].split(' x ')[0]} cartão(s) amarelo")
        print(f"{partida['equipe 2'].title()} ficou com {partida['cartoes'].split(' x ')[1]} cartão(s) amarelo\n")
        corda() 

        input('Pressione ENTER para continuar...')
        limpar_cmd()

    elif escolha==3:    
        corda()
        print("OITAVAS DE FINAL\n")      #Partidas das oitavas
        for i in range(len(partidas)):
            print(f"{i+1} -> {partidas[i]}")
        print()
        corda()

        print("ESTATÍSTICAS DA FASE DE GRUPO\n")     #Dados requisitados
        print(f"Media de gols por jogo: {round(media_geral,2)}")
        for i in range(len(letras)):
            print(f"Média de gols do grupo {letras[i].upper()}: {round(medias[i],2)}")
        print()
        corda()

        print("PARTIDA COM MAIOR GOLEADA\n")
        print(f"{partida['equipe 1'].title()} ({partida['placar'].split(' x ')[0]}) x ({partida['placar'].split(' x ')[1]}) {partida['equipe 2'].title()}")
        print(f"Ocorreu no estádio: {partida['estadio']} às {partida['horario']} do dia {partida['data']}")
        print(f"{partida['equipe 1'].title()} ficou com {partida['cartoes'].split(' x ')[0]} cartão(s) amarelo")
        print(f"{partida['equipe 2'].title()} ficou com {partida['cartoes'].split(' x ')[1]} cartão(s) amarelo\n")
        corda()
        
        input('Pressione ENTER para continuar...')
        limpar_cmd() 
    
    else:
        print("Retornando ao menu inicial...")
        limpar_cmd(True)

################ Funções para guardar em arquivo.txt ################

#Função pra ler um arquivo
def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'r')
        dados = eval(arquivo.readline())
        arquivo.close()
    except Exception as exc:
        return 1, {}   #break e flag pra caso algum erro
    
    if len(dados) > 0:
        return 0, dados

    return 1, {}

#Função para escrever em um arquivo
def escrever_arquivo(dado, nome):
    try:
        arquivo = open(nome, 'w')
        arquivo.write(str(dado))
        arquivo.close()
    except Exception:
        return 1    #break pra caso algum erro

    return 0

#Função para ler os dados do arquivo e tranformar em dicionário
def carregar_dados(grupos, jogos):
    erro, dado = ler_arquivo('grupos.txt')
    if erro == 0:
        print("Arquivo grupos.txt carregado com sucesso!")
        grupos = dict(dado)
    else:
        print("Não foi possível carregar o arquivo grupos.txt")
    
    erro, dado = ler_arquivo('jogos.txt')
    if erro == 0:
        print("Arquivo jogos.txt carregado com sucesso!")
        jogos = dict(dado)
    else:
        print("Não foi possível carregar o arquivo jogos.txt")
    
    return grupos, jogos

#Guardar os dados dos jogos e dos grupos
def guardar_dados(grupos, jogos):
    erro = escrever_arquivo(grupos, 'grupos.txt')
    if erro == 0:
        print("Arquivo grupos.txt escrito com sucesso!")
    else:
        print("Não foi possível escrever o arquivo grupos.txt")
    
    erro = escrever_arquivo(jogos, 'jogos.txt')
    if erro == 0:
        print("Arquivo jogos.txt escrito com sucesso!\n")
    else:
        print("Não foi possível escrever o arquivo jogos.txt\n")

#################### Função principal contendo todas as outras ####################
def main():
    grupos = {"A": [], "B": [], "C": [], "D": [], "E": [], "F": [], "G": [], "H": []}
    jogos = {}    #{letra do grupo: {partida: {dados}, partida2: {dados}, ...}}
    grupos, jogos = carregar_dados(grupos, jogos)
    limpar_cmd(True)
    escolha = -1

    while escolha != 4:
        escolha = menu('\n'+'    '*15+'COPA DO MUNDO 2022\n', "Cadastrar", "Editar", "Visualizar", "Relatório Final" ,"Sair")
        
        if escolha == 4:
            print("Encerrando...\n")
        
        elif escolha == 0:
            cadastros(grupos, jogos)
            guardar_dados(grupos, jogos)    
        
        elif escolha == 1:
            edicoes(grupos, jogos)
            guardar_dados(grupos, jogos)     

        elif escolha == 2:
            visualizacoes(grupos, jogos)

        elif escolha == 3:
            if liberar_relatorio(jogos):
                relatorio(grupos, jogos)
               
            else:
                print("Os resultados ainda não foram lançados!")
                limpar_cmd(True)
        
    guardar_dados(grupos, jogos)
        
if __name__ == "__main__":   
    main()