import fitz  # PyMuPDF
from PIL import Image

# Define the path to your PDF file
pdf_path = 'cardio.pdf'

# Open the PDF file
pdf_document = fitz.open(pdf_path)

# Iterate through each page in the PDF
for i in range(min(17, pdf_document.page_count)):
    # Select the page
    page = pdf_document[i]
    # Render the page to a pixmap (image)
    pix = page.get_pixmap(dpi=300)  # Set dpi to 300 for higher quality
    # Convert the pixmap to an Image object
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
    # Save the image with the specified name format
    img.save(f'cardio_{i+1}.jpg', 'JPEG', quality=100)

print("Conversion complete!")
