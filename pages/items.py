import flet as ft
from components.buttons import FormButton
from config.settings import *

class ItemsPage(ft.UserControl):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page = page
        self.page.title = 'Item Page'

    def build(self):
        return ft.Container(
            content=ft.Column([
                ft.Text('Items Page', color=TEXT_COLOR, size=30, weight='w400'),
                ft.Row(
                    controls=[FormButton("NEW PRODUCT")]
                )
                ],
                spacing=30
            ),
        )