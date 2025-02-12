import os
import re
import shutil

def extract_resumename(tex_file):
    """Extract the desired PDF name from the first line of the .tex file."""
    with open(tex_file, 'r') as file:
        first_line = file.readline().strip()
        # Check if the first line starts with '%' and ends with '.pdf'
        if first_line.startswith('%') and first_line.endswith('.pdf'):
            # Remove the leading '%' and trailing '.pdf', then strip whitespace
            return first_line[1:].rstrip('.pdf').strip()
    return None

def copy_pdf_with_resumename(templates_dir, build_dir, out_dir):
    """Copy PDF files to the 'pdfs' directory with the name from the first line."""
    for root, _, files in os.walk(templates_dir):
        for file in files:
            if file.endswith('.tex'):
                tex_file_path = os.path.join(root, file)
                resumename = extract_resumename(tex_file_path)
                if resumename:
                    # Construct the original PDF file name
                    pdf_file_name = os.path.splitext(file)[0] + '.pdf'
                    pdf_file_path = os.path.join(build_dir, pdf_file_name)

                    # Construct the new PDF file path in the 'pdfs' directory
                    new_pdf_file_path = os.path.join(out_dir, f"{resumename}.pdf")

                    # Copy the PDF file to the 'pdfs' directory with the new name
                    if os.path.exists(pdf_file_path):
                        shutil.copy(pdf_file_path, new_pdf_file_path)
                        print(f"Copied {pdf_file_path} to {new_pdf_file_path}")
                    else:
                        print(f"PDF file not found: {pdf_file_path}")

if __name__ == "__main__":
    # Define directories
    templates_dir = os.path.join(os.path.dirname(__file__), 'templates')
    build_dir = os.path.join(os.path.dirname(__file__), 'build')
    out_dir = os.path.join(os.path.dirname(__file__), 'pdfs')

    # Create the 'pdfs' directory if it doesn't exist
    os.makedirs(out_dir, exist_ok=True)

    # Run the function to copy PDF files
    copy_pdf_with_resumename(templates_dir, build_dir, out_dir)