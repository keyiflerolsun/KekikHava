# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI     import hata_salla
from aiohttp import ClientSession
from asyncio import run
from atexit  import register as kapanirken

class HavaDurumu:
    def __oturum_kapa(self):
        run(self.oturum.close())

    def __init__(self, sehir:str):
        self.oturum = ClientSession()
        kapanirken(self.__oturum_kapa)

        self.__api_key = "39bc7d31306a4bf5b5ee4ea4828b6c30"
        self.sehir     = sehir

    async def ver(self):
        async with self.oturum.get(
            url     = "https://api.weatherbit.io/v2.0/current/weather",
            params  = {
                "city" : self.sehir,
                "key"  : self.__api_key
            },
        ) as yanit:
            return await yanit.json()

async def hava_durumu(sehir:str):
    _hava = HavaDurumu(sehir)
    sorgu = await _hava.ver()
    veri  = sorgu["data"][0]
    try:
        return f"{veri['ob_time']} » [{veri['country_code']}] {veri['city_name']} - {veri['weather']['description']}"
    except KeyError:
        hata_salla(sorgu["error"])
        return sorgu["error"]