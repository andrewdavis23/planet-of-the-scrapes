# Notes from [DataCamp course](https://learn.datacamp.com/courses/web-scraping-with-python):

HTML structures - Consider it a family tree - Below, references will be made to "parents" and "children" - Cats and dogs, pending next update.

## HTML Tree Examples
```html
<html>
  <body>
    <p>
      Introductory content.
    </p
    <span>
      <div class="nephew">
        <p>
          Content.
        </p>
        <p>
          More content.
        </p>
      </div>
      <div>
      </div class="neice">
    </span>
    <div class="uncle">
      <p>
        This content.
      </p>
      <p>
        That content.
      </p>
    </div>
    <div class="aunt">
      Important content.
    </div>
  </body>
</html>
```
Get second div-child of body.
```python
xpath = 'html/body/div[2]'
xpath.extract()
'Important content.'
```
Get every paragraph that is a first child.
```python
xpath = '//p[1]'
xpath.extract()
['Content.','This content.']

```
## More Xpath Syntax

All table elements within the HTML code
```python
xpath = '//table'
```
All tables in the 2nd div child
```python
xpath = 'html/body/div[2]//table'
```
All span elements where the class attribute is set to "some-class"
```python
xpath = '//span[@class = "some-class"]'
```
one generation:
```python
xpath = 'parent/*'
```
all future generations:
```python
xpath = 'parent//*'
```
All elements in code where id="uid"
```
xpath = '//*[@id="uid"]'
```
Get all classes containing the string "class-1" this includes "class-1 class-2" and "class-12"
```python
xpath = '//*[contains(@class,"class-1")'
```
Get all URLs from HTML code
```python
xpath = '//a/@href'
```

## Scrapy selector

```python
import urllib.request
import scrapy

# get webpage
fp = urllib.request.urlopen("http://www.python.org")
mybytes = fp.read()

# decode
html = mybytes.decode("utf8")
fp.close()

# create selector object
sel = scrappy.Selector(text=html)

# extract the CSS body containing the news headlines
trees = sel.xpath('//*[contains(@role,"treeitem")]').extract()

print(trees[0:2])
```

## CSS
```python
# Create the XPath string equivalent to the CSS Locator 
xpath = '/html/body/span[1]//a'

# Create the CSS Locator string equivalent to the XPath
css_locator = html > body > span:nth-of-type(1) a
```
```python
# Create the XPath string equivalent to the CSS Locator 
xpath = '//div[@id="uid"]/span//h4'

# Create the CSS Locator string equivalent to the XPath
css_locator = 'div#uid > span h4'
```
```python
# Create the CSS Locator to all children of the element whose id is uid
css_locator = '#uid > *'
```
```python
# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]/text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3::text'

# Print the text from our selections
print_results( xpath, css_locator )
```
```python
# Create an XPath string to the desired text.
xpath = '//p[@id="p3"]//text()'

# Create a CSS Locator string to the desired text.
css_locator = 'p#p3 ::text'

# Print the text from our selections
print_results( xpath, css_locator )
```
A useful difference:
```python
css = 'html > body > div#uid > p.class1'
xp1 = '/html/body/div[@id="uid"]/p[contains(@class,"class1")]'
xp2 = '/html/body/div[@id="uid"]/p[@class = "class1"]'
```
|css|xp1|xp2|
|---|---|---|
| + class="**class 1**"| + class="<ins>class 1</ins> class2"| + class="<ins>class 1</ins>"|
| + class="**class 1** class2"| + class="<ins>class 1</ins> class2"| x class="class 1 class2"|
| x class="class 12"| + class="<ins>class 1</ins>2"| x class="class12"|

## Response vs. Selector
same thang, except response keeps track of the URL used:
```python
response.url
>>> 'http://www.DataCamp.com/courses/all'
# next_url is the string path of the next URL we want to scrape
response.follow(next_url)
```

## Basic Crawler - [source](https://campus.datacamp.com/courses/web-scraping-with-python/spiders?ex=11)
This example downloads creates a dictionary where keys are course names and each value is a list of chapters. You can copy and run this code.
```python
# import pets
web = chr(128376)
spider = chr(128375)

# url
url_short = 'https://assets.datacamp.com/production/repositories/2560/datasets/19a0a26daa8d9db1d920b5d5607c19d6d8094b3b/all_short'

# Import scrapy
import scrapy

# Import the CrawlerProcess
from scrapy.crawler import CrawlerProcess

# Create the Spider class
class YourSpider(scrapy.Spider):
  name = 'yourspider'
  # start_requests method
  def start_requests( self ):
    yield scrapy.Request(url = url_short, callback = self.parse)
      
  def parse(self, response):
    # My version of the parser you wrote in the previous part
    crs_titles = response.xpath('//h4[contains(@class,"block__title")]/text()').extract()
    crs_descrs = response.xpath('//p[contains(@class,"block__description")]/text()').extract()
    for crs_title, crs_descr in zip( crs_titles, crs_descrs ):
      dc_dict[crs_title] = crs_descr
    
# Initialize the dictionary **outside** of the Spider class
dc_dict = dict()

# Run the Spider
process = CrawlerProcess()
process.crawl(YourSpider)
process.start()

# Print a preview of courses

print( (' {} {}  '.format(web,spider))*10 )
print('Dictionary:')
for i in dc_dict:
    print('{}:'.format(i),dc_dict[i])
```
