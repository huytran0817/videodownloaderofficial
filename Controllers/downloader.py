from tkinter import messagebox, filedialog
from pytube import YouTube
from Controllers.middleware import sanitize_filename, filterCase
# from Views.mainView import mainView as view
import Controllers.database
import re

db = Controllers.database


def claimLink(url, quality, type , format):
    try:

        yt = YouTube(url)
        print("someone tried to download: ",url," as ",type,"with ", format," format and ", quality, " quality.")
        video_title = sanitize_filename(yt.title)
        yt = YouTube(url)
        for stream in yt.streams.all():
            print(stream)
        if quality == 'auto':
            if type == 'Audio':
                stream = yt.streams.get_audio_only()
                print("get audio only")
            if type == 'Video':
                stream = yt.streams.get_highest_resolution()
                print("get highest resolution")
            dir = filedialog.askdirectory(initialdir="videos", title='Please select a directory')
        else:
            if type == 'Audio':
                stream = yt.streams.get_audio_only()
                print("get audio only")
            if type == 'Video':
                stream = yt.streams.get_by_resolution(quality)
                print("get ", quality ," resolution")
            dir = filedialog.askdirectory(initialdir="videos", title='Please select a directory')
        if stream is None:
            print('No stream matching the criteria')
            return None
        
        fileName = str(video_title)+'_'+str(quality)+'.'+ str(format)
        stream.download(output_path=dir, filename= fileName)
        return messagebox.showinfo("Success", "Video downloaded successfully")
    except Exception as e:
        print('Error downloading video:', e)
        return messagebox.showerror("Error", "Failed to download video")

def download(data):
    url = data['url']
    quality = data['quality'].strip(" ")
    type = data['type'].strip(" ")
    format = data['format'].strip(" ")
    regex = re.compile('^https://www.youtube.com/watch?')
    regexshort = re.compile('^https://www.youtube.com/shorts/')
    print(type)
    print (len(quality)) 
    print(len(format))
    if(regex.match(url) or regexshort.match(url)): 
        if type!= None and type!="None" and quality!= None and quality!="" and format!= None and format!="":
            claimLink(url, quality, type, format)
        else:
            messagebox.showerror("Error", "Info require!")
                
    else:
        messagebox.showerror("Error", "Invalid URL!")    
        

# def progress_Check(stream = None, chunk = None, file_handle = None, remaining = None):

#         percent ="file_size", remaining + 1000000   

#         try: 
#             # updates the progress bar                                   
#             bar.update(round(percent/1000000,2))
#         except: 
#             # progress bar dont reach 100% so a little trick to make it 100    
#             bar.update(round("file_size"/1000000,2))