from fpdf import FPDF


def clean_text(text):
    # Replace problematic unicode characters
    replacements = {
        "—": "-",
        "–": "-",
        "“": '"',
        "”": '"',
        "‘": "'",
        "’": "'",
        "•": "-",
    }

    for k, v in replacements.items():
        text = text.replace(k, v)

    # Remove unsupported characters
    return text.encode("latin-1", "ignore").decode("latin-1")


def save_pdf(text, filename="outputs/article.pdf"):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    text = clean_text(text)

    for line in text.split("\n"):
        pdf.multi_cell(0, 8, line)

    pdf.output(filename)