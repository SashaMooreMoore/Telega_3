import requests
from deepface import DeepFace


url_one = 'https://graco-nsk.ru/wp-content/uploads/e/6/3/e63ff36e6266df68112184f709fa4593.jpeg'
url_two = 'https://video-images.vice.com/articles/598105bc703fe320e778b5cd/lede/1501627916500-DSC_0892.jpeg'


response_one = requests.get(url_one)
response_two = requests.get(url_two)

with open('photo_one.jpg', 'wb') as file: # к оператору нужно добавить букву b для обозначения бинарности
    file.write(response_one.content)

with open('photo_two.jpg', 'wb') as file: 
    file.write(response_two.content)   