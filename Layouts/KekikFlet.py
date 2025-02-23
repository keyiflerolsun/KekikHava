# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import flet as ft

class KekikFlet:
    def __init__(self, sayfa:ft.Page, baslik:str):
        sayfa.title                = baslik
        sayfa.horizontal_alignment = "center"
        sayfa.window_width = 540
        sayfa.padding      = 0
        sayfa.spacing      = 0

        sayfa.theme_mode = "dark"
        self.tema_degis  = ft.IconButton(icon=ft.icons.DARK_MODE_OUTLINED, on_click=self.tema_degis_fonksiyonu)

        sayfa.appbar = ft.AppBar(
            leading        = ft.Icon(ft.icons.CLOUD_CIRCLE_OUTLINED),
            toolbar_height = 40,
            title          = ft.Text("Hava Durumu"),
            center_title   = False,
            color          = "#EF7F1A",
            bgcolor        = "#2B2A29",
            actions        = [
                self.tema_degis,
                ft.PopupMenuButton(
                    items = [
                        ft.PopupMenuItem(),
                        ft.PopupMenuItem(text="Merhaba Dünya"),
                        ft.PopupMenuItem()
                    ],
                    tooltip = "Seçenekler"
                )
            ]
        )
        sayfa.update()

        self.sayfa = sayfa

    def tema_degis_fonksiyonu(self, _:ft.ControlEvent):
        self.sayfa.theme_mode = "dark" if self.sayfa.theme_mode == "light" else "light"
        self.tema_degis.icon  = ft.icons.WB_SUNNY_OUTLINED if self.sayfa.theme_mode == "light" else ft.icons.DARK_MODE_OUTLINED
        self.sayfa.update()