# PLANET OF THE SCRAPES
## Repository Directory 🙈 🙉 🗽 🙊

## Notes
   - [Intro to Webscraping](notes-datacamp-scrapy-intro.md)
   - [Other Notes](notes-other.md)

## Web Scrapers
   - [DataCamp courses example](dc-courses-crawler)
   - [Mutual Funds](https://github.com/andrewdavis23/boomer-eggs)

## How to Install Scrapy

Install module into [virtual enviornment](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#installing-virtualenv).  This is recommended by the [creators of scrapy](https://docs.scrapy.org/en/latest/):
> Instead, we recommend that you install Scrapy within a so-called “virtual environment” (venv). Virtual environments allow you to not conflict with already-installed Python > system packages (which could break some of your system tools and scripts), and still install packages normally with pip (without sudo and the likes).
> Also, failure to import the installed scrapy module is common. A virtual environment is a solution.

1. Navigate to the location where you want your virtual environment. I call mine scrapYard.
2. Create the virutal environment. 

```cmd
python3 -m venv C:\Python Projects\scrapYard
```

3. Change environment path to new location. In VS Code: CTRL + SHIFT + P, type "Python: Select Interpretor". Navigate to virtual environment folder (scrapYard > Scripts > python.exe).

4. Install scrapy to environment library. The target is where pip will install the virtual environment.

```cmd 
pip install --target=C:\Python Projects\scrapYard\Programs\scrapYard\Lib\site-packages> scrapy
```
5. To verify the package is installed go to the interpreter (virtual environment > Scripts > python.exe).  View scrapy or all modules:

```cmd
>>> help("scrapy")
>>> help("modules")
```



