from copy import deepcopy


def main():

    # ------------------------------------------------------------------------------------------------------------------
    #                                                   Importar arquivos
    # ------------------------------------------------------------------------------------------------------------------
    regioes = lerArquivo('regioes.txt')  # usando diretorio de testes, para não modificar os arquivos
    tecnicosIBGE = lerArquivo('tecnicosIBGE.txt')
    exemploPesquisa = lerArquivo('ExemploPesquisaV3.txt')
    
    #  desagrupa os dados
    regioes = separarDados(regioes) 
    exemploPesquisa = separarDados(exemploPesquisa)
    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                         menu de cadastro ou estatisticas
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        print('A - Cadastrar novo tecnico')
        print('B - Exibir estatisticas')
        resposta = input('\nSelecione uma opção: ')
        if resposta == 'b':
            break
        elif resposta == 'a':  # Cadastro de tecnicos. Precisa ser revisado.
            resposta = 0
            nome = input('Nome do técnico \n\n\tResposta: ')
            sexo = input('Sexo [F para feminino e M para masculino] \n\n\tResposta: ')
            nascimento = input('Data de nascimento [No formato DD/MM/AAAA] \n\n\tResposta: ')
            matriculaTecnico(nome, sexo, nascimento, tecnicosIBGE)

    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                                   Menu estatísticas
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        print('1 - Números de domicílios utilizados para a coleta')
        print('2 - Número de domicílios particulares que já estão pagos, quantos ainda estão pagando e alugados;')
        print('3 - Quantos domicílios por cidade possuem banheiro e quantos não possuem;')
        print('4 - A forma mais comum de abastecimento de água por cidade;')
        print('5 - O percentual de domicílios por cidade que ainda não possuem energia elétrica;')
        print('6 - O percentual de moradores que participaram da entrevista por cor ou raça.')
        print('7 - A região com maior número de municípios pesquisados.')
        print('8 - Exibir todos os dados')
        print('9 - Encerrar aplicação:')
        resposta = input('\nDigite sua escolha: ')
        print('\n\n\n')
        if resposta == '1':
            numeroDeDomicilios(exemploPesquisa)
            print('\n\n')
            
        elif resposta == '2':
            pagamentoDosDomicilios(exemploPesquisa)
            print('\n\n')

        elif resposta == '3':  # Contagem de domicilios com banheiros, por cidade
            banheiroEmCasa(exemploPesquisa, regioes)
            print('\n\n')
            
        elif resposta == '4':  # Forma mais comum de abastecimeno de agua por cidade
            
            formaMaisCommumAgua(exemploPesquisa, regioes)
            print('\n\n')

        elif resposta == '5':
            energiaEmCasas(exemploPesquisa, regioes)
            print('\n\n')

        elif resposta == '6':
            percentualPorCorOuRaca(exemploPesquisa)
            print('\n\n')

        elif resposta == '7':  
            regiaoComMaisCidades(regioes, exemploPesquisa)
            print('\n\n')
  
        elif resposta == '8':  #  Exibe todos os dados
            numeroDeDomicilios(exemploPesquisa)
            print('\n\n')
            pagamentoDosDomicilios(exemploPesquisa)
            print('\n\n')
            banheiroEmCasa(exemploPesquisa, regioes)
            print('\n\n')
            formaMaisCommumAgua(exemploPesquisa, regioes)
            print('\n\n')
            energiaEmCasas(exemploPesquisa, regioes)
            print('\n\n')
            percentualPorCorOuRaca(exemploPesquisa)
            print('\n\n')
            regiaoComMaisCidades(regioes, exemploPesquisa)
            print('\n\n')

        elif resposta == '9':  # Finaliza o programa
            exit()

    # __________________________________________________________________________________________________________________

def lerArquivo(nome: str):  # Função para ler um arquivo e retornar seus dados numa lista
    arquivo = open(nome, 'r')
    aux = arquivo.readlines()
    arquivo.close()
    return aux
# ______________________________________________________________________________________________________________________

# cadastra novo tecnico
def matriculaTecnico(nome: str, sexo: str, nascimento: str, listaTecnicosCadastrados: list):
    # Gera numero de matricula avaliando cadastros preexistentes
    matricula = 'T' + str(len(listaTecnicosCadastrados) - 1)
    tecnico = matricula + ';' + nome + ';' + sexo + ';' + nascimento + '\n'
    if listaTecnicosCadastrados[len(listaTecnicosCadastrados) - 1] == ' \n' or listaTecnicosCadastrados[len(
        listaTecnicosCadastrados) - 1] == '\n':  # Caso tenha uma linha vazia no final do arquivo
        listaTecnicosCadastrados[len(listaTecnicosCadastrados) - 1] = tecnico
        listaTecnicosCadastrados.append('\n')
    else:
        lista.append(tecnico)
        lista.append('\n')
    escreverArquivo(listaTecnicosCadastrados, 'tecnicosIBGE.txt')
# ______________________________________________________________________________________________________________________

def escreverArquivo(dadosParaEscrita: list, nomeArquivo: str):  # Escrever dados num arquivo
    arquivo = open(nomeArquivo, 'w')
    arquivo.writelines(dadosParaEscrita)
    arquivo.close()
# ______________________________________________________________________________________________________________________

def encontrarCidade(codigoIBGE: str, regioes: list): #  Encontra o nome da cidade a partir do codigo IBGE
    for h in regioes:
        if h[2] == codigoIBGE:
            return h[1]
    return 'cidade'  #  Retorna 
# ______________________________________________________________________________________________________________________

def buscarNaLista(nome: str, lista: list):  # Função de busca
    for contador in range(len(lista)):
        if lista[contador].find(nome) != -1:
            return True
    return False
# ______________________________________________________________________________________________________________________

def separarDados(dadosDoArquivo: list):  # Separa informações contidas na mesma string 
    contarLetrasPalavra = 0
    matrizDadosArquivo: list = [] 
    Laux = [] 
    for contadorTamanhoDadosArquivo in range (len(dadosDoArquivo)):
        dadosDeUmCadastro: str = dadosDoArquivo[contadorTamanhoDadosArquivo]
        for letra in dadosDeUmCadastro:
            if letra != ';' and contarLetrasPalavra == 0:
                v = letra
            elif letra != ';' and letra != '\n' and contarLetrasPalavra != 0:
                v = v + letra
            elif letra == ';' and contarLetrasPalavra != 0:
                Laux.append(v)
                contarLetrasPalavra == -1
                v = ''  # 'apaga' a string para começar a armazenar novos caracteres
            elif letra == '\n':
                Laux.append(v)
                matrizDadosArquivo.append(deepcopy(Laux))
                Laux [:] = []
                contarLetrasPalavra = -1
            contarLetrasPalavra = contarLetrasPalavra + 1
            
    return matrizDadosArquivo
# ______________________________________________________________________________________________________________________

def regiaoDoPais(cidade: str, regioes: list):  # Determina a qual região do país pertençe cada cidade
    for k in regioes:
        if k[2] == cidade:
            estado = k[3]
            if estado == 'MA' or estado == 'PI' or estado == 'CE' or estado == 'RN' or estado == 'PB' or estado == 'PE' or estado == 'AL' or estado == 'SE' or estado == 'BA':
                return 'nordeste'
            elif estado == 'AM' or estado == 'RR' or estado == 'AP' or estado == 'PA' or estado == 'TO' or estado == 'RO' or estado =='AC':
                return 'norte'
            elif estado == 'SP' or estado == 'RJ' or estado == 'ES' or estado == 'MG':
                return 'sudeste'
            elif estado == 'DF' or estado == 'GO' or estado == 'MT' or estado == 'MS':
                return 'centro-oeste'
            elif estado == 'PR' or estado == 'SC' or estado == 'RS':
                return 'sul'
# ______________________________________________________________________________________________________________________

#  Conta o numero de domicilios na pesquisa
def numeroDeDomicilios(exemploPesquisa: list):
    print('Números de domicílios utilizados para a coleta: {}'.format(len(exemploPesquisa) - 1))
    return 0
# ______________________________________________________________________________________________________________________

#  Conta as casas com energia eletrica, e as que naõ tem (por cidade)
def energiaEmCasas(exemploPesquisa: list, regioes: list):
    casasComEnergia = [['cidade', 'possuiEnergia', 'naoPossuiEnergia']]
    for x in exemploPesquisa:
        
        cidade = x[1]
        if x[11].isdecimal():
            possuienergia = int(x[11])
            for c in casasComEnergia:
                if c[0] == cidade:
                    if possuienergia == 1 or possuienergia == 2:
                        c[1] += 1
                        break
                    elif possuienergia == 3:
                        c[2] += 1
                        break
                else:
                    if possuienergia == 1 or possuienergia == 2:
                        casasComEnergia.append([cidade, 1, 0])
                        break
                    elif possuienergia == 3:
                        casasComEnergia.append([cidade, 0, 1])
                        break
    del(casasComEnergia[0])
    for m in casasComEnergia:
        tota = m[1] + m[2]
        tm = m[1] * 100
        ntm = m[2] * 100
        #print('{} {} {}'.format(tota, tm, ntm))
        print(encontrarCidade(m[0], regioes) + ': ' + str(tm / tota) + '% possui energia, ' + str(ntm / tota) + '% não possui')
    
    return 0
# ______________________________________________________________________________________________________________________


def banheiroEmCasa(exemploPesquisa: list, regioes: list):
    banheiroPorCidade = [['codigoDaCidade', 'quantidadeDeBanheiros', 'quantidadeDeSemBanheiros']]
    banheiroAuxiliar = 0
    for i in exemploPesquisa:
        temOuNaoBanheiro = i[6]
        if temOuNaoBanheiro.isdecimal():
            temOuNaoBanheiro = int(temOuNaoBanheiro)
            if 0 < temOuNaoBanheiro <= 9:
                cidade = i[1]
                for j in banheiroPorCidade:
                    if j[0] == cidade:
                        j[1] += 1
                        banheiroAuxiliar += 1
                if banheiroAuxiliar == 0:
                    banheiroPorCidade.append([cidade, 1, 0])
                banheiroAuxiliar = 0
            else: 
                cidade = i[1]
                for j in banheiroPorCidade:
                    if j[0] == cidade:
                        j[2] += 1
                        banheiroAuxiliar += 1
                if banheiroAuxiliar == 0:
                    banheiroPorCidade.append([cidade, 0, 1])
                banheiroAuxiliar = 0
                
    del(banheiroPorCidade[0])  # Elimina linha de referencia

    for p in banheiroPorCidade:  #  Exibe os dados
        cdd = encontrarCidade(p[0], regioes)
        print(cdd + ': ' + str(p[1]) + ' possuem banheiro, ' + str(p[2]) + ' não possuem')

    return 0
# ______________________________________________________________________________________________________________________
            
def pagamentoDosDomicilios(exemploPesquisa):
    domicilioParticularPago: int = 0
    domicilioParticularSendoPago: int = 0
    domicilioParticularAlugado: int = 0

    for i in exemploPesquisa:  # Para domicilios pagos
        if i[3] == '1' and i[5] == '1':
            domicilioParticularPago += 1

    for i in exemploPesquisa:  # Para domicilios sendo pagos
        if i[3] == '1' and i[5] == '2':
            domicilioParticularSendoPago += 1

    for i in exemploPesquisa:  # Para domicilios alugados
        if i[3] == '1' and i[5] == '3':
            domicilioParticularAlugado += 1

    print('Numero de domicilios particulares que ja estão pagos: {}'.format(domicilioParticularPago))
    print('Numero de domicilios particulares que estão sendo pagos: {}'.format(domicilioParticularSendoPago))
    print('Numero de domicilios particulares alugados: {}'.format(domicilioParticularAlugado))

    return 0
# ______________________________________________________________________________________________________________________


def regiaoComMaisCidades(regioes: list, exemploPesquisa: list):
    norte = nordeste = centroOeste = sul = sudeste = nem = 0
    for i in exemploPesquisa:
        cidade = i[1]
        reg = regiaoDoPais(cidade, regioes)
        if reg == 'norte':
            norte += 1
        elif reg ==  'nordeste':
            nordeste += 1
        elif reg == 'sudeste':
            sudeste += 1
        elif reg == 'sul':
            sul += 1
        elif reg == 'centro-oeste':
            centroOeste += 1 
        
    maisComum = 'nenhum'
    if norte > nem:
        nem = norte
        maisComum = 'norte'
    if nordeste > nem:
        nem = nordeste
        maisComum = 'nordeste'
    if sudeste > nem:
        nem = sudeste
        maisComum = 'sudeste'
    if sul > nem:
        nem = sul
        maisComum = 'sul'
    if centroOeste > nem:
        nem = centroOeste
        maisComum = 'Centro-oeste'
        
    print('A região do país com mais cidades pesquisadas: ' + maisComum)

    return 0
# ______________________________________________________________________________________________________________________

def percentualPorCorOuRaca(exemploPesquisa: list):
    branca = preta = parda = amarela = indigena = 0
    quantidadeDeIndividuos = 0
    for b in exemploPesquisa:
        
        if b[18].isdecimal():
            corDoIndividuo = int(b[18])
            quantidadeDeIndividuos += 1
            if corDoIndividuo == 1:
                branca += 1
            elif corDoIndividuo == 2:
                preta += 1
            elif corDoIndividuo == 3:
                amarela += 1
            elif corDoIndividuo == 4:
                parda += 1
            elif corDoIndividuo == 5:
                indigena += 1
    
    branca = (branca * 100) / quantidadeDeIndividuos
    preta = (preta * 100) / quantidadeDeIndividuos
    amarela = (amarela * 100) / quantidadeDeIndividuos
    parda = (parda * 100) / quantidadeDeIndividuos
    indigena = (indigena * 100) / quantidadeDeIndividuos

    print('Participantes da pesquisa por cor ou raça: \n')

    print(str(branca) + ' % branca')
    print(str(preta) + ' % preta')
    print(str(parda) + ' % parda')
    print(str(amarela) + ' % amarela')
    print(str(indigena) + ' % indigena')

    return 0
# ______________________________________________________________________________________________________________________

def formaMaisCommumAgua(exemploPesquisa: list, regioes: list):
    aguaPorCidade = [['codigoDaCidade', 'REDE GERAL DE DISTRIBUIÇÃO', 'POÇO OU NASCENTE NA PROPRIEDADE', 
        'POÇO OU NASCENTE FORA DA PROPRIEDADE', 'CARRO-PIPA', 'ÁGUA DA CHUVA ARMAZENADA EM CISTERNA', 
        'ÁGUA DA CHUVA ARMAZENADA DE OUTRA FORMA', 'RIOS, AÇUDES, LAGOS E IGARAPÉS', 'OUTRA', 
        ' POÇO OU NASCENTE NA ALDEIA', 'POÇO OU NASCENTE FORA DA ALDEIA']]
    
    for i in exemploPesquisa:

        forma = i[9]  #  Forma de abastecimento de agua
        if forma.isdecimal():
            forma = int(forma)
            
            cidade = i[1]  # Conta por cidade novas ocorrencias de cada tipo
            for j in aguaPorCidade:
                if j[0] == cidade:
                    if forma == 1:
                        j[forma] += 1
                        break
                    if forma == 2:
                        j[forma] += 1
                        break
                    if forma == 3:
                        j[forma] += 1
                        break
                    if forma == 4:
                        j[forma] += 1
                        break
                    if forma == 5:
                        j[forma] += 1
                        break
                    if forma == 6:
                        j[forma] += 1
                        break
                    if forma == 7:
                        fj[forma] += 1
                        break
                    if forma == 8:
                        j[forma] += 1
                        break
                    if forma == 9:
                        j[forma] += 1
                        break
                    if forma == 10:
                        j[forma] += 1
                        break
                else:  # Adiciona uma nova cidade e a primeira ocorrencia de um tipo de abastecimento
                    if forma == 1:
                        aguaPorCidade.append([cidade, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])
                        break
                    if forma == 2:
                        aguaPorCidade.append([cidade, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0])
                        break
                    if forma == 3:
                        aguaPorCidade.append([cidade, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0])
                        break
                    if forma == 4:
                        aguaPorCidade.append([cidade, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0])
                        break
                    if forma == 5:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0])
                        break
                    if forma == 6:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0])
                        break
                    if forma == 7:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0])
                        break
                    if forma == 8:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0])
                        break
                    if forma == 9:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0])
                        break
                    if forma == 10:
                        aguaPorCidade.append([cidade, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1])
                        break
    
    del(aguaPorCidade[0]) # o primeiro elemento nao é util; é então descartado (elemento de referencia)
    for t in aguaPorCidade:
        vmaior = t[1]
        if t[2] > vmaior:
            maior = 2
        if t[3] > vmaior:
            maior = 3
        if t[4] > vmaior:
            maior = 4
        if t[5] > vmaior:
            maior = 5
        if t[6] > vmaior:
            maior = 6
        if t[7] > vmaior:
            maior = 7
        if t[8] > vmaior:
            maior = 8
        if t[9] > vmaior:
            maior = 9
        if t[10] > vmaior:
            maior = 10

        forma = maior

        if forma == 1:
            forma =  'REDE GERAL DE DISTRIBUIÇÃO'
        if forma == 2:
            forma =  'POÇO OU NASCENTE NA PROPRIEDADE'
        if forma == 3:
            forma =  'POÇO OU NASCENTE FORA DA PROPRIEDADE'
        if forma == 4:
            forma =  'CARRO-PIPA'
        if forma == 5:
            forma =  'ÁGUA DA CHUVA ARMAZENADA EM CISTERNA'
        if forma == 6:
            forma =  'ÁGUA DA CHUVA ARMAZENADA DE OUTRA FORMA'
        if forma == 7:
            forma =  'RIOS, AÇUDES, LAGOS E IGARAPÉS'
        if forma == 8:
            forma =  'OUTRA'
        if forma == 9:
            forma =  ' POÇO OU NASCENTE NA ALDEIA'
        if forma == 10:
            forma =  'POÇO OU NASCENTE FORA DA ALDEIA'
        
        g = encontrarCidade(t[0], regioes)
        print(g + ': ' + forma)

    return 0
# ______________________________________________________________________________________________________________________

main()
