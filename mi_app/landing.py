import reflex as rx

# Estado principal
class State(rx.State):
    mensaje: str = "Bienvenido a mi nueva página con Reflex"

    def cambiar_texto(self):
        self.mensaje = "¡Gracias por hacer clic!"

# Header estilo SaaS
def header() -> rx.Component:
    return rx.hstack(
        rx.text("MiLogo", weight="bold", size="7", color="white"),
        rx.spacer(),
        rx.link("Inicio", href="#", underline="none", color="white"),
        rx.link("Características", href="#", underline="none", color="white"),
        rx.link("Precios", href="#", underline="none", color="white"),
        rx.link("Contacto", href="#", underline="none", color="white"),
        padding="1.5em",
        align="center",
        bg="linear-gradient(to right, #1e3c72, #2a5298)"
    )

# Hero principal con CTA
def hero() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Envía el correo correcto en el momento correcto", size="9", color="black"),
            rx.text(
                "Conecta tu stack, crea flujos basados en comportamiento y convierte señales en resultados. Sin necesidad de ser experto en marketing.",
                size="5", color="gray", align="center"
            ),
            rx.hstack(
                rx.button("Prueba gratis", color_scheme="blue", size="3"),   # ✅ corregido
                rx.button("Ver cómo funciona", color_scheme="gray", size="3"),  # ✅ corregido
                spacing="4"
            ),
            spacing="6",
            align="center",
            padding="5em"
        ),
        bg="#f9f9f9"
    )

# Sección de métricas
def metrics() -> rx.Component:
    return rx.hstack(
        rx.card(rx.vstack(
            rx.heading("2000+", size="7", color="blue"),
            rx.text("Empresas confían")
        ), shadow="md", border_radius="lg", padding="2em"),
        rx.card(rx.vstack(
            rx.heading("50+", size="7", color="blue"),
            rx.text("Integraciones")
        ), shadow="md", border_radius="lg", padding="2em"),
        rx.card(rx.vstack(
            rx.heading("4.9/5", size="7", color="blue"),
            rx.text("Rating en Trustpilot")
        ), shadow="md", border_radius="lg", padding="2em"),
        spacing="6",
        justify="center",
        padding="3em"
    )

# Logos de clientes
def logos() -> rx.Component:
    return rx.hstack(
        rx.text("Landbot", size="5", color="gray"),
        rx.text("HEVO", size="5", color="gray"),
        rx.text("Squadcast", size="5", color="gray"),
        rx.text("Custify", size="5", color="gray"),
        rx.text("Appsmith", size="5", color="gray"),
        spacing="8",
        justify="center",
        padding="2em"
    )

# Sección de flujo visual (simplificado)
def workflow() -> rx.Component:
    return rx.vstack(
        rx.heading("Ejemplo de flujo automatizado", size="7", color="black"),
        rx.hstack(
            rx.card(rx.text("Usuario inicia prueba de 14 días"), padding="2em"),
            rx.text("→"),
            rx.card(rx.text("Esperar 5 días"), padding="2em"),
            rx.text("→"),
            rx.card(rx.text("¿Creó un proyecto?"), padding="2em"),
            spacing="4"
        ),
        rx.hstack(
            rx.card(rx.text("Sí → Oferta de upgrade"), padding="2em", bg="lightgreen"),
            rx.card(rx.text("No → Tips de activación"), padding="2em", bg="lightyellow"),
            spacing="6"
        ),
        spacing="6",
        align="center",
        padding="3em"
    )

# Footer minimalista
def footer() -> rx.Component:
    return rx.text("Hecho con ❤️ en Reflex", align="center", padding="2em", color="gray")

# Página principal
def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            header(),
            hero(),
            metrics(),
            logos(),
            workflow(),
            footer(),
            spacing="8",
            justify="center",
            min_height="85vh",
        )
    )
