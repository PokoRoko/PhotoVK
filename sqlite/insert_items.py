import sqlite3
from ..get_items import get_best_size_photo

params = (
            'album_id', 'date', 'id', 'owner_id', 'has_tags',
            'height', 'photo_2560', 'photo_1280', 'photo_807',
            'post_id', 'photo_604', 'photo_130', 'photo_75',
            'text', 'width', 'photo'
            )


def insert_list_items(list_items):
    for i in list_items:
        item_photo = i
        for j in params:
             if item_photo.get(j) == None:
                item_photo[j] = None
        item_and_photo = get_best_size_photo(item_photo)
        insert_items_photo(item_and_photo)




# Insert items myphoto
def insert_items_photo(items):
    conn = sqlite3.connect("dbPhotoVK.db")  # or :memory: for save in RAM
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO myphoto VALUES (
                    :album_id,
                    :date,
                    :id,
                    :owner_id,
                    :has_tags,
                    :height,
                    :photo_2560,
                    :photo_1280,
                    :photo_807,
                    :photo_604,
                    :photo_130,
                    :photo_75,
                    :post_id,
                    :text,
                    :width,
                    :photo
                    )''', items)
    conn.commit()
