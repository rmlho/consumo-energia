#As funções criar_equipamento e criar_registro são os dicionarios do que vai ser pedido no main.py, o main é feito por ultimo depois de terminar tudo
#Usem os mesmo nomes das variáveis usadas aqui, tudo ja ta importado para os outros documentos então não vai da erro se usarem

def criar_equipamento(nome, potencia_w, tempo_uso_horas):
    equipamento = {
        'nome': nome,
        'potencia_w': potencia_w,
        'tempo_uso_horas': tempo_uso_horas
    }
    return equipamento


def criar_registro(equipamento, tempo_uso_horas, consumo_kWh, custo, classificacao):
    registro = {
        'equipamento': equipamento,
        'tempo_uso_horas': tempo_uso_horas,
        'consumo_kWh': consumo_kWh,
        'custo': custo,
        'classificacao': classificacao
    }
    return registro

#Esse bloco vai ser usado apenas para válidar os textos e valores

def validar_texto(texto):
    if not texto:
        return False
    else :
        return True
    

def validar_numero_positivo(numero):
    if numero > 0:
        return True
    else :
        return False
    

def validar_faixa(numero, minimo, maximo):
    if minimo <= numero <= maximo:
        return True
    else :
        return False
    

def formatar_nome(nome):
    nome = nome.strip()
    nome = nome.capitalize()
    return nome

def equipamento_para_string(equipamento):
    texto = f"{equipamento['nome']} | {equipamento['potencia_w']}W | {equipamento['tempo_uso_horas']}h" 
    return texto
    
#E essa função caso o usuário digite um valor em horas nada faz, mas se digita em minutos converte em horas
#Um exemplo de como ficaria a variavel: tempo_uso_horas = converter_minutos(30, 'min'), trazendo a função

def converter_minutos(valor, unidade):
    if unidade == 'h':
        return valor
    else :
        if unidade == 'min':
            valor = valor / 60
            return valor
    return None

#Todo o Models.py está pronto, tentem seguir a lógica desse documento nos services, tudo que vcs fizerem tem que ser uma função
#Assim como o models, lembrem que vcs vao usar essas funções em services para criar os calculos, nao todos mas alguns