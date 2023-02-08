from scipy.optimize import fsolve
from numpy import exp
import numpy as np
import math

def question_exp_func_value(x): # valor da funcao exponencial da função
    return (9.06869*math.exp(-2.03263*x))

def question_linear_func_value(x): #valor da funcao linear da função
    return (8.0283*x + 2.0199)

def question_quadratic_func_value(x): #valor da funcao linear da função
    return (2.0036*x**2 + 0.8552*x + 4.0748)

f1 = lambda x: 2.0036*x**2 + 0.8552*x + 4.0748 - 8.0283*x - 2.0199 # funcao ponto de encontro da funcao linear com a quadrática

f2 = lambda x: 8.0283*x + 2.0199 - 9.06869*math.exp(-2.03263*x) # funcao ponto de encontro da funcao linear com a exponencial

f3 = lambda x: 2.0036*x**2 + 0.8552*x + 4.0748 - 9.06869*math.exp(-2.03263*x) # funcao ponto de encontro exponencial com a quadrática

f1_sol = fsolve(f1,[0.3]) #solucao de f1
f2_sol = fsolve(f2,[0.33]) #solucao de f2
f3_sol = fsolve(f3,[0.35]) #solucao de f3

print("\n")
print("solucao f1 = " + str(f1_sol))
print("\n")
print("solucao f2 = " + str(f2_sol))
print("\n")
print("solucao f3 = " + str(f3_sol))
print("\n")

x_vector= np.linspace(0.3,0.4,7000) #gerando 7 mil pontos entre 0.3 e 0.4

f1_value = 8.0283*f1_sol[0] + 2.0199 #valor de y1
f2_value = 8.0283*f2_sol[0] + 2.0199 #valor de y2
f3_value = 2.0036*f3_sol[0]**2 + 0.8552*f3_sol[0] + 4.0748 #valor de y3

x1_shortest_dist = 0
x2_shortest_dist = 0
x3_shortest_dist = 0

#distancia da funcao exponencial
shortest_euclidian_dist = 0
for i in x_vector:
    
    euclidian_dist = math.sqrt((f1_value-question_exp_func_value(i))**2 + (f1_sol - i)**2)
    
    if shortest_euclidian_dist == 0:
        shortest_euclidian_dist = euclidian_dist
        x1_shortest_dist = i

    if euclidian_dist < shortest_euclidian_dist:
        shortest_euclidian_dist = euclidian_dist
        x1_shortest_dist = i

print("\n")
print("X da menor distancia da funcao exponencial em relacao a f1 = " + str(x1_shortest_dist) )
print("Menor distancia da funcao exponencial em relacao a f1 = " + str(shortest_euclidian_dist))
print("\n")

#distancia da funcao quadratica
shortest_euclidian_dist = 0
for i in x_vector:
    
    euclidian_dist = math.sqrt((f2_value-question_quadratic_func_value(i))**2 + (f2_sol - i)**2)
    
    if shortest_euclidian_dist == 0:
        shortest_euclidian_dist = euclidian_dist
        x2_shortest_dist = i

    if euclidian_dist < shortest_euclidian_dist:
        shortest_euclidian_dist = euclidian_dist
        x2_shortest_dist = i

print("\n")
print("X da menor distancia da funcao quadratica em relacao a f2 = " + str(x2_shortest_dist))
print("Menor distancia da funcao quadratica em relacao a f2 = " + str(shortest_euclidian_dist))
print("\n")

#distancia da funcao linear
shortest_euclidian_dist = 0
for i in x_vector:
    
    euclidian_dist = math.sqrt((f3_value-question_linear_func_value(i))**2 + (f3_sol - i)**2)
    
    if shortest_euclidian_dist == 0:
        shortest_euclidian_dist = euclidian_dist
        x3_shortest_dist = i

    if euclidian_dist < shortest_euclidian_dist:
        shortest_euclidian_dist = euclidian_dist
        x3_shortest_dist = i

print("\n")
print("X da menor distancia da funcao linear em relacao a f3 = " + str(x3_shortest_dist))
print("Menor distancia da funcao linear em relacao a f3 = " + str(shortest_euclidian_dist))

end = input() #caso execute o codigo python direto, para aparecer os resultados antes de apertar enter e fechar




