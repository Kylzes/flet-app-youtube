import flet as ft


class Header(ft.Container):
    def __init__(self, page: ft.Page):
        super().__init__(
            bgcolor=ft.Colors.GREY_800,
            padding=ft.padding.only(5,0,5,0),
            #top=0,
            #left=0,
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                controls=[
                    self.btn_icon(ft.Icons.MENU),
                    self.btn_logo(),
                    self.box_search(),
                    self.btn_criar(),
                    self.btn_icon(ft.Icons.SETTINGS_VOICE_OUTLINED),
                    self.btn_icon(ft.Icons.NOTIFICATIONS_OUTLINED),
                    self.avatar(),
                ]
            ),
        )

        self.page = page

    def avatar(self):
        return ft.IconButton(
            col={"xxl": 0.4, "xl": 0.4, "lg": 0.4, "md": 0.4},
            padding=0,
            width=45,
            height=45,
            content=ft.CircleAvatar(
                radius=22.5,
                bgcolor=ft.Colors.GREY_700,
            )
        )


    def btn_logo(self):
        return ft.Container(
            col={"xxl": 2.0, "xl": 2.0, "lg": 2.0, "md": 2.0},
            width=100,
            height=40,
            border_radius=0,
            content=ft.TextButton(
                text="YouTube",
                style=ft.ButtonStyle(
                    color=ft.Colors.RED_ACCENT,
                    text_style=ft.TextStyle(
                        size=25,
                        weight=ft.FontWeight.BOLD,
                        italic=True,
                    ),
                    shape=ft.RoundedRectangleBorder(10),
                ),
            ),
        )

    def btn_criar(self):
        return ft.TextButton(
            col={"xxl": 1.0, "xl": 1.0, "lg": 1.0, "md": 1.0},
            icon=ft.Icons.ADD,
            text="Criar",
            height=40,
            width=80,
            style=ft.ButtonStyle(
                alignment=ft.alignment.center,
                padding=ft.padding.only(0, 0, 5, 0),
                icon_color=ft.Colors.WHITE,
                icon_size=25,
                color=ft.Colors.WHITE,
                shape=ft.RoundedRectangleBorder(10),
                text_style=ft.TextStyle(
                    color=ft.Colors.WHITE,
                    size=25,
                ),
            ),
        )

    def btn_icon(self, icon: ft.Icons):
        return ft.Container(
            col={"xxl": 0.4, "xl": 0.4, "lg": 0.4, "md": 0.4},
            width=40,
            height=40,
            content=ft.IconButton(
                padding=0,
                alignment=ft.alignment.center,
                icon=icon,
                icon_color=ft.Colors.WHITE,
                icon_size=25,
            )
        )

    def box_search(self):
        return ft.Row(
            alignment=ft.MainAxisAlignment.CENTER,
            height=40,
            expand=True,
            col={"xxl": 7.4, "xl": 7.4, "lg": 7.4, "md": 7.4},
            controls=[
                ft.TextField(
                    hint_text="Pesquisar",
                    text_size=16,
                    border_radius=ft.border_radius.only(20,0,20,0),
                    filled=True,
                    fill_color=ft.Colors.GREY_700,
                    border_width=0,
                    content_padding=ft.padding.only(left=10,right=10),
                    expand=True,
                ),
                ft.IconButton(
                    icon=ft.Icons.KEYBOARD,
                    icon_color=ft.Colors.WHITE,
                ),
                ft.TextButton(
                    icon=ft.Icons.SEARCH,
                    icon_color=ft.Colors.WHITE,
                    style=ft.ButtonStyle(
                        icon_size=30,
                        bgcolor=ft.Colors.GREY_700,
                        padding=10,
                        shape=ft.RoundedRectangleBorder(
                            ft.border_radius.only(0,20,0,20)),
                    )

                )
            ]
        )