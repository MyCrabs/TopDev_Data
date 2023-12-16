from scrapy.spiders import Spider
from scrapy.http import Request

class MySpider(Spider):
    name = "my_spider"
    start_urls = ["https://example.com"]

    def parse(self, response):
        # Lấy dữ liệu từ trang web

        # In dữ liệu ra console

        print(">>>", data)

        # Theo dõi các liên kết trên trang web

        yield from response.follow_links()
