import os
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.settings import settings

# Ask the user for input and output directories
source_directory = input("Enter the path to the input folder (containing PDF files): ").strip()
output_directory = input("Enter the path to the output folder (for Markdown files): ").strip()

# Expand ~ and make sure the paths are absolute
source_directory = os.path.abspath(os.path.expanduser(source_directory))
output_directory = os.path.abspath(os.path.expanduser(output_directory))

# Validate the input directory
if not os.path.isdir(source_directory):
    print(f"Error: The input directory '{source_directory}' does not exist.")
    exit(1)

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

print(f"\n📂 Input folder: {source_directory}")
print(f"📝 Output folder: {output_directory}\n")

# Initialize the PDF pipeline options
pipeline_options = PdfPipelineOptions()

# Initialize the DocumentConverter
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
    },
)

# Process all PDF files in the source directory
for file_name in os.listdir(source_directory):
    if file_name.lower().endswith(".pdf"):
        source_path = os.path.join(source_directory, file_name)
        print(f"Processing file: {source_path}")

        try:
            settings.debug.profile_pipeline_timings = True

            # Convert the PDF
            result = converter.convert(source_path).document

            # Export to Markdown
            md_content = result.export_to_markdown()

            # Save to the output directory
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            output_file_path = os.path.join(output_directory, output_file_name)

            with open(output_file_path, "w", encoding="utf-8") as f:
                f.write(md_content)

            print(f"✅ Saved Markdown: {output_file_path}\n")

        except Exception as e:
            print(f"❌ Failed to process {source_path}: {e}\n")

print("🎉 All files processed successfully!")

