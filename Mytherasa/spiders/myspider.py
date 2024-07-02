import scrapy


class MyspiderSpider(scrapy.Spider):
    name = "myspider"
    allowed_domains = ["www.mytheresa.com"]
    start_urls = ["https://www.mytheresa.com/int_en/men/shoes.html"]

    def parse(self, response):
        products=response.css('div.item')
        for pro in products:
            yield{
                'discription':pro.css('div.item__info__name a::text').get(),
                'name':pro.css('div.item__info__header__designer::text').get(),
                'image' : pro.css('div.item_images_image img::attr(src)').get(),
                'price':pro.css('span.pricing__prices__price::attr(src)').get(),
                'discount':pro.css('')
            }
 
