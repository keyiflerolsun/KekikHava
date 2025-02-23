# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI   import hata_salla
from httpx import AsyncClient

class HavaDurumu:
    def __init__(self, sehir:str):
        self.oturum    = AsyncClient()
        self.__api_key = "39bc7d31306a4bf5b5ee4ea4828b6c30"
        self.sehir     = sehir

    async def ver(self):
        try:
            istek = await self.oturum.get(
                url    = "https://api.weatherbit.io/v2.0/current/weather",
                params = {
                    "city" : self.sehir,
                    "key"  : self.__api_key
                }
            )

            sorgu = istek.json()
            veri  = sorgu["data"][0]
            return f"{veri['ob_time']} » [{veri['country_code']}] {veri['city_name']} - {veri['weather']['description']}"
        except Exception as hata:
            hata_salla(hata)
            return "Hava Durumu bilgisi alınamadı."