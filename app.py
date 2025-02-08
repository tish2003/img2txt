import streamlit as st
import pytesseract
from PIL import Image
import os
import json

# Define database for storing notes
NOTES_DB = "notes.json"

def load_notes():
    if os.path.exists(NOTES_DB):
        with open(NOTES_DB, "r") as f:
            return json.load(f)
    return {}

def save_notes(notes):
    with open(NOTES_DB, "w") as f:
        json.dump(notes, f, indent=4)

# Load existing notes
db = load_notes()

# Streamlit UI
st.title("📄 SnapOCR - Lecture Notes Organizer")
st.write("Upload lecture notes and search them using OCR!")

# File Upload
uploaded_file = st.file_uploader("Upload Lecture Notes (Image/PDF)", type=["png", "jpg", "jpeg", "pdf"])

def extract_text(image):
    return pytesseract.image_to_string(image)

if uploaded_file:
    image = Image.open(uploaded_file)
    extracted_text = extract_text(image)
    
    note_id = str(len(db) + 1)
    db[note_id] = extracted_text
    save_notes(db)
    
    st.success("Text extracted and saved!")
    st.text_area("Extracted Text", extracted_text, height=200)

# Search Feature
st.subheader("🔍 Search Notes")
query = st.text_input("Enter keyword to search notes:")
if query:
    results = {k: v for k, v in db.items() if query.lower() in v.lower()}
    if results:
        for note_id, content in results.items():
            st.write(f"**Note {note_id}:**")
            st.text_area("Snippet", content[:300])
    else:
        st.warning("No matching notes found!")
