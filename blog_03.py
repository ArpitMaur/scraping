# ----------------------scrapping blog titles from archanaskitchen.com/")-----------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.archanaskitchen.com/")
    

    topics = await page.querySelectorAll("#content-area > div > div > div > div > div > a > h3 > span")

    
    for topic in topics:
        title = await topic.getProperty("textContent")
        title=(await title.jsonValue())
        print(title)

    await browser.close()

print('searching.............')
asyncio.get_event_loop().run_until_complete(main())
print('end..........')