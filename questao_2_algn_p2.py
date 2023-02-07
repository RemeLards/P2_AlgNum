import math as m

def aproximacao_simpson13(x0, x2, polinominal_power, constant = 1):

    i = 0
    valor_integral_aproximada = 0

    #Aplicando a Fórmula de Simpson

    while(i != n):

        x1 = (x0+x2)/2 #Calculando Ponto Médio

        integral_aproximada = hs13 * 1/3 * constant * ((m.pow(x0,polinominal_power)) + 4*(m.pow(x1,polinominal_power)) + m.pow(x2,polinominal_power))

        valor_integral_aproximada += integral_aproximada

        i += 1

        x0 = x2
        
        x2 = b * (i+1)
    
    return valor_integral_aproximada

def aproximacao_simpson38(x0, x3,polynomial_power, constant = 1):

    i = 0
    valor_integral_aproximada = 0

    #Aplicando a Fórmula de Simpson

    while(i != n):

        x1 = ((x3-x0)/3) + x0 #Calculando Ponto Médio 1
        x2 = (2 * (x3-x0)/3) + x0  #Calculando Ponto Médio 2

        integral_aproximada = hs38 * 3/8 * constant * (m.pow(x0,polynomial_power) + 3*( m.pow(x1,polynomial_power) + m.pow(x2,polynomial_power) )+ m.pow(x3,polynomial_power))

        valor_integral_aproximada += integral_aproximada

        i += 1

        x0 = x3
        
        x3 = b * (i+1)
    
    return valor_integral_aproximada

#Constantes

n = 4 #Número de partições, 4 inicialmente, começaremos com Simpson 1/3

a = 0 #Limite inferior escolhido

b = 1/n #Limite superior escolhido, dividido pelo número de partições/interações do método

hs38 = (b-a)/3 #Ponto médio da dos limites S38

hs13 = (b-a)/2 #Ponto médio da dos limites S13

#Como o problema é apenas polinominal, o código será simples 

valor_simpson_x3 = aproximacao_simpson13(a,b,3)
valor_simpson_x5 = aproximacao_simpson13(a,b,5)

print("Valor da Integral de Simpson 1/3, 4 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 1/3, 4 particoes : " + str( (1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" ) # O Valor da integral original é 1/12
#Portanto fs/(1/12) = 12 * fs
print("\n")

n = 8 # 8 partições Simpson 1/3
b = 1/n # Atualizando B
hs13 = (b-a)/2 # Atualizando ponto médio

valor_simpson_x3 = aproximacao_simpson13(a,b,3)
valor_simpson_x5 = aproximacao_simpson13(a,b,5)

print("Valor da Integral de Simpson 1/3, 8 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 1/3, 8 particoes : " + str( (1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" )
print("\n")

n = 10 # 10 partições Simpson 1/3
b = 1/n # Atualizando B
hs13 = (b-a)/2 # Atualizando ponto médio

valor_simpson_x3 = aproximacao_simpson13(a,b,3)
valor_simpson_x5 = aproximacao_simpson13(a,b,5)

print("Valor da Integral de Simpson 1/3, 10 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 1/3, 10 particoes : " + str( (1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" )
print("\n")

n = 4 # 4 partições Simpson 3/8
b = 1/n # Atualizando B
hs38 = (b-a)/3 # Atualizando ponto médio

valor_simpson_x3 = aproximacao_simpson38(a,b,3)
valor_simpson_x5 = aproximacao_simpson38(a,b,5)

print("Valor da Integral de Simpson 3/8, 4 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 3/8, 4 particoes : " + str( (1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" )
print("\n")

n = 8 # 8 partições Simpson 3/8
b = 1/n # Atualizando B
hs38 = (b-a)/3 # Atualizando ponto médio

valor_simpson_x3 = aproximacao_simpson38(a,b,3)
valor_simpson_x5 = aproximacao_simpson38(a,b,5)

print("Valor da Integral de Simpson 3/8, 8 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 3/8, 8 particoes : " + str((1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" )
print("\n")

n = 10 # 10 partições Simpson 3/8
b = 1/n # Atualizando B
hs38 = (b-a)/3 # Atualizando ponto médio 

valor_simpson_x3 = aproximacao_simpson38(a,b,3)
valor_simpson_x5 = aproximacao_simpson38(a,b,5)

print("Valor da Integral de Simpson 3/8, 10 particoes: " + str(valor_simpson_x3-valor_simpson_x5))
print("Erro Percentual Simpson 3/8, 10 particoes : " + str((1 - 12 * (valor_simpson_x3-valor_simpson_x5)) * 100)  + "%" )
print("\n")

end = input() # Se apenas abrir o programa python, será possível ler os prints
