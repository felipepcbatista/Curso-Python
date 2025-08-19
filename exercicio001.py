print("==== CALCULADORA DE IMC ====")
peso = float(input("Informe o seu peso (kg): "))
altura = float(input("Informe a sua altura (m): "))
imc = peso / (altura ** 2)
peso_ideal = altura ** 2 * 24.9

if imc < 18.5: 
    print(f"IMC: {imc:.2f} - Abaixo do peso.")
elif imc < 24.9: 
    print(f"IMC: {imc:.2f} - Peso normal.")
elif imc < 29.9: 
    print(f"IMC: {imc:.2f} - Sobrepeso.")
else: 
    print (f"IMC: {imc:.2f} - Obesidade.")

if peso > peso_ideal: 
    print(f"Você precisa perder {(peso-peso_ideal):.2f}kg para atingir o peso ideal ({peso_ideal:.2f}kg).")
elif peso < peso_ideal: 
    print(f"Você precisa ganhar {(peso_ideal-peso):.2f}kg para atingir o peso ideal ({peso_ideal:.2f}kg).")
else: 
    print (f"Parabéns! Você está no peso ideal ({peso_ideal:.2f}kg).")