import scrapy
from ..items import QuotutorialItem

class QuoteSpider(scrapy.Spider):
    # handle_httpstatus_list = [400]
    page_number = 2
    name = 'quotes'
    start_urls=['https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk03pjigdgSAV3rBmb7dJ5m_MVoqffw:1629722797267&ei=rZgjYfjaD43cz7sP7JeA2Ak&start=0&sa=N&ved=2ahUKEwi45abDlsfyAhUN7nMBHewLAJs4ChDy0wN6BAgBEDU&biw=1920&bih=937']
#response have all the source code, extract gives only data and remove selector, extract_first gives us string

    def parse(self, response):
        items =QuotutorialItem()
         #all_row=response.xpath("//div[@class='g']/div/div/div/a/@href")
     
        all_row=response.xpath("//div[@class='g']")
        print(all_row)
        #title =response.xpath("//input/@value").extract()
        for row in all_row:
            url=row.xpath("div/div/div/a/@href").extract_first()
            title =row.xpath("div/div/div/a/h3/text()").extract_first()
            # description =row.xpath("//div[@class='IsZvec']/div/span[last()]/text()").extract_first()
            description = row.xpath("//div[@class='VwiC3b MUxGbd yDYNvb lyLwlc lEBKkf']/text()").extract_first()
            # description = row.xpath("div/div/div[@class='VwiC3b MUxGbd yDYNvb lyLwlc lEBKkf']/text()").extract_first()

            items['url']=url
            items['title']=title
            items['description']=description
            yield items

        # next_page = 'https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk03pjigdgSAV3rBmb7dJ5m_MVoqffw:1629722797267&ei=rZgjYfjaD43cz7sP7JeA2Ak&start='+ str(QuoteSpider.page_number) + '0' + '/' + '&sa=N&ved=2ahUKEwi45abDlsfyAhUN7nMBHewLAJs4ChDy0wN6BAgBEDU&biw=1920&bih=937'
        next_page= 'https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk03svxmI8vLIWsMJGgFCCAUnm4YVpg:1628828037882&ei=hfEVYeypNdXC3LUPh7uGmAM&start='+str(QuoteSpider.page_number)+'0&sa=N&ved=2ahUKEwisgOSkka3yAhVVIbcAHYedATM4HhDy0wN6BAgBEDM&biw=795&bih=625'

        # if next_page is not None:
        if QuoteSpider.page_number <= 19:
            QuoteSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)

#     start_urls = [
#        # 'https://www.google.com/search?q=nepal+tour&oq=n&aqs=chrome.0.69i59j69i57j69i59j69i60l5.4485j0j7&sourceid=chrome&ie=UTF-8'
#         'https://www.google.com/search?q=Nepal+Travel&sxsrf=ALeKk02zk_TUGbMpUejgpMzP57t9gWJs6g:1629309316343&ei=hEkdYbSvFKfF4-EPlfO4-A8&start=0&sa=N&ved=2ahUKEwi0gZ6YkrvyAhWn4jgGHZU5Dv84ChDy0wN6BAgBEDQ&biw=1920&bih=937'   ]
# #
# #     def parse(self, response):
# #
# #
# #         items = QuotutorialItem()
# #         # url = response.xpath('//div[@class="g"]/div/div/div/a/@href').extract_first()
# #         print(url)
# #
# #
# #             # title = quotes.css('title::text').extract()
# #             # description = quotes.css('description::text').extract()
# #
# #         items['url']: url
# #             # items['title']: title
# #             # items['description']: description
# #
# #         yield items
# #
# #         # yield {
# #         #     'url': url,
# #         #     'title': title,
# #         #     'description': description
# #         #
# #         # }

#     def parse(self, response):
#         items = QuotutorialItem()
#         # all_row=response.xpath("//div[@class='g']/div/div/div/a/@href")

#         all_row = response.xpath("//div[@class='g']")
#         # title =response.xpath("//input/@value").extract()
#         for row in all_row:
#             url = row.xpath("div/div/div/a/@href").extract_first()
#             # title = row.xpath("div/div/div/a/h3/text()").extract_first()
#             # description = row.xpath("//div[@class='IsZvec']/div/span[last()]").extract_first()
#             items['url'] = url
#             # items['title'] = title
#             # items['description'] = description
#             yield items

