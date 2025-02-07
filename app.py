import streamlit as st
import pytesseract
from PIL import Image
import io

st.set_page_config(page_title="Screenshot-to-Text Extractor", layout="wide")

st.title("📸 Screenshot to Text Extractor")

uploaded_file = st.file_uploader("Upload an image", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Open the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Screenshot", use_column_width=True)

    # Extract text
    text = pytesseract.image_to_string(image)
    
    st.subheader("Extracted Text")
    st.text_area("Text Output", text, height=200)

    # Save text file
    text_filename = "extracted_text.txt"
    text_bytes = io.BytesIO(text.encode())
    st.download_button(label="📥 Download Text", data=text_bytes, file_name=text_filename, mime="text/plain")
