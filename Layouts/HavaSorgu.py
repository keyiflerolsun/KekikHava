# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Libs.HavaDurumu import hava_durumu
from asyncio         import new_event_loop

from flet.page import Page, ControlEvent
from flet      import UserControl, icons, ElevatedButton, Text, TextField, ProgressBar, ProgressRing, Row, Container

class HavaSorgu(UserControl):
    def __init__(self, sayfa:Page):
        super().__init__()
        self.sayfa = sayfa

        self.arama_alani = TextField(label="Şehir Giriniz", width=200, tooltip="Örn.: Çanakkale", hint_text="Ankara, Turkiye")
        self.ara_butonu  = ElevatedButton(text="Arama Yap", icon=icons.SEARCH, on_click=self.arama_fonksiyonu)
        self.yukleniyor  = Row([Text(), ProgressRing()], alignment="start", spacing=20)

    def arama_fonksiyonu(self, _:ControlEvent):
        if not self.arama_alani.value:
            self.arama_alani.error_text = "Lütfen Şehir Giriniz!"
            return self.update()

        self.splash              = ProgressBar()
        self.ara_butonu.disabled = True
        self.sayfa.add(self.yukleniyor)
        self.update()

        arama_degeri = self.arama_alani.value
        arama_verisi = new_event_loop().run_until_complete(hava_durumu(arama_degeri))
        arama_sonucu = Row([Text(), Text(arama_verisi)], alignment="start", spacing=20)

        self.splash              = None
        self.ara_butonu.disabled = False
        self.sayfa.remove(self.yukleniyor)
        self.update()

        self.sayfa.add(arama_sonucu)

    def build(self):
        return Container(
            content = Row(
                controls           = [
                    self.arama_alani,
                    self.ara_butonu
                ],
                vertical_alignment = "center"
            ),
            height  = 120,
            padding = 20
        )