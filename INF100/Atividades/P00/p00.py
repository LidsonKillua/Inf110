# Nome do aluno: Lídson Oliveira    
# Matrícula: 102961
# Data: 10/09/2020
# Esse programa desenha um labirinto baseado no número da matrícula,
# depois, de acordo com os comandos leva a tartaruga Tut até o tomate. 

import turtle as Tut
import p00_maze as m

############# Troque, na linha de baixo, o 0 pelo número de sua matrícula ### 
matricula = 102961   # <------------
############# Troque, na linha de cima, o 0 pelo número de sua matrícula  ### 

m.build_maze( Tut, matricula ) 

############################################
##  Adicione seu código abaixo desta linha
############################################
Tut.right(90)
Tut.fd(50)
Tut.left(90)
Tut.fd(100)

############################################
## Seu código não deve passar desta linha
############################################
Tut.screen().exitonclick()

