import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://en.wikipedia.org/wiki/Main_Page")
    
    await page.type('[id=searchInput]',keyword)
    await page.screenshot({"path": "main_page.png"})
    
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    await page.screenshot({"path": "result.png"})
    
    data= await page.evaluate('''
        ()=>  {                    
            contents=document.querySelectorAll('.mw-parser-output p')[1] 
            ps=contents.innerHTML
            return ps
        }
    ''')
    allData=''.join(data)
    
    soup=BeautifulSoup(allData,'html.parser')
    text=soup.get_text().strip()
    print(text)
    await browser.close()

keyword=input('Enter the text want to search: ')
print('searching.............')
asyncio.get_event_loop().run_until_complete(main(keyword))
print('ending................')