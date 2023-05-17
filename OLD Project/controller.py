from flask import Flask, render_template, request, redirect, Response
import yt_dlp
from pytube import YouTube
import requests
from slugify import slugify
from database import connect_to_database, save_download_history, get_download_history
import routes
import json

db_connection = connect_to_database()

def filterCase(r):
    switcher={
            'video/auto':'auto',
            'video/360p':'360p',
            'video/480p':'480p',
            'video/720p':'720p',
            'video/1080p':'1080p',
            'audio/128kbps':'128kbps',
            'audio/192kbps':'192kbps',
            'audio/320kbps':'320kbps',

            }
    return switcher.get(r,"Invalid filterd!")
def formatCase(f):
    switcher={
            'video/auto':'mp4',
            'video/360p':'mp4',
            'video/480p':'mp3',
            'video/720p':'mp4',
            'video/1080p':'mp4',
            'audio/128kbps':'mp3',
            }
    return switcher.get(f,"Invalid format!")
def typeCase(f):
    switcher={
            'video/auto':'video',
            'video/360p':'video',
            'video/480p':'video',
            'video/720p':'video',
            'video/1080p':'video',
            'audio/128kbps':'audio',
            }
    return switcher.get(f,"Invalid format!")

def claimLink(url):
    try:
        yt = YouTube(url)
        title = yt.title
        thumbnail = yt.thumbnail_url
        author = yt.author
        view = yt.views
        rating = yt.rating
        print(thumbnail)
        print(title)
        return render_template('index.html', title=title, thumbnail=thumbnail, author=author, view=view, rating=rating,url=url)
    except Exception as e:
        print("Error:", e)
        return render_template('index.html')

def downloadProcess(data):
    url = data[0]['url']
    type = data[0]['type']
    print("Someone just tried to download", url, "as", type)
    try:
        yt = YouTube(url, use_oauth=True, allow_oauth_cache=True)
        if typeCase(type)=='audio':
            stream = yt.streams.filter(only_audio=True, bitrate=filterCase(type)).first()
        if filterCase(type)=='auto':
            stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').first()
        else:
            stream = yt.streams.filter(file_extension='mp4', res=filterCase(type)).order_by('resolution').desc().first()
        download_link = stream.url
        title = yt.title
        thumbnail = yt.thumbnail_url
    except Exception as e:
        print("Error downloading video using pytube:", e)
        return routes.home()
        # try:
        #     with yt_dlp.YoutubeDL() as ydl:
        #         info = ydl.extract_info(url, download=False)
        #         try:
        #             download_link = info["entries"][-1]["formats"][-1]["url"]
        #         except:
        #             download_link = info["formats"][-1]["url"]
        #             return routes.home()
        #         title = info['title']
        # except Exception as e:
        #     print("Error downloading video using yt-dlp:", e)
        #     return routes.home()

    save_download_history(db_connection, url, title, type)
    response = requests.get(download_link, stream=True)

    headers = {
        'Content-Disposition': f'attachment; filename= [VIDOWN] - {slugify(title)}.{formatCase(type)}',
        'Content-type': type,
        'format': formatCase(type)
    }
    
    return Response(response.iter_content(chunk_size=8192), headers=headers)


