import tkinter as tk 
import customtkinter as ctk
from pytube import YouTube



def downloadYoutubeVideo():
    try:
        ytLink = link.get()
        ytObject = YouTube(ytLink, on_progress_callback=on_progress)
        # audio = ytObject.streams.get_audio_only()
        # audio.download()
        video = ytObject.streams.get_highest_resolution()
        video.download()
        finishLable.configure(text=f"Downloaded video {ytObject.title} by {ytObject.author}")
    except:
        finishLable.configure(text="Download Error", text_color = "red")
    # finishLable.configure(text="Task is complite!")



def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = round((bytes_downloaded * 100 / total_size), 0)
    per = str(int(percentage_of_completion))
    pPercentage.configure(text=f"{per}%")
    pPercentage.update()
    progressBar.set(float(percentage_of_completion)/100)
    print("test")


#mSystem settings

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


# App frame

app = ctk.CTk()
app.geometry("720x480")
app.title("Downloader")


#Adding ui elem
title = ctk.CTkLabel(app, text="Insert a youtube link")
title.pack(padx = 10, pady = 10)


url_var = tk.StringVar()
link = ctk.CTkEntry(app, width = 350, height = 10, textvariable = url_var)
link.pack()



pPercentage = ctk.CTkLabel(app, text="0%")
pPercentage.pack()

progressBar = ctk.CTkProgressBar(app, width = 400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

finishLable = ctk.CTkLabel(app, text="")
finishLable.pack()
 
downloadButton = ctk.CTkButton(app, 
                                width=120, 
                                height=32, 
                                border_width=0, 
                                corner_radius=8, 
                                text="Download", 
                                command=downloadYoutubeVideo)

downloadButton.pack(padx = 10, pady=10)

# Run app
app.mainloop()