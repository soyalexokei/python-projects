# Programa que genera matemáticamente la siguiente secuencia:  0, 0, 1, 3, 6, 10, 15, 21, ...
# Y al introducir un primer parámetro se muestra desde su nº más cercano.
# Y al introducir un segundo parámetro se muestra hasta su nº más cercano.

## Variables y Arrays
secuencia = []
param1 = 10
param2 = 100

## Función para encontrar el valor más cercano
def encontrarValorCercano(secuencia, valor):
    return min(secuencia, key=lambda x: abs(x - valor))

## Función generar secuencia
def generarSecuencia(secuencia, param):
    for i in range(param):
        valor_sig = i * (i + 1) // 2
        if valor_sig == 0:
            secuencia.append(valor_sig)    
        secuencia.append(valor_sig)
    return secuencia

## Función para generar la secuencia entre los valores cercanos de los valores de entrada
def generarSecReal(secuencia, param1, param2):
    secuencia = generarSecuencia(secuencia, param2)
    num1 = encontrarValorCercano(secuencia, param1)
    num2 = encontrarValorCercano(secuencia, param2)
    inicio = secuencia.index(num1)
    fin = secuencia.index(num2)
    return secuencia[inicio:fin]

## Obtención de la secuencia
secuencia = generarSecReal(secuencia, param1, param2)

## Imprimir secuencia. Para ejecutar en terminal: python ejercicio2.py
print(secuencia)