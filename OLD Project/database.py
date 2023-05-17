import mysql.connector

db_config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'downloadhistory',
}

def connect_to_database():
    connection = mysql.connector.connect(**db_config)
    return connection

def create_table(connection):
    cursor = connection.cursor()
    table_creation_query = '''CREATE TABLE IF NOT EXISTS download_history (
                                id INT AUTO_INCREMENT PRIMARY KEY,
                                video_title VARCHAR(255) NOT NULL,
                                video_url VARCHAR(2083) NOT NULL,
                                timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                             )'''
    cursor.execute(table_creation_query)
    connection.commit()


def save_download_history(connection, url, title, type):
    cursor = connection.cursor()
    query = "INSERT INTO download_history (video_url, video_title, type, timestamp) VALUES (%s, %s, %s, NOW())"
    cursor.execute(query, (url, title, type))
    connection.commit()


def get_download_history(connection):
    cursor = connection.cursor()
    query = "SELECT video_url, video_title, timestamp FROM download_history ORDER BY timestamp DESC"
    cursor.execute(query)
    return cursor.fetchall()

