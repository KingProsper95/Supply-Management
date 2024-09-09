import flet as ft


class LoginInput(ft.TextField):
    """A login input field"""
    def __init__(self, label, password=False, reveal=False, on_change=None):
        super().__init__(
            label=label,
            width=400,
            password=password,
            on_change=on_change
        )
        self.color = 'black'
        self.can_reveal_password = reveal
        self.focused_border_color = 'blue'

