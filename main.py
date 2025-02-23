# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI import cikis_yap, hata_yakala

from flet import app as flet
from flet import Page, Divider

from Layouts import KekikFlet, HavaSorgu

def ana_sayfa(sayfa:Page):
    KekikFlet(sayfa, "Hava Durumu | @KekikAkademi")

    sayfa.add(Divider(height=1))

    sayfa.add(HavaSorgu(sayfa))

if __name__ == "__main__":
    try:
        flet(target=ana_sayfa)
        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)