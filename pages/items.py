import flet as ft
from components.buttons import FormButton
from components.input_fields import SearchBox
from config.settings import *
from utils.helpers import *
import requests
from components.forms.item_form import ItemForm

class ItemsPage(ft.UserControl):

    def __init__(self, page: ft.Page, access_token, refresh_token):
        super().__init__()
        self.page = page
        self.page.title = 'Item Page'

        # Initialize pagination
        self.next_url = None
        self.previous_url = None

        # Search box initialization
        self.search = SearchBox('search item or category here...', width=275)

        # Adding a table
        self.table = ft.DataTable(
            height=400,
            width=1800,
            column_spacing=200,
            heading_text_style=ft.TextStyle(size=16, weight='w600'),
            heading_row_color=TABLE_HEADER_COLOR,
            columns=[
                ft.DataColumn(ft.Text("Id")),
                ft.DataColumn(ft.Text("Name")),
                ft.DataColumn(ft.Text("Category")),
                ft.DataColumn(ft.Text("Actions")),
            ],
            rows=[],
        )

        # Pagination buttons
        self.previous_button = ft.IconButton(
            icon=ft.icons.ARROW_BACK, tooltip="Previous page",icon_color='blue', on_click=self.load_previous_page, disabled=True
        )
        self.next_button = ft.IconButton(
            icon=ft.icons.ARROW_FORWARD, tooltip="Next page",icon_color='blue', on_click=self.load_next_page, disabled=True
        )

        # Initial load
        self.load_data(f"{BASE_API_URL}products/")

        self.item_form = ItemForm(self.page, create=True)

    def load_data(self, url):
        self.results = None
        self.headers = {
            "Authorization": f"Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI2NzQ0MDc2LCJpYXQiOjE3MjYxMzkyNzYsImp0aSI6IjVjMDlkMDlmYjBlNjQwNjVhNDc3MDU5ZGQ5ZmUwYjk4IiwidXNlcl9pZCI6MX0.tFrq5xqiROxo8BdA08d6evUwSagfYFMYzB4I71tWa-s"
        }

        response = requests.get(url, headers=self.headers)

        if response.status_code == 200:
            self.results = response.json()

            # Update pagination
            self.next_url = self.results.get("next")
            self.previous_url = self.results.get("previous")

            # Enable/Disable pagination buttons based on data
            self.next_button.disabled = self.next_url == None
            self.previous_button.disabled = self.previous_url == None

            # Clear existing rows in the table
            self.table.rows.clear()

            # Add new rows from the results
            for product in self.results['results']:
                self.table.rows.append(
                    ft.DataRow(
                        cells=[
                            ft.DataCell(ft.Text(str(product['id']))),
                            ft.DataCell(ft.Text(product['name'])),
                            ft.DataCell(ft.Text(product['category']['name'])),
                            ft.DataCell(
                                content=ft.Row(
                                    [
                                        ft.IconButton(
                                            icon=ft.icons.EDIT,
                                            icon_color=CAMTEL_BLUE,
                                            icon_size=20,
                                            tooltip="Edit record",
                                        ),
                                        ft.IconButton(
                                            icon=ft.icons.DELETE_FOREVER_ROUNDED,
                                            icon_color=TRASH_COLOR,
                                            icon_size=20,
                                            tooltip="Delete record",
                                        ),
                                    ]
                                ),
                            ),
                        ]
                    )
                )
            
            # Update the page to reflect new data
            self.page.update()
        else:
            self.page.go("/login")

    def load_previous_page(self, e):
        if self.previous_url:
            self.load_data(self.previous_url)
            self.update()

    def load_next_page(self, e):
        if self.next_url:
            self.load_data(self.next_url)
            self.update()

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Text('Items Page', color=TEXT_COLOR, size=30, weight='w400'),
                    ft.Row(
                        controls=[FormButton("NEW PRODUCT"), self.search],
                        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    ),
                    ft.Container(content=self.table),
                    ft.Divider(height=5),
                    ft.Row(
                        controls=[self.previous_button, self.next_button],
                        alignment=ft.MainAxisAlignment.END,
                    ),
                    self.item_form
                ],
                spacing=30,
            ),
        )
