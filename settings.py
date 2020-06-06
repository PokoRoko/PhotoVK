# Import my very secret token  :з
from .my_api import my_token
access_token = my_token

# Photo size to add url in db
# Если указано несколько вариантоов то загрузится наиболее качественная из имеющихся
photo_size = (
    'photo_2560',
    'photo_1280',
    'photo_807',
    'photo_604',
    'photo_130',
    'photo_75'
)

# Number of photographs for which information is required (def=20,max=200)
max_photo = '30'
