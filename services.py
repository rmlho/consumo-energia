#Importando as classes do models.py para serem usadas aqui

from models import *

TARIFA = 0.67   #Valor real da tarifa usada na ENERGISA da Paraíba 

ALTO_CONSUMO = 2.0
BAIXO_CONSUMO = 0.5

lista_registros = []

def calcular_consumo(potencia_w, tempo_uso_horas):
    consumo_kWh = (potencia_w * tempo_uso_horas) / 1000
    return consumo_kWh

def calcular_custo(consumo_kWh):
    custo = consumo_kWh * TARIFA
    return custo

def classificar_consumo(consumo_kWh):
    if consumo_kWh >= ALTO_CONSUMO:
        return "ALTO"
    
    else :
        if consumo_kWh <= BAIXO_CONSUMO:
            return "BAIXO"
        
        else :
            return "MODERADO"
        
def adicionar_registro(nome, potencia_w, tempo_uso_horas):
    consumo_kWh_calculado = calcular_consumo(potencia_w, tempo_uso_horas)
    custo_calculado = calcular_custo(consumo_kWh_calculado)

    equipamento = criar_equipamento(nome, potencia_w, tempo_uso_horas)
    status_classificacao = classificar_consumo(consumo_kWh_calculado)
    novo_registro = criar_registro(equipamento, tempo_uso_horas, consumo_kWh_calculado, custo_calculado, status_classificacao)

    lista_registros.append(novo_registro)

    return novo_registro

def buscar_equipamento(nome):
    nome_formatado = formatar_nome(nome)

    for registro in lista_registros:
        if registro['equipamento']['nome'] == nome_formatado:
            return registro
 
    return None