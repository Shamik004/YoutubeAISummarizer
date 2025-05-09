# 🎬 YouTube Video Summarizer using Gemini API

This is a FastAPI-based web service that takes a YouTube video URL, extracts its transcript, and generates a concise summary using **Google Gemini (Gemini 2.0 Flash model)**.

---

## 🚀 Features

- ✅ Extracts transcript from YouTube videos via `youtube-transcript-api`
- 🧠 Summarizes transcript using Google's Gemini model
- ⚡ FastAPI endpoint for real-time summarization
- 🌐 Supports multiple YouTube URL formats
- 🗣️ Works with English (`en`), Indian English (`en-IN`), and Hindi (`hi`) transcripts

---

## 🛠 Tech Stack

- Python 3.8+
- FastAPI
- Google Generative AI (Gemini)
- YouTube Transcript API
- Uvicorn (for local server)
- Python Dotenv (for managing environment variables)

---

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Shamik004/YoutubeAISummarizer.git
   cd YoutubeAISummarizer

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Create a `.env` file**

   ```env
   GEMINI_API_KEY=your-gemini-api-key-here
   ```

4. **Run the FastAPI app**

   ```bash
   uvicorn app:app --reload
   ```

---

## 🧪 Usage

### Local Testing

Start the server and visit:
```
GET /summarize?url=https://www.youtube.com/watch?v=VIDEO_ID
```

Replace `VIDEO_ID` with any valid YouTube video ID or full YouTube URL.

### Example

```
GET http://127.0.0.1:8000/summarize?url=https://www.youtube.com/watch?v=uthjpYKD7Ng
```

### Sample Response

```json
{
    "topic_name": "Pythagorean Theorem",
    "topic_summary": "The video explains how to find the length of the hypotenuse (X) of a right triangle using the Pythagorean theorem (a² + b² = c²). Given the lengths of the legs (6 and 8), the equation 6² + 8² = x² is solved to find that x = 10."
}
```

---

## 📁 Project Structure

```
.
├── main.py             # FastAPI app and Gemini logic
├── requirements.txt    # Project dependencies
├── .env                # (Not tracked) Environment variable file
└── README.md           # Project overview
```

---

## ⚠️ Notes

* Transcript will only be fetched if it's publicly available for the video and supported in specified languages.
* You may encounter errors if the video has no captions/transcripts enabled.

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).

---

## 🙋‍♂️ Author

**Shamik**
📧 [Email](mailto:shamik.bardhan2004@gmail.com)