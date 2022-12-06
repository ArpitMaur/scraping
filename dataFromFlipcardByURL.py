import requests
from bs4 import BeautifulSoup

url="https://www.flipkart.com/computers/monitors/pr?sid=6bo%2C9no&fm=neo%2Fmerchandising&iid=M_ce1a6f68-d7d2-4ae1-875c-0d0877d9a11f_2_372UD5BXDFYS_MC.ECL5SFI77NSY&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L2_view-all&cid=ECL5SFI77NSY&p%5B%5D=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p%5B%5D=facets.brand%255B%255D%3DSAMSUNG&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InZhbHVlQ2FsbG91dCI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ2YWx1ZUNhbGxvdXQiLCJpbmZlcmVuY2VUeXBlIjoiVkFMVUVfQ0FMTE9VVCIsInZhbHVlcyI6WyJGcm9tIOKCuTk5OTkiXSwidmFsdWVUeXBlIjoiTVVMVElfVkFMVUVEIn19LCJ0aXRsZSI6eyJtdWx0aVZhbHVlZEF0dHJpYnV0ZSI6eyJrZXkiOiJ0aXRsZSIsImluZmVyZW5jZVR5cGUiOiJUSVRMRSIsInZhbHVlcyI6WyJNb25pdG9ycyJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX0sImhlcm9QaWQiOnsic2luZ2xlVmFsdWVBdHRyaWJ1dGUiOnsia2V5IjoiaGVyb1BpZCIsImluZmVyZW5jZVR5cGUiOiJQSUQiLCJ2YWx1ZSI6Ik1PTkZZR0dBQ0tTSlg0TVMiLCJ2YWx1ZVR5cGUiOiJTSU5HTEVfVkFMVUVEIn19fX19&fm=neo%2Fmerchandising&iid=M_f578cd35-a232-456b-a165-96592ee11e79_3.W52Y6O5JCN9E&ppt=browse&ppn=browse&ssid=t27mbnn6e80000001670004283745&otracker=hp_omu_Best%2Bof%2BElectronics_3_3.dealCard.OMU_W52Y6O5JCN9E_3&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Best%2Bof%2BElectronics_NA_dealCard_cc_3_NA_view-all_3&cid=W52Y6O5JCN9E"
# url="https://www.flipkart.com/air-conditioners/pr?sid=j9e,abm,c54&p[]=facets.fulfilled_by%255B%255D%3DFlipkart%2BAssured&p[]=facets.brand%255B%255D%3DLG&p[]=facets.serviceability%5B%5D%3Dtrue&otracker=categorytree&otracker=nmenu_sub_TVs%20%26%20Appliances_0_LG"
res=requests.get(url)
htmlContent=res.content
soup=BeautifulSoup(htmlContent,'html.parser')


for d in soup.find_all('div',class_='_1AtVbE col-12-12'):
    titel=d.find('div',class_='_4rR01T')
    # titel=d.find('div',attrs={'class':'_4rR01T'})
    price=d.find('div',class_='_30jeq3 _1_WHN1')
    
    if str(titel) != 'None':
        print(titel.string)
        
    if str(price) != 'None':
        priceInInt=price.string
        # print(priceInInt)
        priceInInt=str(priceInInt)
        priceInInt=priceInInt.replace(',','')
        priceInInt=priceInInt.replace('₹','')
        print(int(priceInInt))