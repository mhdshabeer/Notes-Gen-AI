# src/main.py

import os
import shutil
import streamlit as st
from extract_text import extract_text
from extract_images import extract_images

# Helper function to clear the temporary input directory
def clear_input_directory(input_dir):
    if os.path.exists(input_dir):
        shutil.rmtree(input_dir)
    os.makedirs(input_dir)

# Streamlit App
def main():
    st.title("Perfect Note Generator 📝")
    st.write("Upload multiple PowerPoint (.pptx) or PDF (.pdf) files to extract text and images.")

    # Temporary directories for uploads and extracted data
    input_dir = "../input_files/"
    text_output_dir = "../extracted_data/text/"
    images_output_dir = "../extracted_data/images/"

    # Clear input directory at the start of each session
    clear_input_directory(input_dir)

    # File uploader (multiple files allowed)
    uploaded_files = st.file_uploader(
        "Upload .pptx or .pdf files", type=["pptx", "pdf"], accept_multiple_files=True
    )

    if uploaded_files:
        st.write(f"Uploaded {len(uploaded_files)} file(s):")
        for uploaded_file in uploaded_files:
            st.write(f"- {uploaded_file.name}")

        # Save uploaded files to the input directory
        for uploaded_file in uploaded_files:
            file_path = os.path.join(input_dir, uploaded_file.name)
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())

        # Process the uploaded files
        if st.button("Extract Text and Images"):
            st.write("Processing files...")

            for uploaded_file in uploaded_files:
                file_name = uploaded_file.name
                file_path = os.path.join(input_dir, file_name)

                st.write(f"Processing: {file_name}")
                
                # Extract text
                try:
                    extract_text(file_path, text_output_dir)
                    st.success(f"Text extraction complete for {file_name}")
                except Exception as e:
                    st.error(f"Failed to extract text from {file_name}: {e}")

                # Extract images
                try:
                    extract_images(file_path, images_output_dir)
                    st.success(f"Image extraction complete for {file_name}")
                except Exception as e:
                    st.error(f"Failed to extract images from {file_name}: {e}")

            st.write("All files processed successfully!")

if __name__ == "__main__":
    main()