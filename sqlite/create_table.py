import sqlite3


def create_table_myphoto():
    conn = sqlite3.connect("dbPhotoVK.db")  # or :memory: for save in RAM
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE  IF NOT EXISTS myphoto
                    (
                    album_id TEXT,
                    date TEXT,
                    id INTEGER PRIMARY KEY,
                    owner_id INTEGER,
                    has_tags TEXT,
                    height INTEGER,
                    photo_2560 TEXT,
                    photo_1280 TEXT,
                    photo_807 TEXT,
                    photo_604 TEXT,
                    photo_130 TEXT,
                    photo_75 TEXT,
                    post_id,
                    text TEXT,
                    width INTEGER,
                    photo BLOB
                    )""")
    conn.commit()
