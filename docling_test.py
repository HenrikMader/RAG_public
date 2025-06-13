import logging
import os
from pathlib import Path

import requests
from docling_core.types.doc import PictureItem
from dotenv import load_dotenv

from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import (
    PdfPipelineOptions,
    PictureDescriptionApiOptions,
)
from docling.document_converter import DocumentConverter, PdfFormatOption


def vllm_local_options(model: str):
    options = PictureDescriptionApiOptions(
        url="http://localhost:11434/api/chat",
        params=dict(
            model=model,
            seed=42,
            max_completion_tokens=200,
        ),
        prompt="Describe the image in three sentences. Be consise and accurate.",
        timeout=90,
    )
    return options


def main():
    logging.basicConfig(level=logging.INFO)

    # ad-hoc input / output configuration
    input_doc_path = Path("2408.09869v5.pdf")
    output_markdown_path = Path("picture_descriptions.md")

    # Create the output directory if it doesn't exist
    output_markdown_path.parent.mkdir(parents=True, exist_ok=True)

    pipeline_options = PdfPipelineOptions(
        enable_remote_services=True  # <-- this is required!
    )
    pipeline_options.do_picture_description = True

    # The PictureDescriptionApiOptions() allows to interface with APIs supporting
    # the multi-modal chat interface. Here follow a few example on how to configure those.
    #
    # One possibility is self-hosting model, e.g. via VLLM.
    # $ vllm serve MODEL_NAME
    # Then PictureDescriptionApiOptions can point to the localhost endpoint.
    #
    # Example for the Granite Vision model: (uncomment the following lines)
    pipeline_options.picture_description_options = vllm_local_options(
        model="ibm-granite/granite3.2-vision:2b"
    )
    #
    # Example for the SmolVLM model: (uncomment the following lines)
    #pipeline_options.picture_description_options = vllm_local_options(
    #    model="HuggingFaceTB/SmolVLM-256M-Instruct"
    #)
    #
    # Another possibility is using online services, e.g. watsonx.ai.
    # Using requires setting the env variables WX_API_KEY and WX_PROJECT_ID.
    # Uncomment the following line for this option:

    doc_converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            )
        }
    )
    result = doc_converter.convert(input_doc_path)

    with open(output_markdown_path, "w", encoding="utf-8") as md_file:
        for element, _level in result.document.iterate_items():
            if isinstance(element, PictureItem):
                caption = element.caption_text(doc=result.document)
                annotations = element.annotations

                md_file.write(f"## Picture {element.self_ref}\n\n")
                md_file.write(f"**Caption:** {caption}\n\n")
                if annotations:
                    md_file.write("**Annotations:**\n")
                    for annotation in annotations:
                        md_file.write(f"- {annotation}\n")
                else:
                    md_file.write("**Annotations:** None\n\n")
                md_file.write("---\n\n")

    print(f"Picture descriptions written to: {output_markdown_path}")

if __name__ == "__main__":
    main()
