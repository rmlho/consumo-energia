#Importanto as classes do services.py e do models.py para serem usadas aqui

from services import *
from models import *

from rich.console import Console
from rich.panel import Panel
from rich.table import Table

console = Console()

def exibir_menu():
    console.print(Panel(":light_bulb: [bold blue]CONSUMO DE ENERGIA DOMÉSTICA[/] ||\n[dim green]:zap:Tarifa Energisa PB: R$ 0,67/kWh[/]",title="MENU", style="bold cyan"))
    console.print()
    console.print("[blue]>> Selecione uma opção:[/]")
    console.print("[blue][1][/] Cadastrar equipamento")
    console.print("[blue][2][/] Registrar uso")
    console.print("[blue][3][/] Listar equipamentos")
    console.print("[blue][4][/] Ver ranking de consumo")
    console.print("[blue][5][/] Gerar relatório")
    console.print("[red][0] sair[/]")
    console.print()

def iniciar_sistema():
    rodando = True

    while rodando:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            console.print(":cross_mark: Valor inválido, digite um número")
            continue

        if opcao == 1:
            menu_cadastrar_equipamento()

        else :
            if opcao == 2:
                menu_registrar_uso()

            else :
                if opcao == 3:
                    listar_equipamentos(lista_registros)

                else :
                    if opcao == 4:
                        ranking = gerar_ranking(lista_registros)
                        for i, r in enumerate(ranking):
                            console.print(f"[bold]{i+1}. {r['equipamento']['nome']} - {r['consumo_kWh']} kWh[/]")

                    else :
                        if opcao == 5:
                            mostrar_relatorio()

                        else :
                            if opcao == 0:
                                console.print("[bold red]SAINDO[/]")
                                rodando = False

                            else :
                                console.print(":cross_mark: Opção inválida")

def exibir_mensagem(texto, type="info"):
    if type == "sucesso":
        console.print(f":white_check_mark: [bold green]{texto}[/]")

    else :
        if type == "erro":
            console.print(f":cross_mark: [bold red]{texto}[/]")

        else :
            console.print(f":orange_circle: [bold yellow]{texto}[/]")

def menu_cadastrar_equipamento():
    console.print("\n[bold blue] - CADASTRAR O EQUIPAMENTO -[/]")

    nome = input("Nome do equipamento: ")
    if not validar_texto(nome):
        exibir_mensagem("Nome inválido.", "erro")
        return

    try:
        potencia_w = float(input("Potência do equipamento (W): "))
        if not validar_numero_positivo(potencia_w):
            exibir_mensagem("Potência deve ser maior que zero.", "erro")
            return
    except ValueError:
        exibir_mensagem("Valor inválido para potência.", "erro")
        return

    try:
        unidade = input("Informe a unidade do tempo de uso (h/min): ").strip().lower()
        tempo_valor = float(input("Tempo de uso: "))
        tempo_uso_horas = converter_minutos(tempo_valor, unidade)

        if tempo_uso_horas is None:
            exibir_mensagem("Unidade inválida. Use 'h' ou 'min'.", "erro")
            return
        if not validar_numero_positivo(tempo_uso_horas):
            exibir_mensagem("Tempo deve ser maior que zero.", "erro")
            return
    except ValueError:
        exibir_mensagem("Valor inválido para tempo.", "erro")
        return

    novo_registro = adicionar_registro(nome, potencia_w, tempo_uso_horas)
    exibir_mensagem(f"Equipamento {novo_registro['equipamento']['nome']} cadastrado com sucesso!", "sucesso")

def menu_registrar_uso():
    console.print("\n[bold blue] - REGISTRAR USO -[/]")

    nome = input("Nome do equipamento já cadastrado: ")
    registro_existente = buscar_equipamento(nome)

    if registro_existente is None:
        exibir_mensagem("Equipamento não encontrado.", "erro")
        return

    try:
        unidade = input("Informe a unidade do tempo de uso (h/min): ").strip().lower()
        tempo_valor = float(input("Tempo de uso: "))
        tempo_uso_horas = converter_minutos(tempo_valor, unidade)

        if tempo_uso_horas is None:
            exibir_mensagem("Unidade inválida. Use 'h' ou 'min'.", "erro")
            return
        if not validar_numero_positivo(tempo_uso_horas):
            exibir_mensagem("Tempo deve ser maior que zero.", "erro")
            return
    except ValueError:
        exibir_mensagem("Valor inválido para tempo.", "erro")
        return

    equipamento = registro_existente['equipamento']
    novo_registro = adicionar_registro(equipamento['nome'], equipamento['potencia_w'], tempo_uso_horas)

    exibir_mensagem(
        f"Uso registrado! Consumo: {novo_registro['consumo_kWh']:.3f} kWh | "
        f"Custo: R${novo_registro['custo']:.2f} | "
        f"Classificação: {novo_registro['classificacao']}",
        "sucesso"
    )


def mostrar_relatorio():
    console.print()
    console.print(Panel("[bold blue]Relatório final[/]", style="bold cyan"))

    if not lista_registros:
        exibir_mensagem("Nenhum registro encontrado.", "erro")
        return

    ranking = gerar_ranking(lista_registros)
    maior_consumo = equipamento_mais_consumiu(ranking)

    resumo = Table(show_header=False, box=None)
    resumo.add_row("[bold cyan]Total de registros:[/]", str(len(lista_registros)))
    resumo.add_row("[bold cyan]Consumo total:[/]", f"{total_consumo(lista_registros):.2f} kWh")
    resumo.add_row("[bold cyan]Custo total:[/]", f"R$ {total_custo(lista_registros):.2f}")
    resumo.add_row("[bold cyan]Equipamento que mais consumiu:[/]", maior_consumo["equipamento"]["nome"])

    console.print(resumo)
    console.print()
    console.print("[bold green]Top consumidores:[/]")

    for i, registro in enumerate(ranking):
        classificacao = registro['classificacao']

        if classificacao == "ALTO":
            cor = "green"

        else :
            if classificacao == "MODERADO":
                cor = "yellow"

            else :
                cor = "red"

        console.print(f"[cyan]{i+1}.[/] {registro['equipamento']['nome']} - {registro['consumo_kWh']:.3f} kWh | R$ {registro['custo']:.2f} | [bold {cor}]{classificacao}[/]")

if __name__ == "__main__":
    iniciar_sistema()