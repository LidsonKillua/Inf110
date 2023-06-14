# p14.py
# Programador: Lidson Oliveira  
# Matrícula: 102961
# Criado em: 13/05/2021
# Atualizado em: 13/05/2021
# Este programa utiliza uma heurística dada em aula, além de conceitos de
# conjuntos, funções, classes, listas, dicionários, etc.. para criar um
# horário escolar, baseado em arquivos contendo disciplinas e dados de
# alunos matriculados e disciplinas a cursar.

import sys

####                                                                        ####
# DECLARE AQUI A CLASSE RegistroEscolar com todos os seus métodos (e atributos)#
####                                                                        ####
class RegistroEscolar:
    
    def __init__(self, anoletivo, periodo):
        self.periodo = (anoletivo, periodo)
        self.disciplinas = []
        self.matriculas = {}
        self.horario = []

    def set_disciplinas(self, nomearq):

        try:
            arq = open(nomearq)          
            linha = arq.readline().rstrip('\n')
            
            while linha != '':
                self.disciplinas.append(linha)
                linha = arq.readline().rstrip('\n')

            arq.close()            
                
        except OSError:
            print() 
        

    def set_matriculas(self, nomearq):

        try:
            arq = open(nomearq)          
            linha = arq.readline().rstrip('\n')
            dados = linha.split(',')
            
            while linha != '':
                materias = set()
                for i in range(len(dados)):
                    if i > 0:
                        materias.add(dados[i])

                self.matriculas[dados[0]] = materias
                
                linha = arq.readline().rstrip('\n')
                dados = linha.split(',')

            arq.close()            
                
        except OSError:
            print()         

    def set_horario(self):

        emptySet = set()
        conflito = [emptySet for d in self.disciplinas]

        for a in self.matriculas.keys():
          for d in range(len(self.disciplinas)):
              if self.disciplinas[d] in self.matriculas[a]: 
                  conflito[d] = conflito[d].union(self.matriculas[a])        
        
        restante = set(self.disciplinas)

        while restante != emptySet:
          i = 0
          d = self.disciplinas[i]
          while d not in restante:
            i = i + 1
            d = self.disciplinas[i]
          
          sessao = {d}
          tentativa = restante.difference(conflito[i])
          for s in range(len(self.disciplinas)):
            if self.disciplinas[s] in tentativa:
              if conflito[s].intersection(sessao) == emptySet:
                sessao.add(self.disciplinas[s])
          
          restante = restante.difference(sessao)
          self.horario.append(sessao)


def main():
    # Define os nomes dos arquivos de entrada; usa os defaults, se não houver
    # argumentos com os nomes na linha de comando.
    nomeArqDiscs = 'disciplinas.txt'
    nomeArqMatrics = 'matriculas.txt'
    if len(sys.argv) > 1:
        nomeArqDiscs = sys.argv[1]
    if len(sys.argv) > 2:
        nomeArqMatrics = sys.argv[2]
    
    # Cria uma instância da classe RegistroEscolar.
    res = RegistroEscolar(2020, 2)
    
    # Estabelece as disciplinas do período instanciado.
    res.set_disciplinas(nomeArqDiscs)
    
    # Estabelece as matrículas do período instanciado.
    res.set_matriculas(nomeArqMatrics)
    
    # Estabelece as sessões para o horário do período instanciado.
    res.set_horario()
    
    # Imprime as sessões possíveis para o horário do período instanciado.
    print('\nSessões para o período {:4d}/{:d}:'.format(res.periodo[0],\
          res.periodo[1]))
    for i in range(len(res.horario)):
        print('{:3d}: '.format(i), sorted(res.horario[i]))
    print()


if __name__ == '__main__':
    main()

