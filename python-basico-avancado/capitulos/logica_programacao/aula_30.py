"""
CONSTANTE = "Variáveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

VELOCIDADE = 61  # velocidade atual do carro
LOCAL_CARRO = 100  # local em que o carro está na estrada

RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

VEL_CARRO_PASSOU_RADAR_1 = VELOCIDADE > RADAR_1
INTERVALO_INICIAL = LOCAL_CARRO >= (LOCAL_1 - RADAR_RANGE)
INTERVALO_FINAL = LOCAL_CARRO <= (LOCAL_1 + RADAR_RANGE)
CARRO_PASSOU_RADAR_1 = INTERVALO_INICIAL and INTERVALO_FINAL
CARRO_MULTADO_RADAR_1 = CARRO_PASSOU_RADAR_1 and VEL_CARRO_PASSOU_RADAR_1

if VEL_CARRO_PASSOU_RADAR_1:
    print("Velocidade carro passou do radar 1")

if CARRO_PASSOU_RADAR_1:
    print("Carro passou radar 1")

if CARRO_MULTADO_RADAR_1:
    print("carro multado em radar 1")
