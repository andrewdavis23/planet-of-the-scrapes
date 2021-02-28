# planet-of-the-scrapes
Webscrapes using Python module Scrapy

## Readme

Install module into virtual enviornment.  This is recommended by the creators because their module can interfere with other modules.
Also, failure to import the installed scrapy module is common. A virtual environment is a solution.

> # Navigate to the location where you want your virtual environment
> python3 -m venv scrapYard-env
> 
> # Change environment path to new location.
> 
> # Install scrapy to environment library (not working)
> pip install scrapy




## Notes from DataCamp course:

HTML structures - Consider it like a pedagogy - Below, references will be made to "parents" and "children" - Cats and dogs, pending next update.

'''
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
'''

> xpath = 'html/body/div[2]'
> xpath.extract()
> 'TARGET'

All table elements within the HTML code
> xpath = '//table'

All tables in the 2nd div child
> xpath = 'html/body/div[2]//table'

All <span> elements where the class attribute is set to "some-class"
> xpath = '//span[@class = "some-class"]'

one generation:
> xpath = 'parent/*'

all future generations:
> xpath = 'parent//*'

All elements in code where id="uid"
> xpath = '//*[@id="uid"]'
