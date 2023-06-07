import time
from selectorlib import Extractor
from scrapy import Spider, Request
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

from mobile_de_parser.items import MobileDeItem


class MySpider(Spider):
    name = 'mobile_de_spider'
    start_urls = ['https://suchen.mobile.de/fahrzeuge/search.html?damageUnrepaired=NO_DAMAGE_UNREPAIRED&isSearchRequest=true&makeModelVariant1.makeId=25200&makeModelVariant1.modelId=19&maxFirstRegistrationDate=2022-12-31&maxMileage=150000&minFirstRegistrationDate=2000-01-01&minMileage=50000&ref=srpHead&scopeId=C&sortOption.sortBy=searchNetGrossPrice&sortOption.sortOrder=ASCENDING&refId=dc84461f-f220-8c1c-ef1d-6858662f830b']

    def parse(self, response):
        # Getting the driver object from meta
        driver = response.meta.get('driver')

        # If driver object was not passed, initialize a new Chrome driver
        if not driver:
            options = Options()
            options.add_argument("--headless")
            service = Service('mobile_de_parser/chromedriver')
            driver = webdriver.Chrome(service=service, options=options)

        driver.get(response.url)
        self.logger.info("Page successfully loaded")
        time.sleep(3)  # Introduce a delay to slow down the scraping process

        # Retrieve the page source after the delay
        data = driver.page_source

        extractor = Extractor.from_yaml_file('mobile_de_parser/selectorlib_yaml/mobile_de_parser.yml')
        extracted_data = extractor.extract(data)

        item = MobileDeItem()
        item['make'] = extracted_data['make']
        item['model'] = extracted_data['model']
        item['price'] = extracted_data['price']
        yield item

        # Close the driver if it was initialized in this function
        if not response.meta.get('driver'):
            driver.quit()
