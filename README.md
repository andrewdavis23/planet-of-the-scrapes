# planet-of-the-scrapes
Webscrapes using Python module Scrapy

# Readme

Install module into [virtual enviornment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv).  This is recommended by the [creators of scrapy](https://docs.scrapy.org/en/latest/):
> Instead, we recommend that you install Scrapy within a so-called “virtual environment” (venv). Virtual environments allow you to not conflict with already-installed Python > system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).
> Also, failure to import the installed scrapy module is common. A virtual environment is a solution.

1. Navigate to the location where you want your virtual environment. I call my scrapYard
2. Create the virutal environment. 

```cmd
python3 -m venv C:\Users\nuajd15\Documents\scrapers\scrapYard
```

3. Change environment path to new location. In VS Code: CTRL + SHIFT + P, type "Python: Select Interpretor". Navigate to virtual environment folder (scrapYard > Scripts > python.exe).

4. Install scrapy to environment library. For some reason, I had to force pip to install to virtual environment.

```cmd 
pip install --target=C:\Users\nuajd15\Documents\scrapers\scrapYard\Lib\site-packages scrapy
```
5. To verify the package is installed go to the interpreter (virtual environment > Scripts > python.exe).  View scrapy or all modules:

```cmd
>>> help("scrapy")
>>> help("modules")
```

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
