from db.db import cursor


def get_random_word():
    sql = 'SELECT word, translation FROM words ORDER BY RAND() LIMIT 1'
    cursor.execute(sql)
    random_word = cursor.fetchone()
    return random_word

