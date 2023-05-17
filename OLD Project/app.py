from flask import Flask, render_template, request, redirect, Response
import yt_dlp
from pytube import YouTube
import requests
from slugify import slugify
from database import connect_to_database, save_download_history, get_download_history
import database
import routes
import controller

app = Flask(__name__)

# db_connection = connect_to_database()

# def download():
#     url = download(data)
#     try:
#         yt = YouTube(data.url)
#         stream = yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first()
#         download_link = stream.url
#         title = yt.title

#     except Exception as e:
#         print("Error downloading video using pytube:", e)
        
#         try:
#             with yt_dlp.YoutubeDL() as ydl:
#                 info = ydl.extract_info(url, download=False)
#                 try:
#                     download_link = info["entries"][-1]["formats"][-1]["url"]
#                 except:
#                     download_link = info["formats"][-1]["url"]
#                 title = info['title']
        
#         except Exception as e:
#             print("Error downloading video using yt-dlp:", e)
#             return redirect('/')

#     save_download_history(db_connection, url, title)

#     response = requests.get(download_link, stream=True)
#     headers = {
#         'Content-Disposition': f'attachment; filename={slugify(title)}.mp4',
#         'Content-Type': 'video/mp4'
#     }
#     return Response(response.iter_content(chunk_size=8192), headers=headers)

if __name__ == '__main__':
    routes.run()
    controller.downloadProcess()
