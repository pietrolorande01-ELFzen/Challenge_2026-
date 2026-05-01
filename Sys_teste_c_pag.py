# ==========================================================
# SPRINT 1 - SIMULADOR DE RECARGA INTELIGENTE
# CONDOMÍNIO + GOODWE + BATERIA LYNX
# ==========================================================

import time
import random

print("=" * 65)
print("      SISTEMA DE RECARGA CONDOMINIAL INTELIGENTE")
print("=" * 65)

# ----------------------------------------------------------
# FUNÇÕES DE VALIDAÇÃO
# ----------------------------------------------------------

def texto_obrigatorio(pergunta):
    while True:
        valor = input(pergunta).strip()

        if valor != "":
            return valor

        print("Entrada inválida. Digite novamente.\n")


def numero_positivo(pergunta):
    while True:
        try:
            valor = int(input(pergunta))

            if valor > 0:
                return valor

            print("Digite um número maior que zero.\n")

        except:
            print("Digite apenas números válidos.\n")


def hora_valida(pergunta):
    while True:
        try:
            valor = int(input(pergunta))

            if 0 <= valor <= 23:
                return valor

            print("Digite uma hora entre 0 e 23.\n")

        except:
            print("Digite apenas números válidos.\n")


def escolher_pagamento():
    while True:
        print("\nForma de pagamento:")
        print("1 - PIX")
        print("2 - BOLETO")
        print("3 - Adicionar no condomínio")

        opcao = input("Escolha: ")

        if opcao in ["1", "2", "3"]:
            return opcao

        print("Opção inválida.\n")


# ----------------------------------------------------------
# ENTRADAS
# ----------------------------------------------------------

nome = texto_obrigatorio("Nome do morador: ")
apartamento = numero_positivo("Número apartamento: ")
tempo = numero_positivo("Tempo de recarga (minutos): ")
hora = hora_valida("Hora atual (0 a 23): ")

pagamento = escolher_pagamento()

# ----------------------------------------------------------
# SIMULAÇÃO AUTOMÁTICA DA BATERIA LYNX
# usuário NÃO manipula
# ----------------------------------------------------------

bateria = random.randint(15, 100)

# ----------------------------------------------------------
# BANDEIRA TARIFÁRIA DA CIDADE
# ----------------------------------------------------------

bandeiras = ["Verde", "Amarela", "Vermelha"]
bandeira = random.choice(bandeiras)

taxa_bandeira = 0

if bandeira == "Verde":
    taxa_bandeira = 0.00

elif bandeira == "Amarela":
    taxa_bandeira = 0.20

else:
    taxa_bandeira = 0.45

# ----------------------------------------------------------
# TARIFA BASEADA NA BATERIA
# ----------------------------------------------------------

if bateria >= 70:
    tarifa = 0.85
    fonte = "Solar + Bateria Lynx"
    status = "ALTA RESERVA"

elif bateria >= 40:
    tarifa = 1.20
    fonte = "Bateria Parcial"
    status = "RESERVA MÉDIA"

else:
    tarifa = 1.60 + taxa_bandeira
    fonte = "Rede de Apoio"
    status = "BAIXA RESERVA"

# ----------------------------------------------------------
# DESCONTO MADRUGADA
# ----------------------------------------------------------

if hora >= 0 and hora < 6:
    tarifa -= 0.20

# Segurança
if tarifa < 0:
    tarifa = 0

# ----------------------------------------------------------
# SIMULAÇÃO DA RECARGA
# ----------------------------------------------------------

print("\nIniciando sessão de recarga...\n")

energia_total = 0

for minuto in range(1, tempo + 1):
    energia_total += 0.5
    print(f"Minuto {minuto:02d} | Energia acumulada: {energia_total:.1f} kWh")
    time.sleep(0.10)

# ----------------------------------------------------------
# CÁLCULO FINAL
# ----------------------------------------------------------

valor_total = energia_total * tarifa

# ----------------------------------------------------------
# GERAÇÃO PAGAMENTO
# ----------------------------------------------------------

detalhe_pagamento = ""

if pagamento == "1":
    chave_pix = random.randint(10000000000, 99999999999)
    detalhe_pagamento = f"PIX para conta do condomínio: {chave_pix}"

elif pagamento == "2":
    boleto = random.randint(10000000000000000000, 99999999999999999999)
    detalhe_pagamento = f"Código de boleto: {boleto}"

else:
    detalhe_pagamento = "Valor será lançado na próxima taxa condominial"

# ----------------------------------------------------------
# RELATÓRIO
# ----------------------------------------------------------

print("\n" + "=" * 65)
print("                 RELATÓRIO FINAL")
print("=" * 65)

print(f"Morador....................: {nome}")
print(f"Apartamento...............: {apartamento}")
print(f"Hora da sessão............: {hora}h")
print(f"Tempo total...............: {tempo} min")
print(f"Energia consumida.........: {energia_total:.2f} kWh")

print("\n--- SISTEMA ENERGÉTICO ---")
print(f"Bateria Lynx..............: {bateria}%")
print(f"Status....................: {status}")
print(f"Fonte usada...............: {fonte}")
print(f"Bandeira atual............: {bandeira}")

print("\n--- COBRANÇA ---")
print(f"Tarifa por kWh............: R$ {tarifa:.2f}")
print(f"Total a pagar.............: R$ {valor_total:.2f}")

print("\n--- PAGAMENTO ---")
print(detalhe_pagamento)

print("=" * 65)
print("Sessão encerrada com sucesso.")