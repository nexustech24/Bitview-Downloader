import requests
import os
from tqdm import tqdm

class Video:
    def __init__(self, url, location=None, src="hd"):
        self.url = url
        self.location = location
        self.src = src

        # Check if the URL contains a video ID
        if "bitview.net" in self.url and "v=" in self.url:
            parts = self.url.split("v=")
            if len(parts) > 1:
                self.video_id = parts[-1]
            else:
                self.video_id = None

            if self.video_id:
                # Construct the video URL with the video ID
                self.url = f"https://www.bitview.net/m/video.php?v={self.video_id}"
        else:
            self.video_id = None

    def download(self):
        try:
            # Retrieve the video file from the URL
            response = requests.get(self.url, stream=True)
            total_size = int(response.headers.get('content-length', 0))

            # Determine the file name
            filename = os.path.basename(self.url)
            if not filename:
                filename = 'video.mp4'

            # Determine the save location
            if self.location:
                save_path = os.path.join(self.location, filename)
            else:
                save_path = filename

            # Check if the file already exists
            if os.path.exists(save_path):
                print("File already exists. Skipping download.")
                return save_path

            # Download the video file
            with open(save_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading', leave=False) as pbar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

            print("Download complete.")
            return save_path

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

    def downloadVid(self, overwrite=0, silent=0):
        try:
            # Retrieve the video file from the URL
            response = requests.get(self.url, stream=True)
            total_size = int(response.headers.get('content-length', 0))

            # Sanitize video ID for use as filename
            filename = f"{self.video_id}.mp4"

            # Determine the save location
            if self.location:
                save_path = os.path.join(self.location, filename)
            else:
                save_path = filename

            # Check if the file already exists
            if os.path.exists(save_path) and not overwrite:
                print("File already exists. Skipping download.")
                return save_path

            # Download the video file
            with open(save_path, 'wb') as f:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc='Downloading', leave=False) as pbar:
                    for chunk in response.iter_content(chunk_size=1024):
                        if chunk:
                            f.write(chunk)
                            pbar.update(len(chunk))

            print("Download complete.")
            return save_path

        except Exception as e:
            print(f"An error occurred: {str(e)}")
            return None

# Example usage:
if __name__ == "__main__":
    # Example Bitview URL with video ID
    url = "https://www.bitview.net/m/video.php?v="

    # Create a Video object and initiate download
    video = Video(url)
    video.downloadVid()
