import scrapy 


class MySpider(scrapy.Spider):
    name = 'mytheresa'
    start_urls = [' https://www.mytheresa.com/int/en/men/shoes?rdr=mag',

                ]


    def parse(self,response):
        for product in response.css('div.item'):
            product_link = product.css('div.item__info__name a::attr(href)').get()
            
            if product_link:
                yield response.follow(product_link, self.parse_product)

        next_page = response.css('a.pagination__item.pagination__item__text.pagination__item pagination__item__text--active').attrib['href']
        if next_page is not None:
            yield response.follow(next_page,self.parse)

            
    def parse_product(self,response):

        breadcrumbs = response.css('div.breadcrumb__item a::text').getall()
        image_url = response.css('div.swiper-slide img::attr(src)').get().strip()
        brand = response.css('div.product__area__branding__designer a::text').get().strip()
        product_name = response.css('div.product__area__branding__name::text').get().strip()
        listing_price = response.css('span.pricing__prices__value--original span.pricing__prices__price::text').get()
        offer_price = response.css('span.pricing__prices__value--discount span.pricing__prices__price::text').get()
        discount = response.css('span.pricing__info__percentage ::text').get()
        sizes = response.css('div.sizeitem__wrapper span.sizeitem__label::text').getall()
        description = response.css('div.accordion__body__content li::text').getall()
        other_images = response.css('div.swiper-slide img::attr(src)').getall()

        item = {
        'breadcrumbs': breadcrumbs,
        'image_url': image_url,
        'brand': brand,
        'product_name': product_name,
        'listing_price': listing_price,
        'offer_price': offer_price,
        'discount': discount,
        'sizes': sizes,
        'description': description,
        'other_images': other_images

    }

        yield item
        

        
