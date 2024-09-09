import flet as ft
from .buttons import SideBarButton
from config.settings import *

class SideBar(ft.UserControl):
    def __init__(self, page:ft.Page, username, description):
        super().__init__()
        self.page = page  # Store the page object reference
        self.username = username
        self.description = description

         # List of all sidebar buttons
        self.buttons = [
            SideBarButton(ft.icons.GRID_VIEW, "Overview", "/overview", on_click=self.navigate_to),
            SideBarButton(ft.icons.PEOPLE, "Customers", "/customers", selected=False, on_click=self.navigate_to),
            SideBarButton(ft.icons.INVENTORY_2_OUTLINED, "Items", "/items", selected=True, on_click=self.navigate_to),
            SideBarButton(ft.icons.SHOPPING_BAG, "Orders", "/orders", on_click=self.navigate_to),
            SideBarButton(ft.icons.EXIT_TO_APP, "Items out", "/items_out", on_click=self.navigate_to),
            SideBarButton(ft.icons.PERSON_ADD, "Suppliers", "/suppliers", on_click=self.navigate_to),
        ]

    def navigate_to(self, e):
        if self.page:  # Check if the page is set
            print(f"Navigating to {e.control.data}")
            self.page.go(e.control.data)  # Navigate to the route
            for button in self.buttons:
                button.selected = button.data == e.control.data  # Update selected button
            self.page.update()  # Update the page to reflect changes
        else:
            print("Page object is None")

    def user_data(self):
        #first row has user info, different from the icon row so we create a function for it
        return ft.Container(
            padding=15,
            content= ft.Row(
                controls = [
                    ft.CircleAvatar(
                        content=ft.Text("AA"),
                        bgcolor="blue400",
                        radius=26,
                    ),
                    ft.Column(
                        spacing=1,
                        controls=[
                            ft.Text(
                                value=self.username,
                                size=16,
                                weight="bold",
                                color=TEXT_COLOR
                            ),
                            ft.Text(
                                value=self.description,
                                size=16,
                                weight="w200",
                                color=TEXT_COLOR,
                            )
                        ]
                    )
                ],
                spacing=20
            )
        )

    def build(self):
        #defining the characteristics and dimensions of the returned sidebar
        return ft.Container(
            height=1024,
            width=260,
            padding=ft.padding.only(top=10),
            content=ft.Column(
                horizontal_alignment=ft.MainAxisAlignment.CENTER,
                controls=[
                    self.user_data(),
                    ft.Divider(height=15, color='blue100'),
                    *self.buttons
                ]
            )
        )