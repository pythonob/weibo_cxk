# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
import json
from ..items import RredisItem


class WeiboSpider(RedisSpider):
    name = 'weibo'
    allowed_domains = ['weibo.cn']
    redis_key = "weibo:start_url"

    def parse(self, response):
        base_url = 'https://m.weibo.cn/api/statuses/repostTimeline?id=4363605740515964&page='
        for i in range(10000, 0, -1):

            yield scrapy.Request(url=base_url+str(i), callback=self.get_forward)

    def get_forward(self, response):
        print(111)
        item = RredisItem()
        data = json.loads(response.text)
        inner_data = data["data"]
        success = inner_data.get('data') # 返回一个列表
        if success:
            inner_data = inner_data["data"]
            for one_forward in inner_data:
                item['fwd_text'] = one_forward["raw_text"]
                item['device'] = one_forward["source"]
                item['u_id'] = one_forward["user"]["id"]
                item['u_name'] = one_forward["user"]["screen_name"]
                item['gender'] = one_forward["user"]["gender"]
                item['follows'] = one_forward["user"]["follow_count"]
                item['followers'] = one_forward["user"]["followers_count"]
                item['desc'] = one_forward["user"]["description"]
                item["fwd_id"] = one_forward["id"]
                yield item
