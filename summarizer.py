import os
from dotenv import load_dotenv
import google.generativeai as genai
from utils.youtube import get_transcript
from utils.chunking import chunk_text

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

PROMPT = """
You are a professional tech article writer.

Convert the following YouTube transcript into a HIGH QUALITY article.

RULES:
- Remove intro, outro, promotions
- Focus only on useful technical content
- Use clean structure

FORMAT:
- Title
- Introduction
- Sections with headings
- Bullet points
- Code blocks if needed
- Conclusion

Transcript:
{content}
"""

def generate_article_from_chunk(chunk):
    response = model.generate_content(PROMPT.format(content=chunk))
    return response.text

def generate_article(url):
    transcript = get_transcript(url)

    # Short video
    if len(transcript) < 4000:
        return generate_article_from_chunk(transcript)

    # Long video → chunking
    chunks = chunk_text(transcript)

    final_article = ""
    for chunk in chunks:
        part = generate_article_from_chunk(chunk)
        final_article += "\n\n" + part

    return final_article