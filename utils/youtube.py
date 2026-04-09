from youtube_transcript_api import YouTubeTranscriptApi


def extract_video_id(url):
    if "watch?v=" in url:
        return url.split("watch?v=")[-1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL")


def get_transcript(url):
    video_id = extract_video_id(url)

    try:
        transcript = YouTubeTranscriptApi().fetch(video_id)

        text = " ".join([t.text for t in transcript])
        return text

    except Exception as e:
        return f"Error fetching transcript: {str(e)}"