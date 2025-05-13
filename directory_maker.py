import customtkinter as ctk
import os
from tkinter import filedialog, messagebox

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

class FolderCreatorApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Media Folder Creator")
        self.geometry("400x200")

        self.label = ctk.CTkLabel(self, text="Choose your directory:")
        self.label.pack(pady=20)

        self.select_button = ctk.CTkButton(self, text="Browse", command=self.browse_directory)
        self.select_button.pack()

        self.status_label = ctk.CTkLabel(self, text="Waiting for a choice...")
        self.status_label.pack(pady=20)

    def browse_directory(self):
        path = filedialog.askdirectory()
        if not path:
            return
        
        video_path = os.path.join(path, "video")
        audio_path = os.path.join(path, "audio")

        try:
            os.makedirs(video_path, exist_ok=True)
            os.makedirs(audio_path, exist_ok=True)
            self.status_label.configure(text=f"Created:\n{video_path}\n{audio_path}", text_color="orange")
        except Exception as e:
            self.status_label.configure(text=f"Error: {e}", text_color="red")

if __name__ == "__main__":
    app = FolderCreatorApp()
    app.mainloop()