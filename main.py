import flet as ft
import flet
from flet import (
    ElevatedButton,
    FilePicker,
    FilePickerResultEvent,
    FilePickerFileType,
    Page,
    Row,
    Text,
    icons,
)


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER

    txt_number = ft.Text(value="0", text_align=ft.TextAlign.RIGHT, width=100)
    def save_clicked(e):
        save = txt_number.value
        filename = "save.txt"
        with open(filename, "w") as file:
            file.write(save)


    def button_clicked(e):
        txt_number.value = "0"
        page.update()

    def plus_click(e):
        txt_number.value = str(int(txt_number.value) + 1)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=button_clicked),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
                ft.IconButton("SAVE", on_click=save_clicked),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )

    )

ft.app(target=main)