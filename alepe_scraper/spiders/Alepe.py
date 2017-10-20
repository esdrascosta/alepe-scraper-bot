# -*- coding: utf-8 -*-
import scrapy


class AlepeSpider(scrapy.Spider):
    name = 'alepe'
    allowed_domains = ['http://www.alepe.pe.gov.br/transparencia-vi/']
    start_urls = ['http://www.alepe.pe.gov.br/transparencia-vi/']

    def parse(self, response):

	#parliamentarians
	for par in response.css("select[name=dep] > option")[1:]:
		
		par_code = par.css("::attr(value)").extract()
		par_name = par.css("::text").extract()
		
		for year in [ 2015, 2016, 2017 ] :
			for month in range(1, 13):

				url = "?dep=%s&ano=%s&mes=%s" % (par_code, year, month)
				next_url = response.urljoin(url)
				next_request = scrapy.Request(next_url, callback=self.parse_par)
				next_request.meta['par_name'] = par_name
				next_request.meta['year'] = year
				next_request.meta['month'] = month
				yield next_request

    def parse_par(self, response):
        pass
		
#		par_name = next_request.meta['par_name']
#       year     = next_request.meta['year']
#       month    = next_request.meta['month']
#       grant_declared = response.css("div#div-com-verba > div.search-result-resume")		

#		if grant_declared:
			
#			order = response.css("div#div-com-verba > div.row > h2::text").extract_first()
#			for item in response.css("div#div-com-verba > div.accordion"):
				
			
			
				
		

		
	


