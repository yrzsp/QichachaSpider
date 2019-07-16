#-*-coding:utf-8 -*-

import scrapy
from urllib import parse
from qichacha.items import QichachaItem


class QichachaSpider(scrapy.Spider):
    name = "qichacha_spider"
    # name = 'hunan_tender_t_spider'
    # allowed_domains = ['https://www.qichacha.com/']
    def start_requests(self):
        search_key = ['小米']
        for key in search_key:
            start_url = "https://www.qichacha.com/search?key=" + parse.quote(key)
            # print(start_url,"***********************************")
            yield scrapy.Request(start_url, callback=self.parse, dont_filter=True)

    def parse(self, response):
        header = {
            'Referer': None,
        }
        origin_urls = response.xpath('//tbody[@id="search-result"]/tr/td/a/@href').extract()
        print(origin_urls)
        for origin_url in origin_urls:
            request_url = parse.urljoin("https://www.qichacha.com",origin_url)
            print(request_url)
            yield scrapy.Request(request_url, headers=header, callback=self.detail_parse, dont_filter=True)

    def detail_parse(self, response):
        items = QichachaItem()
        trs = response.xpath("//section[@id='Cominfo']/table[2]/tr")
        items['qiye_name'] = response.xpath("//*[@id='company-top']/div[2]/div[2]/div[1]/h1/text()").extract()
        print(items['qiye_name'])
        qiye_info = []
        for i in range(len(trs)-2):
            qiye_info.append(''.join(trs[i].xpath(".//td[2]/text()").extract()).replace('\n', '').strip())
            qiye_info.append(''.join(trs[i].xpath(".//td[4]/text()").extract()).replace('\n', '').strip())
        qiye_info.append(''.join(trs[-2].xpath(".//td[2]/text()").extract()).replace('\n', '').strip())
        qiye_info.append(''.join(trs[-1].xpath(".//td[2]/text()").extract()).replace('\n', '').strip())
        print(qiye_info)
        items['registered_capital'] = qiye_info[0]
        items['real_capital'] = qiye_info[1]
        yield items
        # print(response.xpath("//section[@id='Cominfo']/table[2]/tr/[{}]td[1]|td[2]}").extract()[0])