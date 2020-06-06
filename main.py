from PhotoVK.get_items import get_list_photo_items
from PhotoVK.my_api import my_token
from PhotoVK.sqlite.create_table import create_table_myphoto
from PhotoVK.sqlite.insert_items import insert_list_items


list_items = get_list_photo_items(my_token)
create_table_myphoto()
insert_list_items(list_items)
