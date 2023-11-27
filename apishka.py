from typing import Union

from fastapi import FastAPI

import psycopg2

app = FastAPI()

app.get("/")


def read_root():
    return {"Hello": "World"}


# @app.get("/fuck/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#    return {"item_id": item_id, "q": q}

@app.get("/search/{item_id}")
def read_users(item_id: str, q: Union[str, None] = None):
    try:
        conn = psycopg2.connect(dbname='people', user='postgres', password='1234', host='host')
    except:
        print('Can`t establish connection to database')

    cursor = conn.cursor()

    # Получаем список всех пользователей
    cursor.execute('SELECT search_vector FROM all_info WHERE search_vector @@ to_tsquery("russian", item_id);')
    users = cursor.fetchall()
    cursor.close()  # закрываем курсор
    conn.close()  # закрываем соединение

    return users