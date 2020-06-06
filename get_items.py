import requests
from .settings import photo_size, max_photo


def get_best_size_photo(items):
    for i in photo_size:
        if items.get(i) != None:
            best_photo = requests.get(items.get(i)).content
            items['photo'] = best_photo
            return items


# return dict items photo
def get_list_photo_items(access_token):
    api_url = "https://api.vk.com/method/photos.getAll"  # url for method photos.getAll
    params = {
        #    'owner_id':'-150926517', # Можно скачать фото определенного пользователя если у вас есть к ним доступ
        'extended': '0',  # returns advanced photo information
        'count': max_photo,  # the number of photographs for which information is required (def=20,max=200)
        'access_token': access_token,  # token for this application
        'v': '5.52'  # Ver API
            }
    res = requests.get(api_url, params=params)
    print(res.status_code)
    data = res.json()
    list_items = data['response']['items']
    return list_items


