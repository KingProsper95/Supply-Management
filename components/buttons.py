import flet as ft
from config.settings import *

class SideBarButton(ft.ListTile):
    def __init__(self, icon, label, route, selected=False, on_click=None):

        super().__init__(
            # Define colors based on selected state
            leading=ft.Icon(icon),
            title=ft.Text(label, size=16, style=ft.TextStyle(weight="w500")),
            selected=selected,
            on_click=on_click,
            data=route,
        )
        # Set colors for hover, selected, etc.
        self.selected_tile_color = HOVER_COLOR
        self.hover_color = HOVER_COLOR
        self.shape = ft.RoundedRectangleBorder(radius=10)
        self.mouse_cursor = 'CLICK'

class SubmitButton(ft.ElevatedButton):
    def __init__(self, on_click=None):
        super().__init__(
            on_click=on_click
        )
        self.text = 'Submit'
        self.bgcolor = '#134BF2'
        self.color = 'white'
        self.height = 40
        self.style = ft.ButtonStyle(
            shape= ft.RoundedRectangleBorder(radius=8),
            padding=12,
        )
        self.disabled = True

