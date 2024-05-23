import requests
from deepface import DeepFace
import os


url_one = 'https://graco-nsk.ru/wp-content/uploads/e/6/3/e63ff36e6266df68112184f709fa4593.jpeg'
url_two = 'https://video-images.vice.com/articles/598105bc703fe320e778b5cd/lede/1501627916500-DSC_0892.jpeg'


response_one = requests.get(url_one)
response_two = requests.get(url_two)

current_path = os.path.dirname(os.path.abspath(__file__)) # Вернет абсолютный путь 
photos_path = os.path.join(current_path, 'photos') # объединяет пути в один

photo_1 = os.path.join(photos_path, 'photo_one.jpg')
photo_2 = os.path.join(photos_path, 'photo_two.jpg')

with open(photo_1, 'wb') as file:       # 'wb' b - обозначение бинарности
    file.write(response_one.content)

with open(photo_2, 'wb') as file: 
    file.write(response_two.content)   