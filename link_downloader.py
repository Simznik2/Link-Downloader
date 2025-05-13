def link_downloader(self, url, directory, quality="360p", file_format="mp4"):
    from yt_dlp import YoutubeDL
    import os

    ydl_opts = {
        'noplaylist': True,
        'outtmpl': os.path.join(directory, '%(title)s.%(ext)s'),
        'progress_hooks': [self.progress_hook],
    }

    quality_dict = {
        "360p": "bestvideo[height<=360]+bestaudio/best",
        "480p": "bestvideo[height<=480]+bestaudio/best",
        "720p": "bestvideo[height<=720]+bestaudio/best",
        "1080p": "bestvideo[height<=1080]+bestaudio/best",
    }

    if file_format == "mp4":
        ydl_opts['format'] = quality_dict.get(quality, "bestvideo[height<=360]+bestaudio/best")
        ydl_opts['postprocessors'] = [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4'  # Prepisuje kontajner na MP4
        }]
    
    elif file_format == "mp3":
        ydl_opts['format'] = 'bestaudio[ext=m4a]/bestaudio'
        ydl_opts['postprocessors'] = []  # Žiadny postprocessing
    
    try:
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        return True
    except Exception as e:
        print(f"Error during download: {e}")
        return False