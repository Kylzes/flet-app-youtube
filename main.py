import flet as ft

from menu import Menu
from header import Header
from menu_videos import MenuVidoes

def main(page: ft.Page):
    full_bar_menu = Menu(page)
    header = Header(page)

    page.spacing=0
    page.padding=0
    page.window.height=700
    page.window.max_width=1600
    page.window.min_width=770
    page.bgcolor=ft.Colors.GREY_700
    page.horizontal_alignment = ft.CrossAxisAlignment.START
    page.vertical_alignment = ft.MainAxisAlignment.START
    page.window.resizable = True
    page.window.center()

    print(page.window.height)



    page.add(
        ft.Stack(
            expand=True,
            controls=[
                header,
                full_bar_menu,
            ]
        )
    )
    page.update()


if __name__ == "__main__":
    ft.app(main)