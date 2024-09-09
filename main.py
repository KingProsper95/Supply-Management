import flet as ft
from config.settings import *
from components.buttons import SideBarButton
from components.sidebar import SideBar
from utils.helpers import login
from pages.login import LoginPage

def main(page: ft.Page):
    page.title = "Camtel Supply App"
    page.theme_mode = 'light'

    sidebar = SideBar(page, 'Mr Jerry', 'Admin')

    def on_route_change(route):
        # Clear the current views but leave the sidebar intact
        content = []

        # Determine which page to show based on the route
        if page.route == "/overview":
            content.append(ft.Text("Overview Page"))
        elif page.route == "/customers":
            content.append(ft.Text("Customers Page"))
        elif page.route == "/items":
            content.append(ft.Text("Items Page"))
        elif page.route == "/orders":
            content.append(ft.Text("Orders Page"))
        elif page.route == "/items_out":
            content.append(ft.Text("Items Out Page"))
        elif page.route == "/suppliers":
            content.append(ft.Text("Suppliers Page"))
        else:
            content.append(ft.Text("Welcome to the Dashboard"))

        # Add the content to the right side of the layout
        page.views.append(
            ft.View(
                route,
                controls=[ft.Row([sidebar, ft.VerticalDivider(width=5), ft.Column(content)])]
            )
        )

        page.update()

    page.on_route_change = on_route_change

    # Start with the default route
    #page.go("/items")

    page.add(LoginPage(page))

ft.app(main)
