import scrapy
from scrapy.loader import ItemLoader
from itemloaders.processors import TakeFirst
from datetime import datetime
from smtb.items import Article


class Smtb_spiderSpider(scrapy.Spider):
    name = 'smtb_spider'
    start_urls = ['https://fund.smtb.jp/smtb/qsearch.exe?F=mkt_news']

    def parse(self, response):
        links = response.xpath('//dd/a/@href').getall()
        yield from response.follow_all(links, self.parse_article)

    def parse_article(self, response):
        item = ItemLoader(Article())
        item.default_output_processor = TakeFirst()

        title = response.xpath('//h2/text()').get().strip()
        date = response.xpath('//p[@class="pType_01"]/text()').get().strip()
        date = datetime.strptime(date, '（%m/%d %H:%M）')
        date = date.strftime('%m/%d %H:%M')
        content = response.xpath('//div[@class="marketNewsContent"]//text()').getall()
        content = [text for text in content if text.strip()]
        content = "\n".join(content).strip()

        item.add_value('title', title)
        item.add_value('date', date)
        item.add_value('link', response.url)
        item.add_value('content', content)

        return item.load_item()
