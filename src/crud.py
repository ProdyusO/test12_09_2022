# pylint: disable=C0301, C0114,  W3101
from bs4 import BeautifulSoup
import requests

from database import database
from models import notes



def get_pages_content(html):
    """Get data from page."""
    soup = BeautifulSoup(html, "lxml")
    data = soup.find_all("div", {"class": "container-results large-images"})[1].find_all("div", {"class": "search-item"})
    detail = []
    for item in data:
        detail.append(
            {
                "title": item.find("a").get_text(strip=True),
                "img": item.find("img").get("data-src"),
                "date": item.find("span", {"class": "date-posted"}).get_text(strip=True),
                "city": item.find("span", {"class": ""}).get_text(strip=True),
                "bed": item.find("span", {"class": "bedrooms"}).get_text().replace("\n", "").replace(" ", ""),
                "description": item.find("div", {"class": "description"}).get_text(strip=True),
                "currency": item.find("div", {"class": "price"}).get_text(strip=True)[0],
                "price": item.find("div", {"class": "price"}).get_text(strip=True)[1:],
            }
        )
    return detail


async def save_to_db(nums, URL):
    """Write data into db."""
    items = []
    for page in range(nums):
        html1 = requests.get(URL, params={"page-": page})
        items.extend(get_pages_content(html1.text))
    print(len(items))
    for item in items:
        detail = notes.insert().values(
            title=item["title"],
            img=item["img"],
            date=item["date"],
            city=item["city"],
            bed=item["bed"],
            description=item["description"],
            currencies=item["currency"],
            price=item["price"],
        )
        await database.execute(detail)


async def read_from_db():
    """Show db items."""
    return await database.fetch_all(query=notes.select())
