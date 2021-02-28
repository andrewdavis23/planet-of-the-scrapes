# planet-of-the-scrapes
Webscrapes using Python module Scrapy

## Readme

Install module into [virtual enviornment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/).  This is recommended by the [creators of scrapy](https://docs.scrapy.org/en/latest/):
> Instead, we recommend that you install Scrapy within a so-called “virtual environment” (venv). Virtual environments allow you to not conflict with already-installed Python > system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).
> Also, failure to import the installed scrapy module is common. A virtual environment is a solution.

1. Navigate to the location where you want your virtual environment.
2. Create the virutal environment. 

```cmd
$ python3 -m venv scrapYard-env
```

3. Change environment path to new location. In VS Code: CTRL + SHIFT + P, type "Python: Select Interpretor". Navigate to virtual environment, select PYTHON.EXE.
4. Install scrapy to environment library (not working) 

```cmd
$ pip install scrapy
```


## Notes from [DataCamp course](https://learn.datacamp.com/courses/web-scraping-with-python):

HTML structures - Consider it like a pedagogy - Below, references will be made to "parents" and "children" - Cats and dogs, pending next update.

```html
<html>
  <body>
    <span>
      Content.
    </span>
    <div>
      More content.
    </div>
    <div>
      TARGET
    </div>
  </body>
</html>
```
```python
xpath = 'html/body/div[2]'
xpath.extract()
'TARGET'
```
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
