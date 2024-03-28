import scrapy


class PythonTutorialSpider(scrapy.Spider):
    # name = 'python_tutorial'
    # start_urls = [
    #     'https://docs.python.org/3/tutorial/index.html',
    # ]
    #
    # def parse(self, response):
    #     for title in response.css('div.toctree-wrapper li.toctree-l1 > a::text').getall():
    #         yield {'title': title.strip()}
    name = 'python_tutorial'
    ##allowed_domains 是一个列表,用于限定爬虫只能爬取指定域名下的页面。
    allowed_domains = ['douban.com']
    ##start_urls = ['https://movie.douban.com/top250']
    start_urls = ['https://movie.douban.com/top250']

##这是爬虫的一个方法,它会被调用来处理每个请求的响应。
    def parse(self, response):
        for movie in response.css('.item'):
            yield {
                'title': movie.css('.title::text').get(),
            }
        ##这行代码尝试找到"下一页"的链接。
        next_page = response.css('.next a::attr(href)').get()
        ##这部分代码处理分页。
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)