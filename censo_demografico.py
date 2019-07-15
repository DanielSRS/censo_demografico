# ----------------------------------------------------------------------------------------------------------------------
#                                                   Importar arquivos
# ----------------------------------------------------------------------------------------------------------------------
arquivo = open('regioes.txt', 'r')
regioes = arquivo.readlines()
arquivo.close()

arquivo = open('tecnicosIBGE.txt', 'r')
tecnicosIBGE = arquivo.readlines()
arquivo.close()


# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                                 menu pré-cadastro
# ----------------------------------------------------------------------------------------------------------------------
while True:
    print('A - Cadastrar novo tecnico')
    print('B - Realizar pesquisa')
    resposta = input('\nSelecione uma opção: ')
    if resposta == 'b':
        resposta = 0
        break

# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                                   Menu estatístticas
# ----------------------------------------------------------------------------------------------------------------------
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
    if resposta == '1':
        break
    elif resposta == '2':
        break
    elif resposta == '3':
        break
    elif resposta == '4':
        break
    elif resposta == '5':
        break
    elif resposta == '6':
        break
    elif resposta == '7':
        break
    elif resposta == '8':
        break
    elif resposta == '9':
        break

# ______________________________________________________________________________________________________________________