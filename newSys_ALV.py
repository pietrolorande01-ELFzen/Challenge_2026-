# ==========================================================
# TOTEM DE RECARGA INTELIGENTE (VALIDAÇÃO COMPLETA)
# ==========================================================

import time
import random
from datetime import datetime, timedelta

print("=" * 65)
print("        TOTEM DE RECARGA INTELIGENTE")
print("=" * 65)

# ----------------------------------------------------------
# FUNÇÕES DE VALIDAÇÃO
# ----------------------------------------------------------

def texto_obrigatorio(msg):
    while True:
        valor = input(msg).strip()
        if valor != "":
            return valor
        print("Entrada inválida. Não pode ser vazio.\n")


def numero_positivo(msg):
    while True:
        try:
            valor = int(input(msg))
            if valor > 0:
                return valor
            print("Digite um número maior que zero.\n")
        except:
            print("Digite apenas números inteiros.\n")


def token_valido():
    while True:
        token = input("Digite seu token (6 dígitos): ").strip()

        if token.isdigit() and len(token) == 6:
            return token

        print("Token inválido. Deve conter exatamente 6 números.\n")


def sim_ou_nao(msg):
    while True:
        valor = input(msg).strip().lower()

        if valor in ["s", "n"]:
            return valor

        print("Digite apenas 's' ou 'n'.\n")


def escolher_pagamento():
    while True:
        print("\nForma de pagamento:")
        print("1 - PIX (Governo)")
        print("2 - BOLETO")
        print("3 - TAG (Sem Parar)")
        print("4 - Cartão (Aproximação)")

        op = input("Escolha: ").strip()

        if op in ["1", "2", "3", "4"]:
            return op

        print("Opção inválida. Escolha de 1 a 4.\n")


# ----------------------------------------------------------
# ENTRADAS
# ----------------------------------------------------------

nome = texto_obrigatorio("Nome do usuário: ")
token = token_valido()

inicio = datetime.now()
print(f"\nHorário de início: {inicio.strftime('%H:%M')}")

# ----------------------------------------------------------
# SIMULAÇÃO DO CARRO
# ----------------------------------------------------------

print("\nConectando ao veículo...")
time.sleep(2)

marcas = ["BYD", "Tesla", "Volvo", "BMW", "Renault"]
marca_carro = random.choice(marcas)

bateria_inicial = random.randint(10, 80)
capacidade_total = 100

energia_necessaria = capacidade_total - bateria_inicial
tempo_sugerido = int(energia_necessaria / 0.5)

print("\n--- VEÍCULO DETECTADO ---")
print(f"Marca: {marca_carro}")
print(f"Bateria atual: {bateria_inicial}%")
print(f"Tempo sugerido: {tempo_sugerido} minutos")

escolha = sim_ou_nao("\nAceitar sugestão? (s/n): ")

if escolha == "s":
    tempo = tempo_sugerido
else:
    tempo = numero_positivo("Digite o tempo desejado (minutos): ")

# ----------------------------------------------------------
# SISTEMA ENERGÉTICO (BATERIA LYNX)
# ----------------------------------------------------------

bateria_lynx = random.randint(15, 100)

bandeiras = ["Verde", "Amarela", "Vermelha"]
bandeira = random.choice(bandeiras)

if bandeira == "Verde":
    taxa_bandeira = 0
elif bandeira == "Amarela":
    taxa_bandeira = 0.20
else:
    taxa_bandeira = 0.45

if bateria_lynx >= 70:
    tarifa = 0.85
    fonte = "Solar + Bateria Lynx"
elif bateria_lynx >= 40:
    tarifa = 1.20
    fonte = "Bateria Parcial"
else:
    tarifa = 1.60 + taxa_bandeira
    fonte = "Rede de Apoio"

hora = inicio.hour
if 0 <= hora < 6:
    tarifa -= 0.20

if tarifa < 0:
    tarifa = 0

taxa_fixa = 15

# ----------------------------------------------------------
# PAGAMENTO
# ----------------------------------------------------------

pagamento = escolher_pagamento()

print("\nProcessando pagamento...")
time.sleep(3)

if pagamento == "1":
    print("Gerando PIX para o governo...")
    time.sleep(4)
    print("Pagamento confirmado via PIX.")

elif pagamento == "2":
    print("Gerando boleto...")
    time.sleep(5)
    print("Pagamento confirmado via boleto.")

elif pagamento == "3":
    print("Lendo TAG...")
    time.sleep(4)
    print("Pagamento aprovado.")

else:
    print("Aproxime o cartão...")
    time.sleep(4)
    print("Pagamento aprovado.")

# ----------------------------------------------------------
# RECARGA
# ----------------------------------------------------------

print("\nIniciando recarga...\n")

energia_total = 0
tempo_atual = inicio

for minuto in range(1, tempo + 1):
    energia_total += 0.5
    tempo_atual += timedelta(minutes=1)

    print(f"{tempo_atual.strftime('%H:%M')} | {energia_total:.1f} kWh")

    time.sleep(0.05)

fim = tempo_atual

bateria_final = min(100, bateria_inicial + (energia_total / capacidade_total * 100))

# ----------------------------------------------------------
# VALORES
# ----------------------------------------------------------

valor_energia = energia_total * tarifa
valor_total = valor_energia + taxa_fixa

# ----------------------------------------------------------
# RELATÓRIO FINAL
# ----------------------------------------------------------

print("\n" + "=" * 65)
print("                RELATÓRIO FINAL")
print("=" * 65)

print(f"Usuário...............: {nome}")
print(f"Token.................: {token}")

print("\n--- TEMPO ---")
print(f"Início................: {inicio.strftime('%H:%M')}")
print(f"Fim...................: {fim.strftime('%H:%M')}")
print(f"Duração...............: {tempo} min")

print("\n--- VEÍCULO ---")
print(f"Marca.................: {marca_carro}")
print(f"Bateria inicial.......: {bateria_inicial}%")
print(f"Bateria final.........: {bateria_final:.1f}%")

print("\n--- ENERGIA ---")
print(f"Bateria Lynx..........: {bateria_lynx}%")
print(f"Fonte.................: {fonte}")
print(f"Bandeira..............: {bandeira}")

print("\n--- COBRANÇA ---")
print(f"Valor energia.........: R$ {valor_energia:.2f}")
print(f"Taxa fixa.............: R$ {taxa_fixa:.2f}")
print(f"TOTAL.................: R$ {valor_total:.2f}")

print("=" * 65)
print("Sessão finalizada com sucesso.")
print("\nDesenvolvido por FIAP / GoodWe")