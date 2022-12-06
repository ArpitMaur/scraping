# --------------------scrapping news Articles form indiatoday.in by searching keywords-----
import asyncio
from bs4 import BeautifulSoup
from pyppeteer import launch

async def main(keyword):
    browser = await launch()
    page = await browser.newPage()
    await page.goto("https://www.indiatoday.in/")
    
    await page.click('#__next > header > div > div.jsx-da955aab8836061b.nav__section > div.jsx-da955aab8836061b.rhs__menu > div.jsx-da955aab8836061b.srchclose__icon > svg.jsx-da955aab8836061b.search__icon')
    
    await page.type('[class=Search_grpsrchbox__d1_jR]',keyword)
    
    await page.keyboard.press('Enter')
    await page.waitForNavigation()
    # await page.screenshot({"path": "main_page.png"})
    # # await page.screenshot({"path": "result.png"})
    

    
    data= await page.evaluate('''
        ()=>  {                    
            contents=document.querySelectorAll('.B1S3_story__card__A_fhi')
            ps=Array.from(contents).map((para)=>para.innerHTML)
            return ps
        }
    ''')
    # print(data)
    allData=''.join(data)
    
    soup=BeautifulSoup(allData,'html.parser')
    print(soup.prettify())
    for d in soup.find_all('div',class_='B1S3_content__wrap__9mSB6'):
        title=d.find('a')
        print(title.string)

    await browser.close()

print('searching.............')
keyword=input('Enter the keyword want to search: ')
asyncio.get_event_loop().run_until_complete(main(keyword))
print('end..........')