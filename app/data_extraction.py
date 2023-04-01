
from typing import List
from bs4 import BeautifulSoup
import requests
from csv import writer

def extract_buy_properties_page() -> List[str]:

    url = "https://www.bproperty.com/en/bangladesh/properties-for-sale/"
    website_main_url = "https://www.bproperty.com/"
    page = requests.get(url)

    soup = BeautifulSoup(page.content,'lxml')
    listed_items = soup.find_all('a',class_="_287661cb")
    print(len(listed_items))
    detail_page_urls = []
    for list_item in listed_items:
        detail_page_url_context = list_item.get('href')
        detail_page_url = f"{website_main_url}{detail_page_url_context}"
        detail_page_urls.append(detail_page_url)

    return detail_page_urls

def extract_detail_page(list:List[str]):
    with open('housing.csv', 'w', encoding='utf8', newline='') as f:
        thewriter = writer(f)
        header = ['Type', 'Location', 'Price', 'Area','Bed Rooms','Bath Rooms']
        thewriter.writerow(header)

        for detail_page_url in list :
             page = requests.get(detail_page_url)
             soup = BeautifulSoup(page.content,'lxml')
             currency = soup.find('span',class_="e63a6bfb").text
             price = soup.find('span',class_="_105b8a67").text
             location = soup.find('div',class_="_1f0f1758").text
             num_bed_rooms = soup.find('span',class_="fc2d1086").text
             num_bath_rooms = soup.find('span',class_="fc2d1086").text
             area = soup.find('span',class_="fc2d1086").text
             type = soup.find('span',class_="_812aa185").text

             info = [type, location, price, area,num_bed_rooms,num_bath_rooms]
             thewriter.writerow(info)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("main")
    list_of_detail_page_urls = extract_buy_properties_page()
    extract_detail_page(list_of_detail_page_urls)