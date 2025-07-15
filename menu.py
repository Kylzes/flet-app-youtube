import flet as ft


class Menu(ft.Container):

    def __init__(self, page: ft.Page):
        self.is_expanded = False
        self.additional_list_items = ft.Ref[ft.Column]()
        self.expand_button = ft.Ref[ft.ElevatedButton]()
        super().__init__(
            bgcolor=ft.Colors.BLACK54,
            top=45,
            left=0,
            bottom=0,
            expand=True,
            content=ft.Column(
                width=290,
                scroll=ft.ScrollMode.AUTO,
                spacing=0,
                horizontal_alignment=ft.CrossAxisAlignment.START,
                controls=[
                    self.btn_menu(ft.Icons.HOME, "Início"),
                    self.btn_menu(ft.Icons.SHORTCUT_ROUNDED, "Shorts"),
                    self.btn_menu(ft.Icons.APP_REGISTRATION, "Inscrições"),
                    self.divisor_menu(),
                    self.btn_you(ft.Icons.ARROW_RIGHT, "Você"),
                    self.btn_menu(ft.Icons.HISTORY, "Histórico"),
                    self.btn_menu(ft.Icons.PLAYLIST_PLAY, "Playlists"),
                    self.btn_menu(ft.Icons.ONDEMAND_VIDEO_OUTLINED, "Seus vídeos"),
                    self.btn_menu(ft.Icons.TIMER_OUTLINED, "Assistir mais tarde"),
                    self.btn_menu(ft.Icons.THUMB_UP_OUTLINED, "Vídeos com 'Gostei'"),
                    self.divisor_menu(),
                    self.text_value("Inscrições"),
                    self.list_incricoes(),
                    self.divisor_menu(),
                    self.text_value("Explorar"),
                    self.btn_menu(ft.Icons.LOCAL_FIRE_DEPARTMENT_OUTLINED, "Em alta"),
                    self.btn_menu(ft.Icons.SHOPPING_BAG_OUTLINED, "Shopping"),
                    self.btn_menu(ft.Icons.QUEUE_MUSIC_OUTLINED, "Música"),
                    self.btn_menu(ft.Icons.MOVE_DOWN_OUTLINED, "Filmes"),
                    self.btn_menu(ft.Icons.LIVE_TV_OUTLINED, "Ao vivo"),
                    self.btn_menu(ft.Icons.GAMES, "Jogos"),
                    self.btn_menu(ft.Icons.NEWSPAPER, "Notícias"),
                    self.btn_menu(ft.Icons.SPORTS, "Esportes"),
                    self.btn_menu(ft.Icons.BOOK_ONLINE, "Cursos"),
                    self.btn_menu(ft.Icons.PODCASTS, "Podcasts"),
                    self.divisor_menu(),
                    self.text_value("Mais do YouTube"),
                    self.btn_menu(ft.Icons.WORKSPACE_PREMIUM, "YouTube Premium"),
                    self.btn_menu(ft.Icons.WORKSPACES, "YouTube Studio"),
                    self.btn_menu(ft.Icons.LIBRARY_MUSIC, "YouTube Music"),
                    self.btn_menu(ft.Icons.CHILD_FRIENDLY, "YouTube Kids"),
                    self.divisor_menu(),
                    self.btn_menu(ft.Icons.SETTINGS, "Configurações"),
                    self.btn_menu(ft.Icons.REPORT_GMAILERRORRED_OUTLINED, "Histórico de denúncias"),
                    self.btn_menu(ft.Icons.HELP_OUTLINE, "Ajuda"),
                    self.btn_menu(ft.Icons.FEEDBACK, "Enviar feedback"),
                ]
            )
        )
        self.page = page

    def list_incricoes(self):
        return ft.Column(
            controls=[
                *self.list_visible(),
                ft.Column(
                    ref=self.additional_list_items,
                    controls=self.list_expande(),
                    visible=self.is_expanded,
                ),
                self.btn_more_see(),
            ]
        )

    def btn_more_see(self):
        self.icon_more_see = ft.Ref[ft.Icon]()
        self.text_more_see = ft.Ref[ft.Text]()

        return ft.TextButton(
            ref=self.expand_button,
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Icon(
                        ref=self.icon_more_see,
                        name=ft.Icons.KEYBOARD_ARROW_DOWN if not self.is_expanded else ft.Icons.KEYBOARD_ARROW_UP,
                        color=ft.Colors.WHITE,
                        size=30,
                    ),
                    ft.Text(
                        ref=self.text_more_see,
                        value="Ver mais" if not self.is_expanded else "Ver menos",
                        color=ft.Colors.WHITE,
                        size=20,
                        expand=True,
                    ),
                ]
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(10),
                padding=ft.padding.only(20, 10, 10, 10),
                overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                color=ft.Colors.WHITE,
            ),
            on_click=self.toggle_expansion,
        )

    def toggle_expansion(self, e):
        self.is_expanded = not self.is_expanded

        if self.additional_list_items.current:
            self.additional_list_items.current.visible = self.is_expanded

        if self.icon_more_see.current:
            self.icon_more_see.current.name = ft.Icons.KEYBOARD_ARROW_DOWN if not self.is_expanded else ft.Icons.KEYBOARD_ARROW_UP
        if self.text_more_see.current:
            self.text_more_see.current.value = "Ver mais" if not self.is_expanded else "Ver menos"

        self.page.update()

    def list_visible(self):
        return [self.btn_incricoes("Canal 1"),
                self.btn_incricoes("Canal 2"),
                self.btn_incricoes("Canal 3"), ]

    def list_expande(self):
        return [self.btn_incricoes("Canal 4"),
                self.btn_incricoes("Canal 5"),
                self.btn_incricoes("Canal 6"),
                self.btn_incricoes("Canal 7"),
                self.btn_incricoes("Canal 8"),
                self.btn_incricoes("Canal 9"), ]

    def text_value(self, text_value: str):
        return ft.Container(
            padding=ft.padding.only(20, 10, 0, 10),
            content=ft.Text(
                value=text_value,
                color=ft.Colors.WHITE,
                weight=ft.FontWeight.BOLD,
                size=20,
            )
        )

    def btn_incricoes(self, text_value: str):
        return ft.TextButton(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.CircleAvatar(
                        radius=18,
                        bgcolor=ft.Colors.GREY_700,
                    ),
                    ft.Text(
                        value=text_value,
                        color=ft.Colors.WHITE,
                    ),
                ]
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(10),
                padding=ft.padding.only(20, 10, 10, 10),
                overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                color=ft.Colors.WHITE,
            )
        )

    def btn_you(self, icon: ft.Icons, text_value: str):
        return ft.TextButton(
            content=ft.Row(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                controls=[
                    ft.Text(
                        value=text_value,
                        color=ft.Colors.WHITE,
                        size=20,
                        weight=ft.FontWeight.BOLD,
                    ),
                    ft.Icon(
                        name=icon,
                        color=ft.Colors.WHITE,
                        size=30,
                    ),
                ]
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(10),
                padding=ft.padding.only(20, 10,10,10),
                overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                color=ft.Colors.WHITE,
            )
        )

    def btn_menu(self, icon: ft.Icons, text_value: str):
        return ft.TextButton(
            content=ft.ResponsiveRow(
                alignment=ft.MainAxisAlignment.START,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Icon(
                        col={"xs": 2},
                        name=icon,
                        color=ft.Colors.WHITE,
                        size=24,
                    ),
                    ft.Text(
                        col={"xs": 8},
                        value=text_value,
                        color=ft.Colors.WHITE,
                        size=18,
                    ),
                    ft.Icon(
                        col={"xs": 2},
                        name=ft.Icons.CIRCLE,
                        color=ft.Colors.BLUE_ACCENT_200,
                        size=5,
                    )
                ]
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(10),
                padding=ft.padding.only(20,20,20,20),
                overlay_color=ft.Colors.with_opacity(0.1, ft.Colors.WHITE),
                color=ft.Colors.WHITE,
            )
        )

    def divisor_menu(self):
        return ft.Divider(
            color=ft.Colors.WHITE,
            thickness=1,
            leading_indent=10,
            trailing_indent=10,
        )