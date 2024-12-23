from Url_to_Frame import main1
from Detect_Object import main2


# Url to keyframe processing
def url_to_keyframe(url):
    return main1(url)
    
# keyframe to Object detection 
def keyframe_to_object(title):
    main2(title)
   
    
def main(url):
    keyframe_to_object(url_to_keyframe(video_url))

if __name__ == "__main__":
    video_url = "https://youtu.be/GKAf4sV3-GQ?si=u9o14D9dzs-z0QAg"
    main(video_url)
    
