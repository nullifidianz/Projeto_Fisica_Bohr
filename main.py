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
    print("Este programa procura realizar conversões entre diferentes unidades e calcular valores como: raio da órbita, velocidade, energia cinética, energia potencial e energia total para um valor de n.")
    print()
    print("O modelo de Bohr para o átomo de hidrogênio é uma teoria que descreve a estrutura simplificada desse átomo, levando em consideração a ideia de órbitas eletrônicas quantizadas. Ele introduz o conceito de números quânticos para descrever o nível de energia das órbitas e permite calcular propriedades como raio da órbita, velocidade do elétron e energias cinética e potencial. Este modelo foi um avanço importante na compreensão da estrutura atômica e serviu como base para desenvolvimentos posteriores na teoria quântica.")
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Mateus Rocha - RA: 22.222.022-2")
    print("Feito por: Leandro de Brito Alencar - RA: 22.222.034-5")
    print()
    print("***************************************************************",)
    
def menu():
    print("Escolha uma opção:")
    print("\t1. Calcular raio da órbita, velocidade, energia cinética, energia potencial e energia total para um valor de n.")
    print("\t2. Conversor de medias")
    print("\t3. Sair do Programa")
    
def menu2():
    print("Escolha uma opção de conversão:")
    print("\t1. m para nm")
    print("\t2. J para ev")

def calculo_Bohr(n):
    # Cálculo do raio da órbita
    raio_orbita = ((n**2)*5.29e-11)

    # Cálculo da velocidade do elétron
    velocidade = (2.187e6/n)

    # Cálculo da energia cinética
    energia_cinetica = (13.6/(n**2))

    # Cálculo da energia potencial
    energia_potencial = -(27.2/(n**2))

    # Cálculo da energia total
    energia_total = -(13.6/(n**2))
    
    # Cálculo do comprimento de onda
    comprimento_onda = (constante_plank/(massa_eletron*velocidade))
    
    # Saída com resultados
    print(f"\nResultados para n = {n:.3e}: ")
    print(f"Raio da órbita: {raio_orbita:.3e} m")
    print(f"Velocidade do elétron: {velocidade:.3e} m/s")
    print(f"Energia Cinética: {energia_cinetica:.3e} J")
    print(f"Energia Potencial: {energia_potencial:.3e} J")
    print(f"Energia Total: {energia_total:.3e} J")
    print(f"Comprimento de onda: {comprimento_onda:.3e} m")

# Conversor de m para nm    
def conversor1(n2):
    nm = n2*1e9
    print(f"{n2:.3e} metros equivalem a {nm:.3e} nanômetros")
    print()

# Conversor de J para eV
def conversor2(n2):
    ev=n2*6.242e12
    print(f"{n2:.3e} Joules equivalem a {ev:.3e} eletronvolts (eV)")
    print()
    
def main():
    info()
    while True:
        menu()
        e = int(input())
        if e ==1:
            n = int(input("Digite o nível quantico: "))
            calculo_Bohr(n)
        elif e ==3:
            print("Saindo do programa: ")
            break
        elif e ==2:
            menu2()
            e2 = int(input())
            if e2==1:
                n2 = float(input("Digite o valor que você gostaria de converter: "))
                conversor1(n2)
            elif e2==2:
                n2 = float(input("Digite o valor que você gostaria de converter: "))
                conversor2(n2)
            else:
                print("Opção inválida por favor digite novamente")
        else:
            print("Opção inválida, por favor selecione novamente.")
            
if __name__=="__main__":
    main()
