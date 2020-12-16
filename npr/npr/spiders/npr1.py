import scrapy
from npr.items import NprItem


class Npr1Spider(scrapy.Spider):
    name = 'npr1'
    allowed_domains = ['https://www.npr.org/']
    start_urls = ['https://www.npr.org/get/1001/render/partial/next?start=22']

    def parse(self, response):
        urls = response.xpath("//*/div/div[2]/ul/li[3]/a[not(contains(@href,'about-npr'))and not(contains(@href,'twitter'))]/@href").extract()
        for url in urls:
            yield scrapy.Request(url,callback=self.parse_mp3, dont_filter=True)
    def parse_mp3(self,response):
        href = response.xpath('//*[@id="primaryaudio"]//div/div[2]/ul/li[1]/a/@href').extract()[0]
        title = response.xpath('//*[@id="main-section"]/article/div[2]/input[@type = "hidden"][1]/@value').extract()[0]
        print(title)
        print(type(title))
        script = "\n".join(response.xpath('//*[@id="main-section"]/article/div[@aria-label="Transcript"]/p[not(contains(@class,"disclaimer"))]/text()').extract())
        item = NprItem()
        item['file_urls'] = [href.split('?')[0]]

        item['file_name'] = title
        item['file_script'] = script
        yield item






