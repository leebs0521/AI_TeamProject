"""
@auther Hyunwoong
@since 7/1/2020
@see https://github.com/gusdnd852
"""

from kocrawl.dust import DustCrawler
from kocrawl.weather import WeatherCrawler
from kochat.app import Scenario
from kocrawl.map import MapCrawler
from Api.KnuInfo import KunInfoAnswer

weather = Scenario(
    intent='weather',
    api=WeatherCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['이번주']
    }
)

dust = Scenario(
    intent='dust',
    api=DustCrawler().request,
    scenario={
        'LOCATION': [],
        'DATE': ['오늘']
    }
)

restaurant = Scenario(
    intent='restaurant',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['맛집']
    }
)

travel = Scenario(
    intent='travel',
    api=MapCrawler().request,
    scenario={
        'LOCATION': [],
        'PLACE': ['관광지']
    }
)

knu_info = Scenario(
    intent = 'knu_info',
    api = KunInfoAnswer().request,
    scenario = {
        'KEYWORD' : [],
    }
)
