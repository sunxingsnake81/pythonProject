# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
from openpyxl import Workbook

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class CgwPipeline:
    def __init__(self):
        self.wb = Workbook()
        self.ws = self.wb.active
        self.ws.append(['title', 'url','time','cust','prox'])
    def process_item(self, item, spider):
        line = [item['title'], item['url'],item['time'],item['cust'],item['prox']]
        self.ws.append(line)
        self.wb.save('zbml.xlsx')

        return item
