def lerArquivo(nome: str):  # Função para ler um arquivo e retornar seus dados numa lista
    arquivo = open(nome, 'r')
    aux = arquivo.readlines()
    arquivo.close()
    return aux

def matriculaTecnico(nome: str, sexo: str, nascimento: str, lista: list):  # cadastra novo tecnico
    matricula = 'T' + str(len(lista) - 1)
    tecnico = matricula + ';' + nome + ';' + sexo + ';' + nascimento + '\n'
    if lista[len(lista) - 1] == ' \n' or lista[len(lista) - 1] == '\n':
        lista[len(lista) - 1] = tecnico
        lista.append('\n')
    else:
        lista.append(tecnico)
        lista.append('\n')

def escreverArquivo(lista: list, nomeArquivo: str):  # Escrever dados num arquivo
    arquivo = open(nomeArquivo, 'w')
    arquivo.writelines(lista)
    arquivo.close()

def buscarNaLista(nome: str, lista: list):  # Função de busca
    for contador in range(len(lista)):
        if lista[contador].find(nome) != -1:
            return True
    return False

def main():

    # ------------------------------------------------------------------------------------------------------------------
    #                                                   Importar arquivos
    # ------------------------------------------------------------------------------------------------------------------
    regioes = lerArquivo('testes/regioes.txt')  # usando diretorio de testes, para não modificar os arquivos
    tecnicosIBGE = lerArquivo('testes/tecnicosIBGE.txt')
    
    print(len(tecnicosIBGE))
    print(tecnicosIBGE[len(tecnicosIBGE) - 1])
    print(tecnicosIBGE)
    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                                 menu de cadastro
    # ------------------------------------------------------------------------------------------------------------------
    while True:
        print('A - Cadastrar novo tecnico')
        print('B - Realizar pesquisa')
        resposta = input('\nSelecione uma opção: ')
        if resposta == 'b':
            resposta = 0
            tec = input('Digite o nome do tecnico: ')
            if buscarNaLista(tec, tecnicosIBGE):
                print('Tecnico valido')
            break
        elif resposta == 'a':  # Cadastro de tecnicos. Precisa ser revisado.
            nome = input('Nome do técnico [Somente primeiro nome] \n\n\tResposta: ')
            sexo = input('Sexo [F para feminino e M para masculino] \n\n\tResposta: ')
            nascimento = input('Data de nascimento [No formato DD/MM/AAAA] \n\n\tResposta: ')
            matriculaTecnico(nome, sexo, nascimento, tecnicosIBGE)
            print(lista)  #  Apenas para verificação. Apagar
            
    # __________________________________________________________________________________________________________________

    # ------------------------------------------------------------------------------------------------------------------
    #                                                   Pesquisa
    # ------------------------------------------------------------------------------------------------------------------
    print('1 - Importar arquivo de respostas: ')
    print('2 - Realizar pesquisa: ')
    print('3 - Cadastrar novo tecnico: ')
    
    #while True:
    #    login = input('Digite a matricula do tecnico: ')

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

    # __________________________________________________________________________________________________________________

#  if __name__ == '__main__':
#      main()

main()
