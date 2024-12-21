import os
import cv2
import json
import urllib.request
import urllib.parse
import yt_dlp
import re 

class VideoProcessor:
    def __init__(self, video_url):
        self.video_url = video_url
        self.stream_url = None
        self.title_folder_name = ""

    def download_video_stream(self):
        # Create options for yt-dlp
        ydl_opts = {
            'format': 'best',
            'quiet': True,
            'noplaylist': True,
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            # Extract video information
            info_dict = ydl.extract_info(self.video_url, download=False)
            # Get the best video URL
            self.stream_url = info_dict['url']
    def get_video_title(self):
        # Prepare the oEmbed API request
        params = {"format": "json", "url": self.video_url}
        url = "https://www.youtube.com/oembed"
        
        # Create query string
        query_string = urllib.parse.urlencode(params)
        full_url = f"{url}?{query_string}"

        try:
            # Make the request and parse JSON response
            with urllib.request.urlopen(full_url) as response:
                data = json.loads(response.read().decode())
                self.title_folder_name = re.sub(r'[^a-zA-Z0-9 ]', '',data['title'].split('|')[0].strip()).replace(' ', '_')
                
            # Clean up the title for folder name usage
            return self.title_folder_name
        
        except Exception as e:
            print(f"Error fetching video title: {e}")
            return None

    def extract_keyframes(self):
        # Ensure the stream URL is available
        if not self.stream_url:
            print("Error: Stream URL not available. Please download the video stream first.")
            return
        
        # Open the video stream
        cap = cv2.VideoCapture(self.stream_url)

        if not cap.isOpened():
            print("Error: Could not open video.")
            return

        # Define main folder and subfolder paths
        main_folder = "Movie Frame"
        title_folder = os.path.join(main_folder, self.title_folder_name, "Key_Frame")

        # Create the entire directory structure
        os.makedirs(title_folder, exist_ok=True)

        frame_count = 0
        keyframes = []
        count = 1

        while True:
            success, frame = cap.read()
            if not success:
                break
            
            # Save every nth frame as a keyframe (e.g., every 30th frame)
            if frame_count % 100 == 0:  # Adjust this value as needed
                keyframes.append(frame)
                cv2.imwrite(os.path.join(title_folder, f'img_{count}.jpg'), frame)  # Save keyframe as an image
                count += 1
            
            frame_count += 1

        cap.release()
        print(f"Extracted {len(keyframes)} keyframes to {title_folder}.")

# Example usage
def main1(video_url):
    # video_url = "https://youtu.be/tOM-nWPcR4U"  # Replace with your YouTube URL
    processor = VideoProcessor(video_url)
    processor.download_video_stream()
    title=processor.get_video_title()
    processor.extract_keyframes()
    return title

# if __name__ == "__main1__":
#     video_url = "https://youtu.be/tOM-nWPcR4U"  # Replace with your YouTube URL
#     main1(video_url)

