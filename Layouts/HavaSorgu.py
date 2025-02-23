# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import flet          as ft
from Libs.HavaDurumu import HavaDurumu

class HavaSorgu(ft.Container):
    def __init__(self, sayfa:ft.Page):
        super().__init__()
        self.sayfa   = sayfa

        self.arama_alani = ft.TextField(label="Şehir Giriniz", width=200, tooltip="Örn.: Çanakkale", hint_text="Ankara, Turkiye")
        self.ara_butonu  = ft.ElevatedButton(text="Arama Yap", icon=ft.icons.SEARCH, on_click=self.arama_fonksiyonu)
        self.yukleniyor  = ft.Row([ft.Text(), ft.ProgressRing()], alignment="start", spacing=20)

        self.content = ft.Row(
            vertical_alignment = "center",
            controls           = [
                self.arama_alani,
                self.ara_butonu
            ]
        )
        self.height  = 120
        self.padding = 20

    async def arama_fonksiyonu(self, _:ft.ControlEvent):
        if not self.arama_alani.value:
            self.arama_alani.error_text = "Lütfen Şehir Giriniz!"
            return self.update()

        self.splash              = ft.ProgressBar()
        self.ara_butonu.disabled = True
        self.sayfa.add(self.yukleniyor)
        self.update()

        arama_degeri = self.arama_alani.value
        hava         = HavaDurumu(arama_degeri)
        arama_verisi = await hava.ver()
        arama_sonucu = ft.Row([ft.Text(), ft.Text(arama_verisi)], alignment="start", spacing=20)

        self.splash              = None
        self.ara_butonu.disabled = False
        self.sayfa.remove(self.yukleniyor)
        self.update()

        self.sayfa.add(arama_sonucu)