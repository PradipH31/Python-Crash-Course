#!./P2ENV/bin/python
# Country codes for pygal

from pygal.maps.world import COUNTRIES


def get_country_code(country_name):
    '''Get the country code'''
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    return None
