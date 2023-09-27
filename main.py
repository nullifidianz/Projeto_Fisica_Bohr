import math

# Constantes físicas
massa_eletron = 9.109e-31  # kg
carga_eletron = 1.60e-19  # C
perm_vacuo = 8.854187817e-12  # F/m
constante_plank_eV = 4.13566743e-15  # eV
constante_plank = 6.62607015e-34  # J*s
constante_velocidade_luz = 3e8  # m/s


def info():
    print(
        "Programa que realiza cálculos relacionados ao modelo de Bohr para o átomo de hidrogênio para a matéria "
        "CF3121 - Tópicos de Optica e Física Moderna")

    print()
    print(
        "Este programa procura realizar conversões entre diferentes unidades e calcular valores como: raio da órbita, "
        "velocidade, energia cinética, energia potencial e energia total para um valor de n.")
    print()
    print(
        "O modelo de Bohr para o átomo de hidrogênio é uma teoria que descreve a estrutura simplificada desse átomo, "
        "levando em consideração a ideia de órbitas eletrônicas quantizadas. Ele introduz o conceito de números "
        "quânticos para descrever o nível de energia das órbitas e permite calcular propriedades como raio da órbita, "
        "velocidade do elétron e energias cinética e potencial. Este modelo foi um avanço importante na compreensão "
        "da estrutura atômica e serviu como base para desenvolvimentos posteriores na teoria quântica.")
    print("Feito por: João Paulo Paggi Zuanon Dias - RA: 22.222.058-4")
    print("Feito por: Mateus Rocha - RA: 22.222.022-2")
    print("Feito por: Leandro de Brito Alencar - RA: 22.222.034-5")
    print()
    print("***************************************************************")


def menu():
    print("Escolha uma opção:")
    print(
        "\t1. Calcular raio da órbita, velocidade, energia cinética, energia potencial e energia total para um valor "
        "de n.")
    print("\t2. Conversor de medias")
    print("\t3. Calcular energia do foton")
    print("\t4. Sair do Programa")


def menu2():
    print("Escolha uma opção de conversão:")
    print("\t1. m para nm")
    print("\t2. J para ev")
    print("\t3. THz para Hz")


def menu3():
    print("Escolha entre absorção, emissão ou foton de hidrogenio:")
    print("\t1. absorção")
    print("\t2. emissão")
    print("\t3. hidrogenio")


def calculo_bohr(n):
    # Cálculo do raio da órbita
    raio_orbita = ((n ** 2) * 5.29e-11)

    # Cálculo da velocidade do elétron
    velocidade = (2.187e6 / n)

    # Cálculo da energia cinética
    energia_cinetica = (13.6 / (n ** 2))

    # Cálculo da energia potencial
    energia_potencial = -(27.2 / (n ** 2))

    # Cálculo da energia total
    energia_total = -(13.6 / (n ** 2))

    # Cálculo do comprimento de onda
    comprimento_onda = (constante_plank / (massa_eletron * velocidade))
    # Saída com resultados
    print(f"\nResultados para n = {n:.3e}: ")
    print(f"Raio da órbita: {raio_orbita:.3e} m")
    print(f"Velocidade do elétron: {velocidade:.3e} m/s")
    print(f"Energia Cinética: {energia_cinetica:.3e} eV")
    print(f"Energia Potencial: {energia_potencial:.3e} eV")
    print(f"Energia Total: {energia_total:.3e} eV")
    print(f"Comprimento de onda: {comprimento_onda:.3e} m")


def calculo_energia_foton_absorvido(n_inicial, n_final):
    energia_inicial = (-13.6 / n_inicial ** 2)
    energia_final = (-13.6 / n_final ** 2)
    energia_absorvida = (energia_final - energia_inicial)
    lambda_absorvido = (constante_velocidade_luz * constante_plank_eV / energia_absorvida)
    freq_foton = (constante_velocidade_luz / lambda_absorvido)
    print(f"Resultados para n{n_inicial} e n{n_final}: ")
    print(f"Energia do fóton absorvido: {energia_absorvida:.3e} eV")
    print(f"Comprimento de onda do fóton absorvido: {lambda_absorvido:.3e} metros")
    print(f"Frequência do fóton absorvido: {freq_foton:.3e} Hz")


def calculo_energia_foton_emitido(n_inicial, n_final):
    energia_inicial = (-13.6 / n_inicial ** 2)
    energia_final = (-13.6 / n_final ** 2)
    energia_emitida = (energia_inicial - energia_final)
    lambda_emitido = (constante_velocidade_luz * constante_plank_eV / energia_emitida)
    freq_foton = (constante_velocidade_luz / lambda_emitido)
    print(f"Resultados para n{n_inicial} e n{n_final}: ")
    print(f"Energia do fóton emitido: {energia_emitida:.3e} eV")
    print(f"Comprimento de onda do fóton emitido: {lambda_emitido:.3e} metros")
    print(f"Frequência do fóton emitido: {freq_foton:.3e} Hz")
    
    
def calculo_energia_atomo_hidrogenio(n_inicial, frequencia_hz):
  energia_inicial = (-13.6 / n_inicial ** 2)
  energia_inicial_J = energia_inicial * 1.60218e-19
  energia_foton = (constante_plank * frequencia_hz)
  energia_final = energia_inicial_J + energia_foton
  n = (-13.6 / (energia_final / 1.60218e-19))**0.5
  nf = round(n)
  print(f"O valor de nf é: {nf}")

def calculo_energia_atomo_hidrogenio_2(n_inicial, comprimento_onda):
  energia_inicial = (-13.6 / n_inicial ** 2)
  energia_inicial_J = energia_inicial * 1.60218e-19
  energia_foton = ((constante_plank * constante_velocidade_luz)/comprimento_onda)
  energia_final = energia_inicial_J + energia_foton
  n = (-13.6 / (energia_final / 1.60218e-19))**0.5
  nf = round(n)
  print(f"O valor de nf é: {nf}")  


# Conversor de m para nm    
def conversor1(n2):
    nm = (n2 * 1e9)
    print(f"{n2:.3e} metros equivalem a {nm:.3e} nanômetros")
    print()


# Conversor de J para eV
def conversor2(n2):
    ev = (n2 * 6.242e18)
    print(f"{n2:.3e} Joules equivalem a {ev:.3e} eletronvolts (eV)")
    print()

def conversor3(n2):
    Hz = (n2*1e12)
    print(f"{n2:.3e} THz equivalem a {Hz:.3e} Hz")
    print()

def main():
    info()
    while True:
        menu()
        e = int(input())
        if e == 1:
            n = int(input("Digite o nível quantico: "))
            calculo_bohr(n)
        elif e == 2:
            menu2()
            e2 = int(input())
            if e2 == 1:
                n2 = float(input("Digite o valor que você gostaria de converter: "))
                conversor1(n2)
            elif e2 == 2:
                n2 = float(input("Digite o valor que você gostaria de converter: "))
                conversor2(n2)
            elif e2==3:
                n2 = float(input("digite o valor que você gostaria de converter: "))
                conversor3(n2)
            else:
                print("Opção inválida por favor digite novamente")
        elif e == 3:
            menu3()
            e3 = int(input())
            if e3 == 1:
                n_inicial = int(input("Digite o valor de n inicial: "))
                n_final = int(input("Digite o valor de n final: "))
                calculo_energia_foton_absorvido(n_inicial, n_final)
            elif e3 == 2:
                n_inicial = int(input("Digite o valor de n inicial: "))
                n_final = int(input("Digite o valor de n final: "))
                calculo_energia_foton_emitido(n_inicial, n_final)
            
            elif e3 == 3:
              print("Você deseja calcular a partir de: ")
              print("1. Frequência")
              print("2. Comprimento de onda")
              e4= int(input())
            if e4==1:  
                n_inicial = int(input("Digite o valor de n inicial: "))
                frequencia = (float(input("Digite o valor da frequencia em hz: ")))
                calculo_energia_atomo_hidrogenio(n_inicial, frequencia)
            elif e4==2:
                n_inicial = int(input("Digite o valor de n inicial: "))
                comprimento_onda = (float(input("Digite o valor do Comprimento de onda em m: ")))
                calculo_energia_atomo_hidrogenio_2(n_inicial, comprimento_onda)
            else:
                print("Opção inválida por favor digite novamente")

        elif e == 4:
            print("Saindo do programa")
            break
        else:
            print("Opção inválida, por favor selecione novamente.")


if __name__ == "__main__":
    main()
