import flet as ft
from components.input_fields import LoginInput
from components.buttons import SubmitButton
from config.settings import *
import requests
# from session_manager import SessionManager
from utils import helpers

class LoginPage(ft.UserControl):
    def __init__(self, page:ft.Page):
        super().__init__()
        self.page = page  # Reference to the main page
        self.page.title = "Login"
        self.page.route = "/login"
    
        self.error_message = ft.Text(color='red600')

        # defining the page UI
        self.username_field = LoginInput('username', on_change=self.verify_input)
        self.password_field = LoginInput('password', password=True, reveal=True, on_change=self.verify_input)
        self.submit_button = SubmitButton(width=400, on_click=self.login)

    def verify_input(self, e):
        if self.username_field.value == '' or self.password_field.value == '':
            self.submit_button.disabled = True
        else:
            self.submit_button.disabled = False
        self.update()

    def login(self, e):
        """
        Here when the user tries to login these are the following possibilities
        valid credentials -> navigates the user to the main page
        invalid credentials -> sends an error message
        no credentials -> sends an error message
        server unreachable -> throws an exception which is caught and sent to the use
        """
        try:
            # Send POST request to Django backend with the username and password
            response = requests.post(BASE_API_URL + "token/", json={
                "username": self.username_field.value,
                "password": self.password_field.value
            })
            # Handle response from the server
            if response.status_code == 200:
                tokens = response.json()  # Get the JWT tokens
                access_token = tokens['access']
                refresh_token = tokens['refresh']
                #store all the data
                helpers.USERNAME = self.username_field.value
                helpers.ACCESS_TOKEN = access_token
                helpers.REFRESH_TOKEN = refresh_token
                # Store access token, refresh token, and username in SessionManager
                # session = SessionManager.get_instance()
                # session.set_session_data(access_token, refresh_token, self.username_field.value)
                # print(f"Username set in session: {session.get_username()}")
                print(f"from helpers {helpers.USERNAME}")
                # Show success message and navigate to the home page
                self.page.snack_bar = ft.SnackBar(
                    ft.Text("Login Successful!", text_align='center', color='white'),
                    bgcolor= CAMTEL_BLUE,
                    open=True
                    )
                #navigate to the items page
                self.page.go('/items')
            elif response.status_code == 401:
                self.error_message.value = response.json()['detail']
            else:
                self.error_message.value = 'Username and password fields are required'

            self.update()

        except Exception:
            self.error_message.value = "Server is unreachable"
            self.update()

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