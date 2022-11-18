# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flet.page import Page, ControlEvent
from flet      import IconButton, AppBar, Icon, icons, PopupMenuButton, PopupMenuItem, Text

class KekikFlet:
    def __init__(self, sayfa:Page, baslik:str):
        sayfa.title                = baslik
        sayfa.horizontal_alignment = "center"
        sayfa.window_width = 540
        sayfa.padding      = 0
        sayfa.spacing      = 0

        sayfa.theme_mode = "dark"
        self.tema_degis  = IconButton(icon=icons.DARK_MODE_OUTLINED, on_click=self.tema_degis_fonksiyonu)

        sayfa.appbar = AppBar(
            leading        = Icon(icons.CLOUD_CIRCLE_OUTLINED),
            toolbar_height = 40,
            title          = Text("Hava Durumu"),
            center_title   = False,
            color          = "#EF7F1A",
            bgcolor        = "#2B2A29",
            actions        = [
                self.tema_degis,
                PopupMenuButton(
                    items = [
                        PopupMenuItem(),
                        PopupMenuItem(text="Merhaba Dünya"),
                        PopupMenuItem()
                    ],
                    tooltip = "Seçenekler"
                )
            ]
        )
        sayfa.update()

        self.sayfa = sayfa

    def tema_degis_fonksiyonu(self, _:ControlEvent):
        self.sayfa.theme_mode = "dark" if self.sayfa.theme_mode == "light" else "light"
        self.tema_degis.icon  = icons.WB_SUNNY_OUTLINED if self.sayfa.theme_mode == "light" else icons.DARK_MODE_OUTLINED
        self.sayfa.update()