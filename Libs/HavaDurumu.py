# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from aiohttp import ClientSession
from asyncio import run
from atexit  import register as kapanirken

class HavaDurumu:
    def __oturum_kapa(self):
        run(self.oturum.close())

    def __init__(self, sehir:str):
        self.oturum = ClientSession()
        kapanirken(self.__oturum_kapa)

        self.__api_key = "beb64d2aebef4d8394b48fa0f23da885"
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
    veri  = (await _hava.ver())["data"][0]
    return f"{veri['ob_time']} » [{veri['country_code']}] {veri['city_name']} - {veri['weather']['description']}"