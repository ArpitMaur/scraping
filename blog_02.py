# ----------------------scrapping blog titles from shoutmeloud.com/blog -----------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main():
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.shoutmeloud.com/blog")
    

    topics = await page.querySelectorAll("div > div > header > h2")

    
    for topic in topics:
        title = await topic.getProperty("textContent")
        title=(await title.jsonValue())
        print(title)

    await browser.close()

print('searching.............')
asyncio.get_event_loop().run_until_complete(main())
print('end..........')