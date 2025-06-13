from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption

IMAGE_RESOLUTION_SCALE = 2.0

pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = IMAGE_RESOLUTION_SCALE
pipeline_options.generate_picture_images = True

doc_converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
    },
)

source = "https://arxiv.org/pdf/2408.09869"  # document per local path or URL
doc = doc_converter.convert(source, page_range=(1, 3)).document

print(doc.export_to_markdown(image_mode=ImageRefMode.EMBEDDED))
# doc.save_as_markdown(filename="output.md", image_mode=ImageRefMode.EMBEDDED)
