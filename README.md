# Link-Downloader
A link downloader (from youtube) using python with the library yt-dlp and a gui interface.
User Guide
Downloading and Installation
Download the Files:
Download all the files into a single directory:

directory_maker.py
gui_downloader.py
link_downloader.py
requirements.txt

Installing Dependencies:

Make sure you have Python installed (preferably version 3.7 or higher).
Open the command prompt or terminal and navigate to the directory where these files are located.
Run the following command:

pip install -r requirements.txt
This will install all the necessary libraries: customtkinter, yt-dlp, pyperclip.

Running the Application
Running the Downloader:

To launch the application, right-click on the gui_downloader.py file and select "Run," or in the command prompt, type:

python gui_downloader.py
Using the Application:

URL Frame: In the text box, enter the URL of the video you want to download. You can also click the "Paste" button to automatically insert the URL from the clipboard (copied URL).
Format: Select the format you want to download the video in:
MP4 (Video) – downloads the video (with audio if selected).
MP3 (Audio) – downloads only the audio.
Quality: Choose the desired video quality (e.g., 360p, 480p, 720p, 1080p).
Directory: Select the directory where the file should be downloaded.
Download: Once all the information is entered, click the "Download" button. The application will begin downloading the file based on your preferences.

Folder Creator:

If needed, you can create two separate folders for video and audio files.
Click the "Browse" button and choose the directory where the video/ and audio/ subdirectories will be created.

Notes
File Format Handling:

If you select MP3, the app will download only the audio and save it as an .mp3 file.
If you select MP4, the app will download the video (with audio) in MP4 format.
No Audio for MP4: If downloading MP4 but you don’t want audio, you can select MP4 (Video) and set the desired video quality (e.g., 720p).
Postprocessing and FFmpeg:
For MP3 format, FFmpeg is needed to convert the audio into the desired format.
To use FFmpeg, download and install it from the official FFmpeg site. Then, set the FFmpeg path in your system environment variables or in the app settings.
Error Handling:
If there is an error during the download, check the URL or select a different format or quality.

Advanced Settings

Using Different Formats:

If you want to download only the audio, select the MP3 format.
To download the entire video, select the MP4 format and set the desired quality.

FFmpeg for MP3:

If you are using FFmpeg for converting audio to MP3, you can download and configure FFmpeg in the settings.

Troubleshooting

FFmpeg Issue: If the application throws an error regarding missing FFmpeg, ensure that it is properly installed and added to your system's path.
URL Too Long: The application allows URLs up to 100 characters. If the URL exceeds this, the app will show a warning.
