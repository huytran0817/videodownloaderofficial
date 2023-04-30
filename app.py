from flask import Flask, render_template, request, redirect, Response
import yt_dlp
from pytube import YouTube
import requests
from slugify import slugify
from database import connect_to_database, save_download_history, get_download_history

app = Flask(__name__)

db_connection = connect_to_database()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/terms-conditions')
def terms():
    return render_template('terms-conditions.html')

@app.route('/history')
def history():
    history_data = get_download_history(db_connection)
    return render_template('history.html', videos=history_data)

@app.route('/download', methods=["POST", "GET"])
def download():
    url = request.form["url"]
    print("Someone just tried to download", url)

    try:
        yt = YouTube(url)
        stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
        download_link = stream.url
        title = yt.title

    except Exception as e:
        print("Error downloading video using pytube:", e)
        
        try:
            with yt_dlp.YoutubeDL() as ydl:
                info = ydl.extract_info(url, download=False)
                try:
                    download_link = info["entries"][-1]["formats"][-1]["url"]
                except:
                    download_link = info["formats"][-1]["url"]
                title = info['title']
        
        except Exception as e:
            print("Error downloading video using yt-dlp:", e)
            return redirect('/')

    save_download_history(db_connection, url, title)

    response = requests.get(download_link, stream=True)
    headers = {
        'Content-Disposition': f'attachment; filename={slugify(title)}.mp4',
        'Content-Type': 'video/mp4'
    }
    return Response(response.iter_content(chunk_size=8192), headers=headers)

if __name__ == '__main__':
    app.run(port=80, debug=True)
