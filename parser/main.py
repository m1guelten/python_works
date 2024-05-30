import requests
import json
from bs4 import BeautifulSoup

url = "https://allo.ua/"
headers = {
    "Accept": "application/json",
    "User-Agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)"
    "AppleWebKit/537.36 (KHTML, Like Gecko)"
    "Chrome/116.0.0.0 Mobile Safari/537.36",
}

req = requests.get(url, headers=headers)
src = req.text

soup = BeautifulSoup(src, "html.parser")
category = soup.find_all("a", class_="v-pt__link")
categories = [
    {"name": item.text.strip(),
     "link": item.get("href"),
     "id": item.get("data-tab-id")
     } for item in category
]

for i in categories:
    URL_product = i['link']
    if URL_product != '#':
        req = requests.get(URL_product, headers=headers)
        src = req.text
        soup = BeautifulSoup(src, "html.parser")

        products = soup.find_all("div", class_="product-card")
        all_products = [
             {"prod_name": item.find("a", class_="product-card__title").text
              if item.find("a", class_="product-card__title") is not None else None,
              "prod_img": item.find("img", class_="gallery__img").get("src")
              if item.find("img", class_="gallery__img") is not None else None,
              "price_new": item.find("div", class_="v-pb__cur").find("span", class_="sum").text
              if item.find("div", class_="v-pb__cur") is not None else None,
              "price_old": item.find("div", class_="v-pb__old").find("span", class_="sum").text
              if item.find("div", class_="v-pb__old") is not None else None
              } for item in products
        ]
        with open(f"{i['name']}.json", "w", encoding="utf8") as file:
            json.dump(all_products, file, indent=4, ensure_ascii=False)
