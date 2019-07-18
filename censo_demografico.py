# ----------------------------------------------------------------------------------------------------------------------
#                                                   Importar arquivos
# ----------------------------------------------------------------------------------------------------------------------
arquivo = open('testes/regioes.txt', 'r')  # usando diretorio de testes, para não modificar os arquivos
regioes = arquivo.readlines()
arquivo.close()

arquivo = open('testes/tecnicosIBGE.txt', 'r')  # usando diretorio de testes, para não modificar os arquivos
tecnicosIBGE = arquivo.readlines()
arquivo.close()
print(len(tecnicosIBGE))
print(tecnicosIBGE[len(tecnicosIBGE) - 1])
print(tecnicosIBGE)
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
    elif resposta == 'a':  # Cadastro de tecnicos. Precisa ser revisado.
        nome = input('Nome do técnico [Somente primeiro nome] \n\n\tResposta: ')
        sexo = input('Sexo [F para feminino e M para masculino] \n\n\tResposta: ')
        nascimento = input('Data de nascimento [No formato DD/MM/AAAA] \n\n\tResposta: ')
        matricula = 'T' + str(len(tecnicosIBGE) - 1)
        tecnico = matricula + ';' + nome + ';' + sexo + ';' + nascimento + '\n'
        if tecnicosIBGE[len(tecnicosIBGE) - 1] == ' \n' or tecnicosIBGE[len(tecnicosIBGE) - 1] == '\n':
            tecnicosIBGE[len(tecnicosIBGE) - 1] = tecnico
            tecnicosIBGE.append('\n')
            print('nao')
        else:
            tecnicosIBGE.append(tecnico)
            tecnicosIBGE.append('\n')
        print(tecnicosIBGE)
        
# ______________________________________________________________________________________________________________________

# ----------------------------------------------------------------------------------------------------------------------
#                                                   Menu estatísticas
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