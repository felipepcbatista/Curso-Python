import math

num = int(input("Digite um número: "))
angulo_graus = float(input("Digite um angulo e veja seu seno, cosseno e tangente: "))

raiz_quadrada = math.sqrt(num)
fatorial = math.factorial(num)
angulo_rad = math.radians(angulo_graus)
seno = math.sin(angulo_rad)
cosseno = math.cos(angulo_rad)
tangente = math.tan(angulo_rad)

print(f"Raiz quadrada: {raiz_quadrada:.2f}\nFatorial: {fatorial}\nSeno: {seno:.2f}\nCosseno: {cosseno:.2f}\nTangente: {tangente:.2f}")