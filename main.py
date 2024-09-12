import flet as ft
from config.settings import *
from components.sidebar import SideBar
from pages.login import LoginPage
from pages.items import ItemsPage
from utils import helpers

def main(page: ft.Page):
    page.theme_mode = 'light'
    page.theme = ft.Theme(color_scheme_seed=BACKGROUND_COLOR)
    page.scroll = "auto"
    
    # Set the initial window width and height
    page.window.width = 1400
    page.window.height = 900
    # Enforce the minimum width and height when resizing
    page.window.min_width = 1250
    page.window.min_height = 800

    sidebar = SideBar(page)

    def on_route_change(route):
        sidebar.username = helpers.USERNAME
        sidebar.logo_name = sidebar.username[:2].upper() # getting the first two letters of the username
        if page.route == "/login":
            page.views.append(
                ft.View(
                    route,
                    controls=[LoginPage(page)],
                    vertical_alignment='center',
                    horizontal_alignment='center',
                )
            )
        else:
            # Clear the current views but leave the sidebar intact
            content = []

            # Determine which page to show based on the route
            if page.route == "/overview":
                content.append(ft.Text("Overview Page"))
            elif page.route == "/customers":
                content.append(ft.Text("Customers Page"))
            elif page.route == "/items":
                content.append(ItemsPage(page, access_token=helpers.ACCESS_TOKEN, refresh_token=helpers.REFRESH_TOKEN))
            elif page.route == "/orders":
                content.append(ft.Text("Orders Page"))
            elif page.route == "/items_out":
                content.append(ft.Text("Items Out Page"))
            elif page.route == "/suppliers":
                content.append(ft.Text("Suppliers Page"))
            else:
                content.append(ft.Text("Welcome to the Dashboard"))

            # Add the content to the right side of the layout with scrolling enabled in a Column
            page.views.append(
                ft.View(
                    route,
                    controls=[
                        ft.Row([
                            sidebar,
                            ft.Container(
                                content=ft.Column(
                                    content,  # Wrap the content in a Column
                                    scroll="auto",  # Enable vertical scrolling
                                    expand=True,  # Make sure the column expands vertically
                                ),
                                padding=15,
                                expand=True,  # Content takes up the remaining space
                                bgcolor=BACKGROUND_COLOR,
                            )
                        ],
                        expand=True
                        )
                    ]
                )
            )
        page.update()

    page.on_route_change = on_route_change
    page.go("/items")   # Default page which is the items page

ft.app(target=main)
