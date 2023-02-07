from scipy.interpolate import CubicSpline
import numpy as np
import matplotlib.pyplot as plt
import math
from numpy import diff 

x = [0, 0.8975979, 1.7951958, 2.692794, 3.5903916, 4.48798951, 5.3855874, 6.2831853]

y = [1, 0.52103, -0.15540, -0.52580, -0.43939, -0.09069, 0.21235, 0.28461]

f = CubicSpline(x, y, bc_type='natural')

x_new = np.linspace(0,7,7000) #gerando 7 mil pontos entre 0 e 7
y_new = f(x_new) #interpolando na funcao f

number3_index = 0
j = 0

for i in x_new: # achando o X mais proximo de 3
    if i >= 3:
        number3_index = j
        break
    j+=1

print("Questao 3, letra A, Parte 1")
print("X mais proximo do valor 3 : "+ str(x_new[number3_index]))
print("Valor da funcao interpolacao no X dado : " + str(y_new[number3_index]))
print("\n")

original_function_value = math.exp(-0.2 * (x_new[number3_index]))*math.cos(x_new[number3_index])

error_percentage = 100* (1-(original_function_value/y_new[number3_index]))

print("Questao 3, letra A, Parte 2")
print("Valor da funcao original no ponto x = 3 : " + str(original_function_value))
print("Erro percentual da interpolacao : " + str(error_percentage)+'%')
print("\n")

x_index_for_derivative = 0
j = 0

for i in x_new: # achando o X mais proximo de 3.59
    if i >= 3.59:
        x_index_for_derivative = j
        break
    j+=1

dydx = np.gradient(y_new,x_new)

print("Questao 3, letra B, Parte 1")
print("Valor de X mais proximo de x = 3.59 : " + str(x_new[x_index_for_derivative]))
print("Valor da Derivada no X dado na funcao interpolacao : " + str(dydx[x_index_for_derivative]))
print("Valor da Derivada em x = 3.5903916 na funcao original : " + str(-0.2*math.exp(-0.2 *3.5903916)*math.cos(3.5903916) - math.exp(-0.2 *3.5903916)*math.sin(3.5903916)))
print("\n")

d2ydx2 = np.gradient(dydx, x_new)

print("Questao 3, letra B, Parte 2")
print("Valor da Derivada Segunda no X dado na funcao interpolacao : " + str(d2ydx2[x_index_for_derivative]))
print("Valor da Derivada Segunda em x = 3.5903916 na funcao original : " + str(-0.96*math.exp(-0.2 *3.5903916)*math.cos(3.5903916) + 0.4*math.exp(-0.2 *3.5903916)*math.sin(3.5903916)))
print("\n")

original_function_value2 = math.exp(-0.2 * (x_new[x_index_for_derivative]))*math.cos(x_new[x_index_for_derivative])
error_percentage2 =  (1 -(y_new[x_index_for_derivative]/original_function_value2) )*100

print("Questao 3, letra B, Parte 3")
print("Valor da funcao interpolacao no X dado : " + str(y_new[x_index_for_derivative]))
print("Valor da funcao original no X dado : " + str(original_function_value2))
print("Erro Percentual : " + str(error_percentage2) + "%" )
print("O Erro Percentual quando x = 3.59 (" +str(error_percentage2)+ "%) e bem menor quando comparado ao erro percentual em x = 3 ("+str(error_percentage)+"%)")

end = input() # Se apenas abrir o programa python, será possível ler os prints
#plt.figure(figsize=(10,8))
#plt.plot(x_new, y_new, 'b')
#plt.plot(x,y,'ro')
#plt.xlabel('x')
#plt.ylabel('y')
#plt.show()

