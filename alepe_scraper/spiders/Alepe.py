# -*- coding: utf-8 -*-
import scrapy


class AlepeSpider(scrapy.Spider):
    name = 'alepe'
    allowed_domains = ['www.alepe.pe.gov.br']
    start_urls = ['http://www.alepe.pe.gov.br/transparencia-vi/']

    def parse(self, response):

        # parliamentarians
        for par in response.css("select[name=dep] > option")[1:]:

            par_code = par.css("::attr(value)").extract_first()
            par_name = par.css("::text").extract_first()

            # TODO year and month must be dynamic
            for year in [2017]:
                for month in range(1, 13):
                    url = "?dep=%s&ano=%s&mes=%s" % (str(par_code), year, month)
                    next_url = response.urljoin(url)
                    next_request = scrapy.Request(url=next_url, callback=self.parse_par, encoding='utf8')
                    next_request.meta['par_name'] = par_name
                    next_request.meta['year'] = year
                    next_request.meta['month'] = month
                    yield next_request

    def parse_par(self, response):
        grant_declared = response.css("div#div-com-verba div.search-result-resume")

        if grant_declared:
            order = response.css("div#div-com-verba div.row h2::text").extract_first()
            for item in response.css("div#div-com-verba div.accordion"):
                expense_type = item.css("h4::text").extract()[1]
                for expense in item.css("table tbody"):
                    expense_itens = expense.css("td::text")

                    yield {
                        "par_name": response.meta['par_name'],
                        "year": response.meta['year'],
                        "month": response.meta['month'],
                        "order": order,
                        "expense_type": expense_type,
                        "date": expense_itens[0].extract(),
                        "cnpj": expense_itens[1].extract(),
                        "company": expense_itens[2].extract(),
                        "value": float(expense_itens[3].extract().replace(".", "").replace(",", "."))
                    }
