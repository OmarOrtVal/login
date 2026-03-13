import flet as ft

def main(page: ft.Page):
    page.title = "Login"
    page.padding = 20
    page.scroll = "adaptive"    

    usuario_valido = "admin@gmail.com"
    password_valido = "1234"

    def login(e):
        if correo.value == usuario_valido and contraseña.value == password_valido:
            mensaje.value = "Inicio de sesión exitoso"
            mensaje.color = "green"
            pantalla_principal()
        else:
            mensaje.value = "Correo o contraseña incorrectos"
            mensaje.color = "red"
        page.update()

    def pantalla_principal():
        page.clean()

    page.navigation_bar = ft.NavigationBar(
        destinations=[
            ft.NavigationBarDestination(icon=ft.Icons.HOME, label="Inicio"),
            ft.NavigationBarDestination(icon=ft.Icons.MENU, label="Menu"),
            ft.NavigationBarDestination(icon=ft.Icons.PERSON, label="Perfil"),
        ],
        on_change=lambda e: print(f"Seleccionado : {e.control.selected_index}")
    )

    barra_superior = ft.Container(
        content=ft.Text(
            "Panel Principal",
            size=20,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.WHITE
        ),
        bgcolor=ft.Colors.GREY_700,
        padding=15,
        border_radius=5,
        width=600
    )

    contenido = ft.Column(
        [
            ft.Text(
                "Bienvenido al Sistema",
                size=32,
                weight=ft.FontWeight.BOLD
            ),
            ft.Text(
                "Has iniciado sesión correctamente",
                size=16,
                color=ft.Colors.GREY_700
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True
    )

    page.add(
        ft.Column(
            [
                barra_superior,
                contenido
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            expand=True
        )
    )

    page.update()


    titulo = ft.Text(
        "Inicio de sesión",
        size=30,
        weight=ft.FontWeight.BOLD,
    )
    
    correo = ft.TextField(
        label="Correo electrónico",
        prefix_icon=ft.Icons.PERSON,
        width=400,
    )

    contraseña = ft.TextField(
        label="Contraseña",
        prefix_icon=ft.Icons.KEY,
        password=True,
        can_reveal_password=True,
        width=400,
    )

    mensaje = ft.Text("", color="red")

    link_forgot= ft.Button(
        "¿Olvidaste tu contraseña?"
    )

    iniciar_sesion = ft.ElevatedButton(
        "Iniciar sesión",
        width=250,
        on_click=login,
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
            mensaje,
            ft.Container(height=10),
            link_forgot,
            ft.Row([iniciar_sesion, registro], alignment=ft.MainAxisAlignment.CENTER)
        ],
        spacing=15,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER)
    )

ft.run(main)