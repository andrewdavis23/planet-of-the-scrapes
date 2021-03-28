import urllib.request
import scrapy
import pandas

# Returns the selector object that xpaths will extract from
def create_selector(url):
    # get web page
    fp = urllib.request.urlopen(url)

    # decode
    html = mybytes.decode("utf8")
    fp.close()

    # create selector object
    sel = scrapy.Selector(text=html)

# List webpages
url = "https://finance.yahoo.com/quote/FCNTX/purchase-info?p=FCNTX"

# extract the data points
min_int = sel.xpath('//span[contains(@class,"Fl(end)") and contains(@data-reactid,"12")]').extract()
min_sub = sel.xpath('//span[contains(@class,"Fl(end)") and contains(@data-reactid,"28")]').extract()
min_int_ira = sel.xpath('//span[contains(@class,"Fl(end)") and contains(@data-reactid,"17")]').extract()
min_sub_ira = sel.xpath('//span[contains(@class,"Fl(end)") and contains(@data-reactid,"33")]').extract()

print(min_int,min_int_ira,min_sub,min_sub_ira)
