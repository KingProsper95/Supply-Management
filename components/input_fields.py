import flet as ft
from .buttons import SubmitButton

class LoginInput(ft.TextField):
    """A login input field"""
    def __init__(self, label, width, password=False, reveal=False, on_change=None):
        super().__init__(
            label=label,
            width=width,
            password=password,
            on_change=on_change
        )
        self.color = 'black'
        self.can_reveal_password = reveal
        self.focused_border_color = 'blue'

class SearchBox(ft.UserControl):
    def __init__(self, placeholder="Search...", width=250):
        super().__init__()
        self.search_box = ft.TextField(
            width=width,
            hint_text=placeholder,
            text_style=ft.TextStyle(size=16),  # Reduce font size
            on_change=self.on_search_change,
        )
        self.submit_button = SubmitButton('search', width=100)
    
    def on_search_change(self, e):
        if self.search_box.value != '':
            self.submit_button.disabled = False
        else:
            self.submit_button.disabled = True
        self.update()

    def build(self):
        return ft.Container(
            content=ft.Row(
                controls=[self.search_box, self.submit_button],
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=30
            ),
        )
