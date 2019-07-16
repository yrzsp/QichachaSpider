# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class QichachaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # name = scrapy.Field()
    # age = scrapy.Field()
    qiye_name = scrapy.Field() # 企业名称
    registered_capital = scrapy.Field() # 注册资本
    real_capital = scrapy.Field() # 实缴资本
    # 经营状态
    # 成立日期
    # 统一社会信用代码
    # 纳税人识别号
    # 注册号
    # 组织机构代码
    # 企业类型
    # 所属行业
