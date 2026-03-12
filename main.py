import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.padding = 20
    page.scroll = "adaptive"
    

    titulo = ft.Text(
        "Inicio de sesion",
        size=30,
        weight=ft.FontWeight.BOLD,
    )
    
    correo = ft.TextField(
        label="Correo electrónico",
        width=400,
    )
    

    contraseña= ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
        )
    
    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesion",
        width=250,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.GREEN_400,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )
    
    registro = ft.ElevatedButton(
        "Registrarme",
        width=200,
        style=ft.ButtonStyle(
            bgcolor=ft.Colors.BLUE_600,
            color=ft.Colors.WHITE,
            padding=20,
            shape=ft.RoundedRectangleBorder(radius=12),
        ),
    )

    
    page.add(
        ft.Column([
            titulo,
            ft.Container(height=10),
            correo,
            ft.Container(height=10),
            contraseña,
            ft.Container(height=10),
            ft.Container(height=20),
            ft.Row([iniciar_sesion, registro], alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.run(main)