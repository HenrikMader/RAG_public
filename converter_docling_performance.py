import os
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import granite_picture_description
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions
from docling.datamodel.pipeline_options import granite_picture_description
from docling.datamodel.accelerator_options import AcceleratorDevice, AcceleratorOptions


import argparse

# Add this near the top
parser = argparse.ArgumentParser()
parser.add_argument("--num_threads", type=int, default=1, help="Number of threads to use")
args = parser.parse_args()




# Specify the source directory containing the PDF files
source_directory = "./db_files_pdf_test"
output_directory = "./db_files_md"

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)


IMAGE_RESOLUTION_SCALE = 2.0



pipeline_options = PdfPipelineOptions()
#pipeline_options.do_picture_description = True
#pipeline_options.picture_description_options = (
#    granite_picture_description  # <-- the model choice
#)
#pipeline_options.picture_description_options.prompt = (
#    "Describe the image in three sentences. Be consise and accurate."
#)
#pipeline_options.images_scale = 2.0
#pipeline_options.generate_picture_images = True

accelerator_options = AcceleratorOptions(
    num_threads=args.num_threads, device=AcceleratorDevice.CPU
)

#accelerator_options = AcceleratorOptions(
#        num_threads=16, device=AcceleratorDevice.CPU
#    )

pipeline_options.accelerator_options = accelerator_options
pipeline_options.do_table_structure = True
pipeline_options.do_code_enrichment = True
pipeline_options.do_formula_enrichment = True



# Initialize the DocumentConverter
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
    },
)


# Loop through all files in the source directory
for file_name in os.listdir(source_directory):
    if file_name.endswith(".pdf"):  # Process only PDF files
        source_path = os.path.join(source_directory, file_name)
        print(f"Processing file: {source_path}")

        try:
            # Convert the PDF to a document
            result = converter.convert(source_path).document

            # Export the document to Markdown
            #markdown_content = result.document.export_to_markdown()

            # Define the output file path with .md extension
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            output_file_path = os.path.join(output_directory, output_file_name)
                
            result.save_as_markdown(filename=output_file_path)

            # Save the Markdown content to the output file
            #with open(output_file_path, 'w', encoding='utf-8') as f:
            #    f.write(markdown_content)

            print(f"Saved Markdown file: {output_file_path}")
        except Exception as e:
            print(f"Failed to process {source_path}: {e}")

print("All files processed!")
