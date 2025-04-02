import os
from PyPDF2 import PdfReader
from PIL import Image
import fitz  # PyMuPDF

def extract_pdf_content(pdf_path, output_folder="extracted_images"):
    """Extracts text and images from a PDF file."""
    reader = PdfReader(pdf_path)
    text_data = []

    # Create output folder for images if not exists
    os.makedirs(output_folder, exist_ok=True)

    for page_idx, page in enumerate(reader.pages):
        text_data.append(f"Page {page_idx + 1}:\n{page.extract_text()}\n")

    # Extract images
    doc = fitz.open(pdf_path)
    for page_idx, page in enumerate(doc):
        for img_idx, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            img_data = doc.extract_image(xref)
            img_bytes = img_data["image"]
            img_ext = img_data["ext"]
            img_path = os.path.join(output_folder, f"page_{page_idx+1}_img_{img_idx+1}.{img_ext}")

            with open(img_path, "wb") as f:
                f.write(img_bytes)

    return "\n\n".join(text_data)

# Example usage
if __name__ == "__main__":
    pdf_file = "example.pdf"  # Replace with your actual file path
    extracted_text = extract_pdf_content(pdf_file)
    print(extracted_text)
