import flet as ft

def main(page: ft.Page):
    page.title = "CarDoctor"
    page.bgcolor = "#F2F2F2"
    page.padding = 20

    titulo = ft.Text("🚗 CarDoctor", size=30, weight="bold", color="#1A73E8")
    subtitulo = ft.Text("Diagnóstico rápido do teu carro", size=16, color="grey")

    resultado = ft.Text("", size=18, weight="bold")

    def diagnosticar(e):
        sintoma = dropdown.value
        if sintoma == "Não pega":
            resultado.value = "🔋 Bateria fraca ou motor de arranque"
            resultado.color = "red"
        elif sintoma == "Fumaça branca":
            resultado.value = "💧 Problema no radiador / junta"
            resultado.color = "orange"
        elif sintoma == "Barulho no travão":
            resultado.value = "🛑 Pastilhas de travão gastas"
            resultado.color = "orange"
        elif sintoma == "Tremer ao andar":
            resultado.value = "⚙️ Alinhamento ou pneus"
            resultado.color = "blue"
        else:
            resultado.value = "Escolhe um sintoma"
        page.update()

    dropdown = ft.Dropdown(
        label="O que o carro está a fazer?",
        options=[
            ft.dropdown.Option("Não pega"),
            ft.dropdown.Option("Fumaça branca"),
            ft.dropdown.Option("Barulho no travão"),
            ft.dropdown.Option("Tremer ao andar"),
        ],
        width=300
    )

    botao = ft.ElevatedButton("Diagnosticar", on_click=diagnosticar, bgcolor="#1A73E8", color="white")

    page.add(titulo, subtitulo, dropdown, botao, resultado)

ft.app(target=main)
