import flet as ft

def main(page: ft.Page):
    # Configurar o título da página e a cor de fundo
    page.title = "Cadastro de Pacientes"
    page.bgcolor = "#004B49"  # Verde escuro da Unimed

    # Criação dos controles para o formulário
    form = ft.Column(
        controls=[
            ft.Row(
                controls=[
                    ft.TextField(label="Código", width=100,bgcolor="#FFFFFF"),
                    ft.TextField(label="Data de cadastro", width=200,bgcolor="#FFFFFF"),
                    ft.TextField(label="Nome do paciente", width=900,bgcolor="#FFFFFF"),
                ]
            ),
            ft.Row(
                controls=[ 
                    ft.Dropdown(
                        label="Sexo",
                        width=200,
                        bgcolor="#FFFFFF",
                        options=[
                            ft.dropdown.Option("Masculino"),
                            ft.dropdown.Option("Feminino"),
                            ft.dropdown.Option("Outro")
                        ]
                    ),
                    ft.TextField(label="Data de Nascimento", width=200,bgcolor="#FFFFFF"),
                    ft.TextField(label="Idade", width=100,bgcolor="#FFFFFF"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.Dropdown(
                        label="Estado Civil",
                        width=200,bgcolor="#FFFFFF",
                        options=[
                            ft.dropdown.Option("Solteiro(a)"),
                            ft.dropdown.Option("Casado(a)"),
                            ft.dropdown.Option("Divorciado(a)"),
                            ft.dropdown.Option("Viúvo(a)")
                        ]
                    ),
                    ft.TextField(label="Profissão", width=325,bgcolor="#FFFFFF"),
                    ft.TextField(label="Naturalidade", width=325,bgcolor="#FFFFFF"),
                    ft.TextField(label="Cartão SUS", width=340,bgcolor="#FFFFFF"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.TextField(label="CPF", width=300,bgcolor="#FFFFFF"),
                    ft.TextField(label="RG", width=200,bgcolor="#FFFFFF"),
                    ft.TextField(label="Pai", width=345,bgcolor="#FFFFFF"),
                    ft.TextField(label="Mãe", width=345,bgcolor="#FFFFFF"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.TextField(label="Endereço", width=500,bgcolor="#FFFFFF"),
                    ft.TextField(label="Número", width=100,bgcolor="#FFFFFF"),
                    ft.TextField(label="Bairro", width=390,bgcolor="#FFFFFF"),
                    ft.TextField(label="CEP", width=200,bgcolor="#FFFFFF"),
                ]
            ),
            ft.Row(
                controls=[
                    ft.TextField(label="Cidade", width=430,bgcolor="#FFFFFF"),
                    ft.TextField(label="UF", width=50,bgcolor="#FFFFFF"),
                    ft.TextField(label="Celular", width=200,bgcolor="#FFFFFF"),
                    ft.TextField(label="Telefone", width=200,bgcolor="#FFFFFF"),
                    ft.TextField(label="Empresa", width=300,bgcolor="#FFFFFF"),
                ]
            ),
            ft.TextField(label="Observações", multiline=True, width=1220, height=150,bgcolor="#FFFFFF"),
            ft.Row(
                controls=[
                    ft.ElevatedButton(text="Salvar", on_click=lambda e: print("Salvo"), bgcolor="#00B3A6"),  # Verde claro da Unimed
                    ft.ElevatedButton(text="Limpar", on_click=lambda e: print("Limpo"), bgcolor="#00B3A6"),  # Verde claro da Unimed
                    ft.ElevatedButton(text="Fechar", on_click=lambda e: page.window_close(), bgcolor="#00B3A6"),  # Verde claro da Unimed
                ],
                alignment=ft.MainAxisAlignment.SPACE_AROUND, spacing=20
            ),
        ]
    )

    # Adicionar o formulário à página
    page.add(form)

# Executar o aplicativo
ft.app(target=main)
