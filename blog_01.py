# ----------------------scrapping blog titles from codewithharry.com/blog/ first page scrapping -----------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.codewithharry.com/blog/")
    

    topics = await page.querySelectorAll("#__next > div > div> div > div > div > div > div > div > div.mt-2 > span")
    
    for topic in topics:
        title = await topic.getProperty("textContent")
        print(await title.jsonValue())
        
    await browser.close()

print('searching.............')
asyncio.get_event_loop().run_until_complete(main())
print('end..........')