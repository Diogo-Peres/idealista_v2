import scrapy

class PrecosMiniprecoSpider(scrapy.Spider):
    name = "precos_idealista"
    allowed_domains = ["www.idealista.pt"]
    start_urls = ["https://www.idealista.pt/imovel/32733847/"]
    def parse(self, response):
        # Your parsing logic here
        yield{response}
