import streamlit as st
from summarizer import generate_article
from webpage_generator import generate_html
from utils.pdf_generator import save_pdf
import os

st.set_page_config(page_title="YouTube → Article", layout="centered")

st.title("🎥 YouTube → Article + PDF Generator")

url = st.text_input("Enter YouTube URL")

if st.button("Generate Article"):
    if not url:
        st.warning("Please enter a URL")
    else:
        with st.spinner("Processing..."):

            article = generate_article(url)

            # Save outputs
            if not os.path.exists("outputs"):
                os.makedirs("outputs")

            # Save PDF
            save_pdf(article)

            # Save HTML
            html = generate_html(article)
            with open("outputs/article.html", "w", encoding="utf-8") as f:
                f.write(html)

        st.success("Done!")

        st.subheader("📄 Article")
        st.write(article)

        # Download PDF
        with open("outputs/article.pdf", "rb") as f:
            st.download_button("Download PDF", f, "article.pdf")

        # Download HTML
        with open("outputs/article.html", "rb") as f:
            st.download_button("Download HTML", f, "article.html")