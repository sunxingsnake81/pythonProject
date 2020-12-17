import scrapy
from cgw.items import CgwItem


class Cg1Spider(scrapy.Spider):
    name = 'cg1'

    allowed_domains = ['ccgp.gov.cn']
    start_urls = ['http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index=1&bidSort'
        '=0&buyerName=&projectId=&pinMu=0&bidType=&dbselect=bidx&kw=%E6%B5%8B%E5%BA%8F%E4%BB%AA&star'
                  't_time=2020%3A12%3A17&end_time=2020%3A11%3A17&timeType=3&displayZone=&zoneI'
                  'd=&pppStatus=0&agentName=3E']

    # start_urls = ['http://www.ccgp.gov.cn/cggg/dfgg/']
    i = 2

    def parse(self, response):
        # str1 = "/html/body[@id='bid_lst']/div[@class='main']/div" \
        #        "[@class='main_container']/div[@class='main_left_block mt13']/div" \
        #        "[@class='wz_block']/div[@class='vF_detail_relcon" \
        #        "tent mt13']/div[@class='vF_detail_relcontent_lst']/ul" \
        #        "[@class='c_list_bid']/li["
        # str2 = "]/a/text()"
        # str3 = "]/a/@href"

        global tit
        str1 = "/html/body/div[@class='vT_z'][4]/div[@class='vT_z']/div"\
                   "[@class='vT-srch-result']/div[@class='vT-srch-result-list-con2']"\
               "/div[@class='vT-srch-result-list']/ul[@class='vT-srch-result-list-bid']/li["
        str2 = "]/a/text()"
        str3 = "]/a/@href"
        str4 = "]/span/text()[1]"
        item = CgwItem()

        for p in range(1, 21):
            tit = response.xpath(str1 + str(p) + str2).extract()

            s = "".join(tit)
            # print(tit)
            if response.xpath(str1 + str(p) + str3).extract() :
                url = response.xpath(str1 + str(p) + str3).extract()[0]
            else :
                url = "url is not exit"
            if response.xpath(str1 + str(p) + str4).extract():

                msg = response.xpath(str1 + str(p) + str4).extract()[0]
            else:
                msg = "msg is not exit"
            # if tit[0].find('测序') == -1:
            #     pass
            #     # print('no')
            # print(tit)
            # print(url)
            # print(msg.split('|')[0])
            if msg.split('|'):

                time = msg.split('|')[0]
                if len(msg.split('|')) >= 2:
                    cust = msg.split('|')[1]
                else:
                    cust = "cust not exit"
                if len(msg.split('|')) >= 3:
                    prox = msg.split('|')[2]
                else:
                    prox = "prox not exit"

            else:
                time,cust,prox = "not exit","not exit","not exit"
            item['title'] = s.strip()
            item['url'] = url
            item['time'] = time
            item['cust'] = cust
            item['prox'] = prox



            yield item

        # if tit == "":
        #     pass
        if tit :
            url1 = "http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index="
            url3 = "&bidSort" \
                   "=0&buyerName=&projectId=&pinMu=0&bidType=&dbselect=bidx&kw=%E6%B5%8B%E5%BA%8F%E4%BB%AA&star" \
                   "t_time=2019%3A12%3A12&end_time=2020%3A12%3A12&timeType=3&displayZone=&zoneI" \
                   "d=&pppStatus=0&agentName="
            URL = url1 + str(self.i) + url3
            print(self.i)
            yield scrapy.Request(URL, callback=self.parse)
        else:
            print('its over')

        self.i += 1




        # else:
        #     url1 = "http://search.ccgp.gov.cn/bxsearch?searchtype=1&page_index="
        #     url3 = "&bidSort" \
        #            "=0&buyerName=&projectId=&pinMu=0&bidType=&dbselect=bidx&kw=%E6%B5%8B%E5%BA%8F%E4%BB%AA&star" \
        #            "t_time=2020%3A11%3A09&end_time=2020%3A12%3A10&timeType=3&displayZone=&zoneI" \
        #            "d=&pppStatus=0&agentName="
        #     # url3 = "&bidSort" \
        #     #            "=0&buyerName=&projectId=&pinMu=0&bidType=&dbselect=bidx&kw=测序仪&star" \
        #     #        "t_time=2020%3A11%3A09&end_time=2020%3A12%3A10&timeType=3&displayZone=&zoneI" \
        #     #        "d=&pppStatus=0&agentName="
        #
        #     URL = url1 + str(self.i) + url3
        #     print(self.i)
        #     yield scrapy.Request(URL, callback=self.parse)
        # self.i += 1





            # # if tit.find('海关') = -1
            # else:
            # item['title'] = tit[0]
            # url = 'http://www.ccgp.gov.cn/cggg/dfgg' + url[0].replace('.','',1)
        #
        #         item['url'] = url
        #         yield item
        # url1 = 'http://www.ccgp.gov.cn/cggg/dfgg/index_'
        # url2 = '.htm'
        # for page in range(2,24):
        #     url3 = url1 + str(page) + url2
        #     yield scrapy.Request(url3,callback=self.parse)