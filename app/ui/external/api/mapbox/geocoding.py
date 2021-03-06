import requests
from app.ui.external.api.mapbox import api_key
# 'https://api.mapbox.com/geocoding/v5/mapbox.places/-73.40970188275578,40.690894499124994.json?access_token=pk.eyJ1IjoibWltc2xhZGUiLCJhIjoiY2trZnUxajFjMGY4djJ2bnc3OXdoN3J4YSJ9.RTrxB7_bNl0JOHPXYJeF4g'


def get_geoinformation_by_latlng(lat, lng, **kwargs):
    base = 'https://api.mapbox.com/geocoding/v5'
    endpoint = 'mapbox.places'
    url = f'{base}/{endpoint}/{lat},{lng}.json?access_token={api_key}'
    result = requests.get(url)
    try:
        result.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(e)
        return {'status': 404}

    return result.json()


if __name__ == '__main__':
    get_geoinformation_by_latlng('-1', '4')
