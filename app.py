import os
from youtube_transcript_api import YouTubeTranscriptApi
from google import genai
from google.genai import types
from fastapi import FastAPI
import json
import re

app = FastAPI()
# Gemini summary function
def generate_summary_from_transcript(transcript_text):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    prompt = f"""Based on the following YouTube transcription, return me a brief summary of the topic in the below JSON format only:

{transcript_text}

```json
{{
  "topic_name": "name of the topic",
  "topic_summary": "summary of the topic"
}}
```"""

    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=prompt)
            ]
        )
    ]

    generate_content_config = types.GenerateContentConfig(
        temperature=0.5,
        response_mime_type="text/plain",
    )

    response = client.models.generate_content(
        model=model,
        contents=contents,
        config=generate_content_config,
    )
    return response.text


def extract_youtube_id(url):
    if "youtube.com/watch?v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("/")[-1]
    else:
        raise ValueError("Invalid YouTube URL format.")




def extract_json_from_gemini_response(response_text):
    """
    Extracts and parses JSON from a Gemini response string that includes markdown code blocks.
    """
    # Remove triple backticks and anything after ```json or ``` or ```json\n
    cleaned_text = re.sub(r"```json\s*|\s*```", "", response_text.strip())

    try:
        json_obj = json.loads(cleaned_text)
        return json_obj
    except json.JSONDecodeError as e:
        print("Failed to decode JSON:", e)
        return None


# Fetch and summarize transcript
def main():
    # video_id = "uthjpYKD7Ng"
    video_id = extract_youtube_id("https://www.youtube.com/watch?v=uthjpYKD7Ng")

    try:
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=["en-IN", "en", "hi"])
        full_text = " ".join([entry["text"] for entry in transcript_data])
        summary = generate_summary_from_transcript(full_text)
        print(summary)
    except Exception as e:
        print("Error:", e)

@app.get("/summarize")
def summarize_video(url: str):
    try:
        video_id = extract_youtube_id(url)
        transcript_data = YouTubeTranscriptApi.get_transcript(video_id, languages=["en-IN", "en", "hi"])
        full_text = " ".join([entry["text"] for entry in transcript_data])
        summary = generate_summary_from_transcript(full_text)
        return extract_json_from_gemini_response(summary)
    except Exception as e:
        return {"error": str(e)}
