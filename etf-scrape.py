import urllib.request
import scrapy
import pandas as pd
import concurrent.futures
import re
from datetime import datetime

start_time = datetime.now()

etfs_path = "C:/Python Programs/ETF Scraper/etfs.txt"
df = pd.DataFrame()
        
# Returns the selector object that xpaths will extract from
def create_selector(url):
    # get web page using fake user agent
    req = urllib.request.Request(url=url, headers={'User-Agent': 'Mozilla/5.0'})
    fp = urllib.request.urlopen(req)
    mybytes = fp.read()

    # decode
    html = mybytes.decode("utf8")
    fp.close()

    # create selector object
    sel = scrapy.Selector(text=html)
    return sel    

# Function to scrape a single URL
def scrape_summary(ticker):
    url = "https://finance.yahoo.com/quote/"+ticker

    path = '//td//text()'
    sel = create_selector(url)
    extract = sel.xpath(path).extract()

    temp_dict = {extract[i]: extract[i+1] for i in range(0, len(extract), 2)}

    return temp_dict

def scrape_profile(ticker):
    url = "https://finance.yahoo.com/quote/"+ticker+"/profile?p="+ticker

    path = '//span/text()'
    sel = create_selector(url)
    extract = sel.xpath(path).extract()

    start = extract.index('Fund Overview') + 1
    end = extract.index('Fund Operations')
    table = extract[start:end]
    temp_dict = {table[i]: table[i+1] for i in range(0, len(table), 2)}

    start = extract.index('Fund Operations') + 4
    end = extract.index('Total Net Assets') + 3
    table = extract[start:end]

    temp_dict.update( {table[i]+'_ETF': table[i+1] for i in range(0, len(table), 3)} )
    temp_dict.update( {table[i]+'_CAT': table[i+2] for i in range(0, len(table), 3)} )

    return temp_dict

def scrape_performance(ticker):
    url = "https://finance.yahoo.com/quote/"+ticker+"/performance?p="+ticker

    path = '//span/text()'
    sel = create_selector(url)
    extract = sel.xpath(path).extract()

    start = extract.index('Performance Overview') + 1
    end  = extract.index('Trailing Returns (%) Vs. Benchmarks')
    table = extract[start:end]
    temp_dict = {table[i+1] : table[i] for i in range(0, len(table), 2)}

    start  = extract.index('Trailing Returns (%) Vs. Benchmarks') + 4
    end  = extract.index('Annual Total Return (%) History')
    table = extract[start:end]
    temp_dict.update( {table[i]+'_ETF' : table[i+1] for i in range(0, len(table), 3)} )
    temp_dict.update( {table[i]+'_CAT' : table[i+2] for i in range(0, len(table), 3)} )

    return temp_dict

# Function to process a single URL and store the result
def process_url(ticker):
    global df
    print("Processing {}".format(ticker))

    temp_dict = scrape_summary(ticker)
    temp_dict.update( scrape_profile(ticker) )
    temp_dict.update( scrape_performance(ticker) )
    temp_df = pd.DataFrame([temp_dict], index=[ticker])
    df = pd.concat([df, temp_df])

# Function to read URLs from a text file
def text_to_list(file_path):
    with open(file_path, 'r') as file:
        urls = file.readlines()
    return [url.strip() for url in urls]

if __name__ == '__main__':
    # Read URLs from a text file
    ticker_list = text_to_list(etfs_path)
    print("Ticker list loaded")

    # Create a thread pool executor
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # Submit the scraping tasks to the executor
        futures = [executor.submit(process_url, ticker) for ticker in ticker_list]

        # Wait for all tasks to complete
        concurrent.futures.wait(futures)

    print("Finished {}".format(datetime.now() - start_time))
    df.to_csv('C:/Python Programs/ETF Scraper/output.csv', index=True)
    print(df.head())
