import requests
from bs4 import BeautifulSoup
from .hard_code import HardCode


class PageFocus(HardCode):
    def __init__(self):
        super().__init__()

    def request_page(self, url):
        response : str = requests.get(url).text
        soup = BeautifulSoup(response, 'html.parser')
        return soup
