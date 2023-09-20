import math

# Constantes físicas
massa_eletron = 9.109e-31  # kg
carga_eletron = 1.60e-19  # C
perm_vacuo = 8.854187817e-12    # F/m
constante_plank = 6.62607015e-34  # J*s
constante_velocidade_luz = 3e8  # m/s

def info():
    print("Programa que realiza cálculos relacionados ao modelo de Bohr para o átomo de hidrogênio para a matéria CF3121 - Tópicos de Optica e Física Moderna")
    print()
    print("Este programa procura realizar conversões entre diferentes unidades e calcular valores como:\n*frequência\n*comprimento de onda\n*número de onda\n*frequência angular\n*amplitude do campo elétrico\n*amplitude do campo magnético\n*intensidade")
    print()
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Mateus Rocha - RA: 22.222.022-2")
    print("Feito por: Leandro de Brito Alencar - RA: 22.222.034-5")
    print()
    print("***************************************************************",)
    
def menu():
    print("Escolha uma opção:")
    print("\t1. Calcular raio da órbita, velocidade, energia cinética, energia potencial e energia total para um valor de n.")
    print("\t2. Sair do programa")
    print()

def calculo_Bohr(n):
    # Cálculo do raio da órbita
    raio_orbita = (4 * math.pi * perm_vacuo * (n ** 2) * (constante_plank ** 2)) / (massa_eletron * (carga_eletron ** 2))

    # Cálculo da velocidade do elétron
    velocidade = (carga_eletron ** 2) / (4 * math.pi * perm_vacuo * raio_orbita * massa_eletron)

    # Cálculo da energia cinética
    energia_cinetica = (1 / 2) * massa_eletron * (velocidade ** 2)

    # Cálculo da energia potencial
    energia_potencial = -(carga_eletron ** 2) / (4 * math.pi * perm_vacuo * raio_orbita)

    # Cálculo da energia total
    energia_total = energia_cinetica + energia_potencial
    print(f"\nResultados para n = {n:.3e}: ")
    print(f"Raio da órbita: {raio_orbita:.3e} m")
    print(f"Velocidade do elétron: {velocidade:.3e} m/s")
    print(f"Energia Cinética: {energia_cinetica:.3e} J")
    print(f"Energia Potencial: {energia_potencial:.3e} J")
    print(f"Energia Total: {energia_total:.3e} J")

 
def main():
    info()
    while True:
        menu()
        e = int(input("\tDigite o número desejado: "))
        if e ==1:
            n = int(input("Digite o nível quantico: "))
            calculo_Bohr(n)
        elif e == 2:
            print("Saindo do programa: ")
            break
        else:
            print("Opção inválida, por favor selecione novamente.")
            
if __name__=="__main__":
    main()