import flet as ft
from components.input_fields import LoginInput
from components.buttons import SubmitButton
from config.settings import *
import requests 

class ItemForm(ft.UserControl):
    def __init__(self, page:ft.Page, create=True, access_token=None, refresh_token=None):
        super().__init__()
        self.page = page
        self.page.title = "item form"
        self.create = create # variable to determine whether to send a post or put request
        # authorization token
        self.headers = {
            "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NzQ0MDc2LCJpYXQiOjE3MjYxMzkyNzYsImp0aSI6IjVjMDlkMDlmYjBlNjQwNjVhNDc3MDU5ZGQ5ZmUwYjk4IiwidXNlcl9pZCI6MX0.tFrq5xqiROxo8BdA08d6evUwSagfYFMYzB4I71tWa-s"
        }
        # setting the tokens
        self.access_token = access_token
        self.refresh_token = refresh_token
        # UI Elements
        self.item_name = LoginInput('Item name', 400, on_change=self.verify_input)
        self.category_name = LoginInput('Category', 400, on_change=self.verify_input)
        self.submit_button = SubmitButton(width=400, on_click=self.on_submit)
        self.error_message = ft.Text(color='red600')

        self.on_submit

    def on_submit(self, e):
        # request body
        self.body = {
            "name" : self.item_name.value,
            "category" : {
                "name" : self.category_name.value,
            }
        }
        if self.create:
            self.create_item()
            self.update()
        else:
            self.update_item()

    def verify_input(self, e):
        if self.item_name.value == '' or self.category_name.value == '':
            self.submit_button.disabled = True
        else:
            self.submit_button.disabled = False
        self.update()

    def create_item(self):
        self.results = None
        response = requests.post(f"{BASE_API_URL}products/", headers=self.headers, json=self.body)
        # Show success message and navigate to the home page
        if(response.status_code == 201):
            self.results = response.json()
            print(self.results)
            self.page.snack_bar = ft.SnackBar(
                ft.Text("Item Successfully Created", text_align='center', color='white'),
                bgcolor= CAMTEL_BLUE,
                open=True
                )
        else:
            print(response.status_code)
        self.update()

    def update_item(self):
        pass

    def build(self):
        return ft.Container(
             content=ft.Column(
                controls=[
                    ft.Text("Create Item", size=30, weight=ft.FontWeight.BOLD, color=CAMTEL_BLUE),
                    ft.Divider(height=8, color='white'),
                    self.item_name,
                    ft.Divider(height=2, color='white'),
                    self.category_name,
                    ft.Divider(height=6, color='white'),
                    self.error_message,
                    self.submit_button,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=15
            ),
        )