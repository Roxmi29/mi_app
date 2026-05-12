import reflex as rx
from reflex_base.plugins.sitemap import SitemapPlugin
from reflex.plugins import RadixThemesPlugin

config = rx.Config(
    app_name="mi_app",
    disable_plugins=[SitemapPlugin],   # desactiva SitemapPlugin
    plugins=[RadixThemesPlugin()]      # activa Radix explícitamente
)
