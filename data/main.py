import psycopg2
from userSettings import userSettings

conn = psycopg2.connect(
    database = 'railway',
    user = 'postgres',
    password = 'SYydOpWeEquRsAJbFJGHuGGSsLjoZYuO',
    host = 'roundhouse.proxy.rlwy.net',
    port = '21286',
)

class main:
    print("Hello, world!")
    test1 = userSettings("theman","theman@gmail.com","mahman")
    print(test1.user_id)
    print(test1.account_created_date)
    test1.setBirthday('january', "1", "1998")
    print(test1.birthday)
    
    cursor = conn.cursor()
    conn.autocommit = False
    sql = '''CREATE TABLE USER(
    user_ID INT,
    username VARCHAR,
    email VARCHAR,
    verified_email BOOLEAN,
    password VARCHAR,
    account_created_date VARCHAR,
    firstName VARCHAR,
    lastName VARCHAR,
    birthday VARCHAR,
    theme BOOLEAN,
    notifications BOOLEAN,
    analytics BOOLEAN,
    meditation_tab BOOLEAN
    )'''
    sql_two = '''CREATE TABLE MEDITATION(
    meditation_ID INT,
    user_ID INT,
    video_url VARCHAR,
    audio_url VARCHAR
    )'''
    cursor.execute(sql_two)
    insert = 'INSERT INTO USER (username, email, password) VALUES (%s, %s, %s, %s)'
    insert_two = 'INSERT INTO MEDITATION (meditation_ID, user_ID, video_url, audio_url) VALUES (%s, %s, %s, %s)'
    data = [('Theman','321itsthe@gmail.com','hellyeah')]
    data_two = [(1,1,'https://www.youtube.com/watch?v=dQw4w9WgXcQ', 'https://www.youtube.com/watch?v=dQw4w9WgXcQ')]
    cursor.executemany(insert_two, data_two)
    #cursor.executemany(insert, data)
    #cursor.execute('SELECT user_ID, username, email, password from USER')
    cursor.execute('SELECT * FROM MEDITATION')
    print(cursor.fetchall())

    cursor.execute('''SELECT * from account_emailaddress''')
    result = cursor.fetchone()
    print(result)

    cursor.execute('''SELECT username from auth_user''')
    result2 = cursor.fetchall()
    print(result2)

    conn.close() #closing the connection