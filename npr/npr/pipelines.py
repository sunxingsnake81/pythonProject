# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.files import FilesPipeline
from urllib.parse  import urlparse
from scrapy import Request
# from npr.items import NprItem
import os




class NprPipeline(FilesPipeline):
    print('调用nprpipeline类')




    def file_path(self, request, response=None, info=None, *, item=None):
        print('调用file_path')
        print('files/' + os.path.basename(urlparse(request.url).path))
        return 'files/' + os.path.basename(urlparse(request.url).path)
    # # DEFAULT_FILES_URLS_FIELD = 'file_urls'
    # # DEFAULT_FILES_RESULT_FIELD = 'files'
    # def file_downloaded(self, response, request, info, *, item=None):
    #     def md5sum(file):
    #         """Calculate the md5 checksum of a file-like object without reading its
    #         whole content in memory.
    #
    #         >>> from io import BytesIO
    #         >>> md5sum(BytesIO(b'file content to hash'))
    #         '784406af91dd5a54fbb9c84c2236595a'
    #         """
    #         m = hashlib.md5()
    #         while True:
    #             d = file.read(8096)
    #             if not d:
    #                 break
    #             m.update(d)
    #         return m.hexdigest()
    #     print('调用file_downloaded')
    #     buf = BytesIO(response.body)
    #     checksum = md5sum(buf)
    #     return checksum



    # def file_path(self, request, response=None, info=None, *, item=None):
    #     print('调用子函数')
    #     media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
    #     # media_guid = os.path.split(urlparse(request.url).path)[1]
    #     media_ext = os.path.splitext(request.url)[1]
    #     # Handles empty and wild extensions by trying to guess the
    #     # mime type then extension or default to empty string otherwise
    #     if media_ext not in mimetypes.types_map:
    #         media_ext = ''
    #         media_type = mimetypes.guess_type(request.url)[0]
    #         if media_type:
    #             media_ext = mimetypes.guess_extension(media_type)
    #     return f'full/{media_guid}{media_ext}'

    # def get_media_requests(self, item, info):
    #     print(file_name + 'is on line')
    #     for file_url, file_name in zip(item['file_urls'], item['file_name']):
    #         yield scrapy.Request(file_url, meta={'file_name': file_name})

        # def file_path(self, request, response=None, info=None):
        #
        #
        #     file_name = request.meta['file_name']
        #     return 'full/%s' % (file_name)
    # def get_media_requests(self, item, info):
    #     urls = ItemAdapter(item).get(self.files_urls_field, [])
    #     return [Request(u) for u in urls]
    # def file_path(self, request, response=None, info=None, *, item=None):
    #     media_guid = hashlib.sha1(to_bytes(request.url)).hexdigest()
    #     media_ext = os.path.splitext(request.url)[1]
    #     # Handles empty and wild extensions by trying to guess the
    #     # mime type then extension or default to empty string otherwise
    #     if media_ext not in mimetypes.types_map:
    #         media_ext = ''
    #         media_type = mimetypes.guess_type(request.url)[0]
    #         if media_type:
    #             media_ext = mimetypes.guess_extension(media_type)
    #     return f'full/{media_guid}{media_ext}'
    # # def get_media_requests(self, item, info):
    # #     urls = ItemAdapter(item).get(self.files_urls_field, [])
    # #     return [Request(u) for u in urls]
    #
    #
    # # def get_media_requests(self, item, info):
    # #     print('this is  test')
    # #     print(item['file_urls'])
    # #     # for file_urls in item['file_urls']:
    # #     #     yield scrapy.Request(file_urls, meta={'item': item})
    # # def file_path(self, request, response=None, info=None, *, item=None):
    # #
    # #     # print('pipeline is ok')
    # #     print(os.path.split(urlparse(request.url).path)
    # #     # item = request.meta['item']
    #     # filename = os.path.split(urlparse(request.url).path)[1]
    #     # filext = os.path.splitext(urlparse(request.url).path)[1]
    #     # filename = urlparse(request.url).path
    #
    #     # print(filename)
    #     # print(filext)
    #     return 'full/%s%s' % (filename,filext)
    #     # return
    #
    # # def get_media_requests(self,item,info):
    #

    #     file_url = item['url']
    #     yield Request(file_url,meta=item)
    # def file_path(self,request,response=None,info=None):
    #     meta = request.meta
    #     file_path = meta.get('file_paths')
    #
    # def process_item(self, item, spider):

    #     return item
class txtPipeline(object):
    fp = None
    # def open_spider(self, spider):
    #     # print('开始爬虫')
    #     # print('files/'+ os.path.basename(urlparse(request.url).path) )
    #     print(item['file_name'])
    #     self.fp = open('files/' + os.path.basename(urlparse(request.url).path).split('.')[0], 'w', encoding='utf-8')

    def process_item(self, item, spider):
        '''
        处理Item
        :param item:
        :param spider:
        :return:
        '''
        delstr = ['<','>','|','*','?','\\','\"',':']
        for i in delstr:
            item['file_name'] = item['file_name'].replace(i,'')

        self.fp = open('files/' + item['file_name']+ '.txt', 'w', encoding='utf-8')
        self.fp.write(item['file_script'])
        # print(item['author'], item['content'])
        return item

    def close_spider(self, spider):
        print('爬虫结束')
        self.fp.close()




