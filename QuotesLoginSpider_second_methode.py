import scrapy


class QuotesLoginSpider(scrapy.Spider):
    name = 'quotes-login'
    login_url = 'http://quotes.toscrape.com/login'
    start_urls = [login_url]

    def parse(self, response):
        return scrapy.FormRequest.from_response(
            response,
            formdata = {
                'usename': 'abc',
                'password' : 'abc'
            },
            callback  = self.parse_quotes
        )

    def parse_quotes(self, response):
        """Parse the main page after the spider is logged in"""
        for q in response.css('div.quote'):
            yield {
                'author_name': q.css('small.author::text').extract_first(),
                'author_url': q.css(
                    'small.author ~ a[href*="goodreads.com"]::attr(href)'
                ).extract_first()
            }