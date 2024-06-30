# Programa que genera matemáticamente la siguiente secuencia:  0, 0, 1, 3, 6, 10, 15, 21, ...

## Variables y Arrays
valores_secuencia = 8
secuencia = []

## Función generar la secuencia
def generarSecuencia(valores_secuencia, secuencia):
    for i in range(0, valores_secuencia):
        valor_sig = i * (i + 1) // 2
        if valor_sig == 0:
            secuencia.append(valor_sig)    
        secuencia.append(valor_sig)
    return secuencia

## Obtención de la secuencia
secuencia = generarSecuencia(valores_secuencia, secuencia)

## Imprimir secuencia. Para ejecutar en terminal: python ejercicio1.py
print(secuencia)