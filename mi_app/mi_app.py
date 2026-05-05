import reflex as rx

class State(rx.State):
    mensaje: str = "Bienvenido a mi primera página con Reflex"

    def cambiar_texto(self):
        self.mensaje = "¡Gracias por hacer clic!"

def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Mi Proyecto con Reflex", size="9"),
            rx.text(State.mensaje, size="5"),
            rx.button("Haz clic aquí", on_click=State.cambiar_texto),
            spacing="5",
            justify="center",
            min_height="85vh",
        )
    )

app = rx.App()
app.add_page(index)
