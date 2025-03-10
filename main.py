# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI     import cikis_yap, hata_yakala
import flet  as ft
from Layouts import KekikFlet, HavaSorgu

def ana_sayfa(sayfa:ft.Page):
    KekikFlet(sayfa, "Hava Durumu | @KekikAkademi")

    sayfa.add(ft.Divider(height=1))

    sayfa.add(HavaSorgu(sayfa))

if __name__ == "__main__":
    try:
        ft.app(target=ana_sayfa)
        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)