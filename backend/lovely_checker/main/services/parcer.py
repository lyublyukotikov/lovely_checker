import typing

import requests


class Parser:
    def parse_yandex(self):
        return ...


class Client:

    API_URL = "https://geocode-maps.yandex.ru/1.x/"
    PARAMS = {"format": "json"}

    @classmethod
    def request(cls, address: str) -> dict:
        response = requests.get(
            cls.API_URL, params=dict(geocode=address, **cls.PARAMS)
        )

        if response.status_code != 200:
            raise Exception(
                "Non-200 response from yandex geocoder"
            )

        return response.json()["response"]

    @classmethod
    def coordinates(cls, address: str) -> typing.Tuple[str, str]:
        data = cls.request(address)["GeoObjectCollection"]["featureMember"]

        if not data:
            raise Exception(
                '"{}" not found'.format(address)
            )

        coordinates = data[0]["GeoObject"]["Point"]["pos"]  # type: str
        print(data)
        print(data[0]["GeoObject"])
        return tuple(coordinates.split(" "))

Client.request(address='Тургеневский переулок, 24, Таганрог, Ростовская область')