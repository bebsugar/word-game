from db.database import cursor, mydb


def get_random_word():
    sql = 'SELECT word, translation FROM words ORDER BY RAND() LIMIT 1'
    cursor.execute(sql)
    random_word = cursor.fetchone()
    return random_word


def check_date_exists(date) -> bool:
    query = "SELECT date FROM statistics WHERE date = %s"
    cursor.execute(query, [date])
    row = cursor.fetchone()
    if row is None:
        return False
    return True


def insert_row(date, total_count, correct_answer_count):
    sql = "INSERT INTO statistics (date, total_answer, correct_answers) VALUES (%s, %s, %s)"
    val = (date, total_count, correct_answer_count)
    cursor.execute(sql, val)
    mydb.commit()


def update_row(total_count, correct_answer_count, date):
    sql = """
    UPDATE statistics
    SET total_answer = total_answer + %s,
    correct_answers = correct_answers + %s
    WHERE date = %s;
    """
    val = (total_count, correct_answer_count, date)
    cursor.execute(sql, val)
    mydb.commit()
