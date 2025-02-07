import streamlit as st
import pytesseract
from PIL import Image
import io
import time


# Set Tesseract Path (Only needed if it's not detected)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# Set page layout
st.set_page_config(page_title="Screenshot to Text Extractor", layout="centered")

# Custom styling
st.markdown("""
    <style>
        .big-title {font-size: 36px; text-align: center; color: #0047AB; font-weight: bold;}
        .sub-title {font-size: 20px; text-align: center; color: #333;}
        .uploaded-image {border-radius: 10px; margin-top: 20px;}
        .download-button {margin-top: 10px;}
        .loading-circle {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 50px;
        }
        .loading-circle:after {
            content: "";
            width: 40px;
            height: 40px;
            border: 5px solid #0047AB;
            border-top: 5px solid #000;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }
        @keyframes spin {
            0% { transform: rotate(0deg); }
            100% { transform: rotate(360deg); }
        }
    </style>
""", unsafe_allow_html=True)

# Page title
st.markdown("<p class='big-title'>📸 Screenshot to Text Extractor</p>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Upload an image to extract text from it using OCR</p>", unsafe_allow_html=True)

# File Upload
uploaded_file = st.file_uploader("Upload an Image (PNG, JPG, JPEG)", type=["png", "jpg", "jpeg"])

if uploaded_file is not None:
    # Display Image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Extract text button
    if st.button("Extract Text 📝"):
        with st.container():
            st.markdown("<div class='loading-circle'></div>", unsafe_allow_html=True)
            time.sleep(2)  # Simulate processing time
        
        extracted_text = pytesseract.image_to_string(image)
        
        # Display extracted text
        st.text_area("Extracted Text", extracted_text, height=200)
        
        # Save as text file
        text_file = io.BytesIO()
        text_file.write(extracted_text.encode())
        text_file.seek(0)
        st.download_button("Download Extracted Text 📥", text_file, file_name="extracted_text.txt", mime="text/plain")
else:
    st.info("Please upload an image to extract text.")
