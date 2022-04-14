from http import HTTPStatus

import requests

from contants import API_KEY, LON, LAT


class TestOpenWeatherApi:
    base_url = 'https://api.openweathermap.org/data/2.5/weather'

    def test_correct_coordinates(self, master_controller):
        master_controller.execute()
        response = requests.get(f"{self.base_url}?lat={LAT}&lon={LON}&appid={API_KEY}")
        assert response.status_code == HTTPStatus.OK

    def test_incorrect_coordinates(self, master_controller):
        master_controller.execute()
        latitude = 'a'
        longitude = 'b'
        response = requests.get(f"{self.base_url}?lat={latitude}&lon={longitude}&appid={API_KEY}")
        assert response.status_code == HTTPStatus.BAD_REQUEST
