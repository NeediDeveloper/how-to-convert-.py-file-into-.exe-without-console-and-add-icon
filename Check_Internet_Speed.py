import sys
import os

if getattr(sys, 'frozen', False):
    sys.stdout = open(os.devnull, 'w')
    sys.stderr = open("error.log", 'w')


import tkinter as tk
import speedtest #pip install speedtest-cli

def CheckSpeed():
    st = speedtest.Speedtest()
    # if the code is not working then uncomment the following line of code
    st.get_best_server()
    CheckButton.config(image=StartImg)
    
    UploadingLabel.config(text="Testing Upload Speed...", fg="#f07007")
    window.update_idletasks() 
    upload_speed = st.upload() / 1_000_000
    UploadingLabel.config(text=f"Uploading Speed {upload_speed:.2f} MBPS", fg="#22c406")
   
   
    DownloadingLabel.config(text="Testing Download Speed...", fg="#f07007")
    window.update_idletasks()
    download_speed = st.download() / 1_000_000
    DownloadingLabel.config(text=f"Downloading Speed {download_speed:.2f} MBPS", fg="#22c406")

    CheckButton.config(image=StopImg)
    
    
window = tk.Tk()
window.title("Speed Test")
window.iconbitmap("icon.ico")
window.geometry("600x350")
window.configure(bg="#f7f1e1")
window.resizable(False, False)

FirstLabel = tk.Label(window, text="Check Internet Speed",
                      font=("Georgia", 20), bg="#f7f1e1"
                      )
FirstLabel.place(x=170, y=20)

UploadingLabel = tk.Label(window, text="Uploading Speed 0",
                      font=("Georgia", 15), bg="#f7f1e1"
                      )
UploadingLabel.place(x=280, y=130)

DownloadingLabel = tk.Label(window, text="Downloading Speed 0",
                      font=("Georgia", 15), bg="#f7f1e1"
                      )
DownloadingLabel.place(x=280, y=180)

StartImg = tk.PhotoImage(file="start.png").subsample(4, 4)
StopImg = tk.PhotoImage(file="stop.png").subsample(4, 4)

CheckButton = tk.Button(window, bg="#f7f1e1", relief="flat", command=CheckSpeed,
                        image=StopImg, activebackground="#f7f1e1",)
CheckButton.place(x=120, y=120)

window.mainloop()