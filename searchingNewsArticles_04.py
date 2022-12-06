# ----------------------scrapping news titles from indianexpress.com by keywords---------------------------

import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://indianexpress.com/")
    
    await page.click('#wrapper > header > div.t-headlink > div.section_nav > div.topsocial > a > i')

    await page.type('[id=search]',keyword)
    await page.keyboard.press('Enter')
    await page.waitForNavigation()

 
    topics = await page.querySelectorAll("#section > div > div > div.leftpanel > div.search-result > div > h3")
    
    for topic in topics:
        title = await topic.getProperty("textContent")
        print(await title.jsonValue())
    
    await browser.close()

print('searching.............')
keyword=input('Enter the keyword want to search: ')
asyncio.get_event_loop().run_until_complete(main(keyword))
print('end..........')