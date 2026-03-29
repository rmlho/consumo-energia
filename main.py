#Importanto as classes do services.py e do models.py para serem usadas aqui

from services import *
from models import *

from rich.console import Console
from rich.panel import Panel

console = Console()

def exibir_menu():
    console.print(Panel(":light_bulb: [bold blue]CONSUMO DE ENERGIA DOMÉSTICA[/] ||",title="MENU", style="bold cyan"))
    console.print("[blue]>> Selecione uma opção:[/]")
    console.print("[blue][1][/] Cadastrar equipamento")
    console.print("[blue][2][/] Registrar uso")
    console.print("[blue][3][/] Listar equipamentos")
    console.print("[blue][4][/] Ver ranking de consumo")
    console.print("[blue][5][/] Gerar relatório")
    console.print("[red][0] sair[/]")

def iniciar_sistema():
    rodando = True

    while rodando:
        exibir_menu()
        
        try:
            opcao = int(input("Escolha uma opção: "))

        except ValueError:
            console.print(":cross_mark: Valor inválido, digite um nímero")
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
                            print(f"{i+1}. {r['equipamento']['nome']} - {r['consumo_kWh']} kWh")

                    else :
                        if opcao == 5:
                            ranking = gerar_ranking(lista_registros)
                            gerar_relatorio(lista_registros, ranking)

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

