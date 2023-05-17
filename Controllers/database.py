import mysql.connector
def connectDB():
    try:
        conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="downloadhistory"
            )
        return conn
    except Exception as e:
        return (e)
    
def insert_into_db(video_title, video_url):
        mydb = connectDB()
        mycursor = mydb.cursor()

        sql = "INSERT INTO download_history (video_title, video_url) VALUES (%s, %s)"
        val = (video_title, video_url)
        mycursor.execute(sql, val)

        mydb.commit()

        print(mycursor.rowcount, "record inserted.")

def get_downloaded_videos():
    mydb = connectDB()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM download_history")
    return mycursor.fetchall()

