import flet as ft
from components.input_fields import LoginInput
from components.buttons import SubmitButton
from config.settings import CAMTEL_BLUE

class LoginPage(ft.UserControl):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page  # Reference to the main page
        self.page.title = "Login"
        self.page.horizontal_alignment = 'center'
        self.page.vertical_alignment = 'center'

        self.error_message = ft.Text()

        # defining the page UI
        self.username_field = LoginInput('username', on_change=self.verify_input)
        self.password_field = LoginInput('password', password=True, reveal=True, on_change=self.verify_input)
        self.submit_button = SubmitButton(on_click=self.login)

        self.submit_button.width = 400


    def verify_input(self, e):
        if self.username_field.value == '' or self.password_field.value == '':
            self.submit_button.disabled = True
        else:
            self.submit_button.disabled = False
        self.update()

    def login(self, e):
        pass


    def build(self):
        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Text("Login", size=30, weight=ft.FontWeight.BOLD, color=CAMTEL_BLUE),
                    ft.Divider(height=8, color='white'),
                    self.username_field,
                    ft.Divider(height=2, color='white'),
                    self.password_field,
                    ft.Divider(height=6, color='white'),
                    self.error_message,
                    self.submit_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
            padding=20,
            border_radius=15,
            bgcolor='white',
            shadow=ft.BoxShadow(
                spread_radius=3,
                blur_radius=10,
                color=ft.colors.BLUE_GREY_400,
                offset=ft.Offset(0, 5),
            ),
            height=400,
            width=500,
        )