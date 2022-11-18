# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI import cikis_yap, hata_yakala

from flet      import FLET_APP_HIDDEN, FLET_APP, WEB_BROWSER 
from flet      import app as flet
from flet.page import Page
from flet      import Divider

from Layouts import KekikFlet, HavaSorgu

def ana_sayfa(sayfa:Page):
    KekikFlet(sayfa, "Hava Durumu | @KekikAkademi")

    sayfa.add(Divider(height=1))

    sayfa.add(HavaSorgu(sayfa))

if __name__ == "__main__":
    try:
        flet(target=ana_sayfa, view=FLET_APP_HIDDEN, port=3434, assets_dir="Assets")
        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)