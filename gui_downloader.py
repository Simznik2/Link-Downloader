import customtkinter as ctk
from tkinter import filedialog, messagebox
from yt_dlp import YoutubeDL
import pyperclip
import os

class LinkDownloaderApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("YouTube Link Downloader")
        self.geometry("500x500")
        self.resizable(False, False)

        # URL Frame
        self.url_frame = ctk.CTkFrame(self)
        self.url_frame.pack(pady=10, padx=10, fill="x")
        self.url_label = ctk.CTkLabel(self.url_frame, text="Video URL")
        self.url_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.url_entry = ctk.CTkEntry(self.url_frame, width=400)
        self.url_entry.pack(side="left", padx=(10, 5), pady=10)
        self.paste_button = ctk.CTkButton(self.url_frame, text="Paste", command=self.paste_url, width=50)
        self.paste_button.pack(side="right", padx=(0, 10))

        # Format Frame
        self.format_frame = ctk.CTkFrame(self)
        self.format_frame.pack(pady=10, padx=10, fill="x")
        self.format_label = ctk.CTkLabel(self.format_frame, text="Select Format")
        self.format_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.format_var = ctk.StringVar(value="mp4")
        self.mp4_radio = ctk.CTkRadioButton(self.format_frame, text="MP4 (Video)", variable=self.format_var, value="mp4")
        self.mp4_radio.pack(anchor="w", padx=10, pady=2)
        self.mp3_radio = ctk.CTkRadioButton(self.format_frame, text="MP3 (Audio)", variable=self.format_var, value="mp3")
        self.mp3_radio.pack(anchor="w", padx=10, pady=2)

        # Quality Frame
        self.quality_frame = ctk.CTkFrame(self)
        self.quality_frame.pack(pady=10, padx=10, fill="x")
        self.quality_label = ctk.CTkLabel(self.quality_frame, text="Select Quality")
        self.quality_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.quality_dropdown = ctk.CTkOptionMenu(self.quality_frame, values=["360p", "480p", "720p", "1080p"])
        self.quality_dropdown.set("360p")
        self.quality_dropdown.pack(padx=10, pady=5)

        # Directory Frame
        self.dir_frame = ctk.CTkFrame(self)
        self.dir_frame.pack(pady=10, padx=10, fill="x")
        self.dir_label = ctk.CTkLabel(self.dir_frame, text="Download Directory")
        self.dir_label.pack(anchor="w", padx=10, pady=(5, 0))
        self.dir_entry = ctk.CTkEntry(self.dir_frame, width=400)
        self.dir_entry.pack(side="left", padx=(10, 5), pady=10)
        self.browse_button = ctk.CTkButton(self.dir_frame, text="Browse", command=self.browse_directory, width=50)
        self.browse_button.pack(side="right", padx=(0, 10))

        # Download button
        self.download_button = ctk.CTkButton(self, text="Download", command=self.start_download)
        self.download_button.pack(pady=20)

        # Status
        self.status_label = ctk.CTkLabel(self, text="Ready", text_color="green")
        self.status_label.pack()

    def paste_url(self):
        text = pyperclip.paste()
        if len(text) <= 100:
            self.url_entry.delete(0, "end")
            self.url_entry.insert(0, text)
        else:
            messagebox.showwarning("Warning", "URL is too long (max 100 characters).")

    def browse_directory(self):
        folder = filedialog.askdirectory()
        if folder:
            self.dir_entry.delete(0, "end")
            self.dir_entry.insert(0, folder)

    def start_download(self):
        url = self.url_entry.get()
        directory = self.dir_entry.get()
        quality = self.quality_dropdown.get()
        file_format = self.format_var.get()

        if not url or not directory:
            messagebox.showerror("Error", "Please provide both URL and download directory.")
            return

        self.status_label.configure(text="Downloading...", text_color="orange")
        success = self.link_downloader(url, directory, quality, file_format)

        if success:
            self.status_label.configure(text="Download Completed", text_color="green")
        else:
            self.status_label.configure(text="Download Failed", text_color="red")

    def link_downloader(self, url, directory, quality="360p", file_format="mp4"):
        ydl_opts = {
            'noplaylist': True,
            'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
            'progress_hooks': [self.progress_hook],
        }

        quality_dict = {
            "360p": "bestvideo[height<=360]",
            "480p": "bestvideo[height<=480]",
            "720p": "bestvideo[height<=720]",
            "1080p": "bestvideo[height<=1080]",
        }

        if file_format == "mp4":
            ydl_opts['format'] = quality_dict.get(quality, "bestvideo[height<=360]")
        elif file_format == "mp3":
            ydl_opts['format'] = 'bestaudio'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]

        try:
            with YoutubeDL(ydl_opts) as ydl:
                ydl.download([url])
            return True
        except Exception as e:
            print(f"Error during download: {e}")
            return False

    def progress_hook(self, d):
        if d['status'] == 'downloading':
            percent = d.get('percent', 0)
            print(f"Downloading: {percent}")
        elif d['status'] == 'finished':
            print("Download completed!")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # alebo "light"
    ctk.set_default_color_theme("blue")  # alebo "green", "dark-blue"
    app = LinkDownloaderApp()
    app.mainloop()