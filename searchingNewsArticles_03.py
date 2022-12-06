# ----------------------scrapping news titles from timesofindia by given links---------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://timesofindia.indiatimes.com/mostshared.cms")
    
    await page.waitFor(4000)
    topics = await page.querySelectorAll("#itemContainer > li > span > strong")
    
    for topic in topics:
        title = await topic.getProperty("textContent")
        print(await title.jsonValue())
        
    await browser.close()

print('searching.............')
asyncio.get_event_loop().run_until_complete(main())
print('end..........')