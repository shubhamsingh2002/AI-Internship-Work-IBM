import scrapy
from urllib.parse import urljoin
import csv
import os

class EciSpider(scrapy.Spider):
    name='adit'
    allowed_domains= ['results.eci.gov.in']
    start_urls =['https://results.eci.gov.in/PcResultGenJune2024/index.htm']
    count=0
    custom_settings ={
        'DOWLOAD_DELAY': 1
    }
    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse, dont_filter=True)

    def parse(self,response):
        party_urls = response.xpath('//table[@class="table"]/tbody/tr/td[2]/a/@href').getall()

        for party_url in party_urls:
            absoulte_party_url = urljoin(response.url,party_url)
            yield scrapy.Request(absoulte_party_url,callback=self.parse_constituency,dont_filter=True)


    def parse_constituency(self,response):
        constituency_urls = response.xpath('//table[@class="table table-striped table-bordered"]/tbody/tr/td[2]/a/@href').getall()

        for party_url in constituency_urls:
            absoulte_constituency_url = urljoin(response.url,party_url)
            yield scrapy.Request(absoulte_constituency_url,callback=self.parse_candidate,dont_filter=True)

    def parse_candidate(self,response):


        finalData = {}
        self.count +=1

        finalData['ref'] = str(self.count)
        finalData['wonstatus']=response.xpath('//div[@class="cand-info"]/div/div[1]/text()').get(default='').strip()
        finalData['totalvotes']=response.xpath('//div[@class="cand-info"]/div/div[2]/text()').get(default='').strip()
        finalData['winvotes']=response.xpath('//div[@class="cand-box"]/div/div/div[2]/span/text()').get(default='').strip()
        finalData['name']=response.xpath('//div[@class="cand-box"]/div/div[2]/h5/text()').get(default='').strip()
        finalData['partyname']=response.xpath('//div[@class="cand-box"]/div/div[2]/h6/text()').get(default='').strip()

        file_exists = os.path.isfile('final.csv')


        with open('final.csv', mode='a', newline='') as csv_file:
            fieldnames = ['ref', 'wonstatus', 'totalvotes', 'winvotes', 'name', 'partyname']
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

            if not file_exists or csv_file.tell() == 0:
                writer.writeheader()

            writer.writerow(finalData)

        yield finalData       
                