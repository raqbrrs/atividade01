#Crie um programa que converta uma temperatura dada em Celsius para Fahrenheit usando a fórmula: F = C * 9/5 + 32.

C = float(input("Digite a temperatura em °C:"))
F = (9 * C / 5) + 32
print("%5.2f°C é igual a %5.2f°F" % (C, F)) 