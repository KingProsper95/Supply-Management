import flet as ft
from config.settings import *

class SideBarButton(ft.ListTile):
    def __init__(self, icon, label, route, selected=False, on_click=None):
        
        # Define colors based on selected state
        icon_color = CAMTEL_BLUE if selected else TEXT_COLOR
        text_color = CAMTEL_BLUE if selected else TEXT_COLOR

        super().__init__(
            leading=ft.Icon(icon, color=icon_color),
            title=ft.Text(label, color=text_color, size=16, style=ft.TextStyle(weight="w500")),
            selected=selected,
            on_click=on_click,
            data=route,
        )
        # Set colors for hover, selected, etc.

        self.selected_tile_color = HOVER_COLOR
        self.hover_color = HOVER_COLOR
        self.shape = ft.RoundedRectangleBorder(radius=10)
        self.mouse_cursor = 'CLICK'

