import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
from colorama import init, Fore, Style
from video_downloader import Video
import os
import requests
import getopt
import sys
from random import choice
from tqdm import tqdm
import ffmpeg

class BitviewDownloaderApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bitview Downloader")

        # URL input
        self.url_label = tk.Label(root, text="Enter Bitview Video URL:")
        self.url_label.pack()
        self.url_entry = tk.Entry(root, width=50)
        self.url_entry.pack()

        # Quality selection
        self.quality_label = tk.Label(root, text="Select Quality:")
        self.quality_label.pack()
        self.quality_var = tk.StringVar(root)
        self.quality_var.set("360")  # Default quality
        self.qualities = {"144": "144p", "240": "240p", "360": "360p"}
        self.quality_menu = tk.OptionMenu(root, self.quality_var, *self.qualities.values())
        self.quality_menu.pack()

        # Location selection
        self.location_label = tk.Label(root, text="Save Location:")
        self.location_label.pack()
        self.location_entry = tk.Entry(root, width=50)
        self.location_entry.pack()
        self.location_button = tk.Button(root, text="Browse", command=self.browse_location)
        self.location_button.pack()

        # Download button
        self.download_button = tk.Button(root, text="Download", command=self.download_video)
        self.download_button.pack()

    def browse_location(self):
        location = filedialog.askdirectory()
        if location:
            self.location_entry.delete(0, tk.END)
            self.location_entry.insert(0, location)

    def download_video(self):
        url = self.url_entry.get()
        quality = self.quality_var.get()
        location = self.location_entry.get()
        try:
            video = Video(url, src="hd", location=location)
            video.downloadVid(silent=1)
            messagebox.showinfo("Download Complete", "Video downloaded successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")

def main():
    init()  # Initialize colorama
    root = tk.Tk()
    app = BitviewDownloaderApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
