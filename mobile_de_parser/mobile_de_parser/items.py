import scrapy

class MobileDeItem(scrapy.Item):
    make = scrapy.Field()
    model = scrapy.Field()
    price = scrapy.Field()
