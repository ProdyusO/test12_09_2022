
import requests
from bs4 import BeautifulSoup
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, String, Integer


DATABASE_NAME = 'aplication.sqlite'

engine = create_engine(f'sqlite:///{DATABASE_NAME}', connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

db = SessionLocal()

Base = declarative_base()


class Note(Base):

    __tablename__ = 'notes'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    img = Column(String(100))
    date = Column(String(100))
    city = Column(String(100))
    bed = Column(String(100))
    description = Column(String(100))
    currencies = Column(String(100))
    price = Column(String(100))

Base.metadata.create_all(engine)


soup = BeautifulSoup()
url = 'https://www.kijiji.ca/b-apartments-condos/city-of-toronto/c37l1700273'


html = requests.get(url).text
data = BeautifulSoup(html, 'lxml')


title = []
container_title = data.find_all('a', {'class': 'title'})
for link in container_title:
    space_out = link.get_text()
    title.append(space_out.replace('\n', ''))



img = []
container_img = data.find_all('div', {'class': 'image'})
for link in container_img:
   a = link.find('picture')
   if a != None:
    img.append(a.find('img').get('data-src'))
   else:
    img.append('None')


date = []
container_date = data.find_all('span', {'class': 'date-posted'})
for link in container_date:
    date.append(link.get_text().replace(' ', ''))


city = []
container_city = data.find_all('span', {'class': ''})
for link in container_city:
    space_out = link.get_text().replace(' ', '')
    city.append(space_out.replace('\n', ''))



bed = []
container_bed = data.find_all('span', {'class': 'bedrooms'})
for link in container_bed:
     space_out = link.get_text().replace(' ', '')
     bed.append(space_out.replace('\n', ''))



description = []
container_description = data.find_all('div', {'class': 'description'})
for link in container_description:
    space_out = link.get_text()
    description.append(space_out.replace('\n', ''))



currency = []
price = []
container_price = data.find_all('div', {'class': 'price'})
for link in container_price:
    currency.append(link.get_text().split()[0][0])
    price.append(link.get_text().split()[0][1:])


total = {'title': title, 'img': img, 'date': date, 'city': city, 'bed': bed, 'description': description, 'currency': currency, 'price': price}

# result = Note(title=a['title'], img=a['img'], date=a['date'], city=a['city'], bed=a['bed'], description=a['description'], currencies=a['currency'], price=a['price'])
print(total)

for i in total['title']:
    result=Note(title=i)
    db.add(result)
    db.commit()
    db.close()


# data = db.query(Note).all()
# for i in data:
#     for j in total['img']:
#         result = Note(img=j)
#         db.add(result)
#         db.commit()
