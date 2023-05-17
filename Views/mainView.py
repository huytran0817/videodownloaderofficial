# import tkinter as tk
# from tkinter import ttk, messagebox, Label, Radiobutton, PhotoImage
# import threading
from Controllers import downloader
# from functools import partial

# class mainView(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.initializeUI()

#     def initializeUI(self):
#         self.title("Video Downloader")
#         self.minsize(800, 600)  # width, height
#         self.geometry("800x600+50+50")
#         self.setupWindow()

#         photo = PhotoImage(file = "img/logo.png")
#         self.iconphoto(False, photo)
#     # window = tk.Tk()
#     # window.title("Video_Downloader")
#     # window.geometry('800x600') # Set the size of the window
#     # window.configure(bg='white') # Set the background color of the window
#     def setupWindow(self):
#         self.url_label = tk.Label(self, text="URL", )
#         self.url_label.config(width=20, height=3, font=("Arial", 12, "bold"))
#         self.url_label.pack()

#         self.url_entry = tk.Entry(self, width=50)
#         self.url_entry.config(font=("Arial", 12))
#         self.url_entry.pack()
#         Option_label = tk.Label(self, text="Option", )
#         Option_label.config(width=20, height=3, font=("Arial", 12, "bold"))
#         Option_label.pack()
#         self.typeRadio= tk.StringVar()
#         self.typeRadio.set(None)
#         self.videoFormat_list= ['MP4', 'MOV', 'WMV', 'AVI', 'FLV', 'MKV', 'WEBM']
#         self.audioFormat_list= ['MP3', 'WAV', 'AAC', 'OGG']
#         self.type_label = Label(self, text="Type: ").pack()
#         self.audioType = Radiobutton(self, text="Audio", variable= self.typeRadio, value="Audio", command= partial(self.showFormat)).pack()
#         self.videoType = Radiobutton(self, text="Video",variable= self.typeRadio, value="Video", command= partial(self.showFormat)).pack()
#         self.format_label = Label(self, text="Format: ").pack()
#         # if typeRadio.get() == "Audio":
#         #     combo_format.configure(values=self.audio_list)
#         # if typeRadio.get() == "Video":
#         #     combo_format.configure(values=self.video_list)
#         self.combo_format = ttk.Combobox(self, values="", state="readonly")
#         self.combo_format.pack()
#         quality_label = Label(self, text="Quality: ").pack()
#         self.videoQua_list= ["auto", "1080p", "720p", "480p", "360p", "240p", "144p"]
#         self.audioQua_list= ["auto", "320kbps", "128kbps", "64kbps"]
#         self.combo_quality = ttk.Combobox(self, state="readonly", values="")
#         self.combo_quality.pack()

#         self.download_button = tk.Button(self, text="Download", command=partial(self.Submit))
#         self.download_button.pack()

#         self.history_button = tk.Button(self, text="History", command=None)
#         self.history_button.pack()

#         # # Create the frame to hold the Listbox
#         # self.listbox_frame = tk.Frame(self, bd=2, relief=tk.GROOVE)
#         # self.listbox_frame.pack(pady=10)

#         # # Create the Listbox inside the frame
#         # self.listbox = tk.Listbox(self.listbox_frame, width=100, height=20)
#         # self.listbox.pack(side=tk.LEFT, fill=tk.BOTH)

#         # # Create a scrollbar for the Listbox
#         # scrollbar = tk.Scrollbar(self.listbox_frame, orient=tk.VERTICAL)
#         # scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

#         # # Configure the scrollbar to work with the Listbox
#         # self.listbox.config(yscrollcommand=scrollbar.set)
#         # scrollbar.config(command=self.listbox.yview)

#         # Update the listbox with downloaded videos


#         # update_downloaded_videos_list()
    # def showFormat(self):

    #     var = self.typeRadio.get()
    #     if var == "Audio":
    #         self.combo_format.configure(values=self.audioFormat_list)
    #         self.combo_quality.configure(values=self.audioQua_list)
    #     if var == "Video":
    #         self.combo_format.configure(values=self.videoFormat_list)
    #         self.combo_quality.configure(values=self.videoQua_list)

    # def Submit(self):
    #     result=[]
    #     url = self.url_entry.get()
    #     type = self.typeRadio.get()
    #     format = self.combo_format.get()
    #     quality = self.combo_quality.get()
    #     data = {'url': url,
    #             'type': type,
    #             'format': format,
    #             'quality': quality}
    #     result.append(data)
    #     downloader.download(data)

#CHAT GPT GENERATED SOURCE
import tkinter as tk
from tkinter import ttk, Label, Radiobutton, PhotoImage
from functools import partial
from tkinter import *
from PIL import ImageTk, Image

class MainView(tk.Tk):
    def __init__(self):
        super().__init__()
        self.initialize_ui()

    def initialize_ui(self):
        self.title("Video Downloader")
        self.minsize(800, 600)  # width, height
        self.geometry("800x600+50+50")

        style = ttk.Style()
        style.theme_use('clam')
        style.configure(".", font=("Helvetica", 11))
        style.configure("TButton", foreground='black', background='lightblue')
        style.configure("TLabel", foreground='black', background='lightgrey')
        style.configure("TRadiobutton", foreground='black', background='lightgrey')

        self.setup_window()
        photo = PhotoImage(file="img/logo.png")
        self.iconphoto(False, photo)

    def setup_window(self):
        # set logo at the top
        logo = PhotoImage(file="img/logo.png")
        logo = logo.subsample(5) 
        logo_label = tk.Label(self, image=logo)
        logo_label.image = logo  # keep a reference to prevent garbage collection
        logo_label.pack()


        header = tk.Frame(self )
        header.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(header, text="Video Downloader", fg='black', font=("Helvetica", 24, "bold")).pack()

        url_frame = tk.Frame(self, )
        url_frame.pack(fill=tk.X, padx=10, pady=10)
        tk.Label(url_frame, text="URL: ", width=20, height=2, fg='black', font=("Arial", 14, "bold")).grid(row=0, column=0, padx=5, pady=5)
        self.url_entry = tk.Entry(url_frame, width=50, font=("Arial", 12))
        self.url_entry.grid(row=0, column=1, padx=5, pady=5)

        options_frame = tk.Frame(self)
        options_frame.pack(fill=tk.X, padx=10, pady=10)

        tk.Label(options_frame, text="Options: ", width=20, height=2, fg='black', font=("Arial", 14, "bold")).grid(row=0, column=0, padx=5, pady=5)
        
        self.type_radio = tk.StringVar()
        self.type_radio.set(None)
        self.video_format_list = ['MP4', 'MOV', 'WMV', 'AVI', 'FLV', 'MKV', 'WEBM']
        self.audio_format_list = ['MP3', 'WAV', 'AAC', 'OGG']

        Label(options_frame, text="Type: ", font=("Arial", 12)).grid(row=1, column=0, padx=5, pady=5)
        Radiobutton(options_frame, text="Audio", variable=self.type_radio, value="Audio", command=partial(self.show_format), font=("Arial", 12)).grid(row=1, column=1, padx=5, pady=5)
        Radiobutton(options_frame, text="Video", variable=self.type_radio, value="Video", command=partial(self.show_format), font=("Arial", 12)).grid(row=1, column=2, padx=5, pady=5)

        Label(options_frame, text="Format: ", font=("Arial", 12)).grid(row=2, column=0, padx=5, pady=5)
        self.combo_format = ttk.Combobox(options_frame, values="", state="readonly")
        self.combo_format.grid(row=2, column=1, padx=5, pady=5)

        Label(options_frame, text="Quality: ", font=("Arial", 12)).grid(row=3, column=0, padx=5, pady=5)

        self.video_qua_list = ["auto", "1080p", "720p", "480p", "360p", "240p", "144p"]
        self.audio_qua_list = ["auto", "320kbps", "128kbps", "64kbps"]

        self.combo_quality = ttk.Combobox(options_frame, state="readonly", values="")
        self.combo_quality.grid(row=3, column=1, padx=5, pady=5)

        buttons_frame = tk.Frame(self)
        buttons_frame.pack(fill=tk.X, padx=10, pady=10)

        ttk.Button(buttons_frame, text="Download", command=partial(self.submit)).grid(row=0, column=0, padx=5, pady=5, columnspan=2, sticky='nsew')


    def show_format(self):
        var = self.type_radio.get()
        if var == "Audio":
            self.combo_format.configure(values=self.audio_format_list)
            self.combo_quality.configure(values=self.audio_qua_list)
        if var == "Video":
            self.combo_format.configure(values=self.video_format_list)
            self.combo_quality.configure(values=self.video_qua_list)

    def submit(self):
        result=[]
        url = self.url_entry.get()
        type = self.type_radio.get()
        format = self.combo_format.get()
        quality = self.combo_quality.get()
        data = {'url': url,
                'type': type,
                'format': format,
                'quality': quality}
        result.append(data)
        downloader.download(data)