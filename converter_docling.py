import os
from docling.document_converter import DocumentConverter

# Specify the source directory containing the PDF files
source_directory = "./db_files_pdf/"
output_directory = "./db_files_md/"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Initialize the DocumentConverter
converter = DocumentConverter()

# Loop through all files in the source directory
for file_name in os.listdir(source_directory):
    if file_name.endswith(".pdf"):  # Process only PDF files
        source_path = os.path.join(source_directory, file_name)
        print(f"Processing file: {source_path}")

        try:
            # Convert the PDF to a document
            result = converter.convert(source_path)

            # Export the document to Markdown
            markdown_content = result.document.export_to_markdown()

            # Define the output file path with .md extension
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            output_file_path = os.path.join(output_directory, output_file_name)

            # Save the Markdown content to the output file
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)

            print(f"Saved Markdown file: {output_file_path}")
        except Exception as e:
            print(f"Failed to process {source_path}: {e}")

print("All files processed!")
