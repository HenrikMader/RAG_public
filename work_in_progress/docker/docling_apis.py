import os
from fastapi import FastAPI, HTTPException, Query
from pydantic import BaseModel
from typing import List
from docling_core.types.doc import ImageRefMode
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.pipeline_options import granite_picture_description
from docling.datamodel.settings import settings

# FastAPI app
app = FastAPI(title="Flexible PDF to Markdown Converter API")

# PDF converter setup
pipeline_options = PdfPipelineOptions()
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options),
    },
)

# ========== Models ==========

class ConvertRequest(BaseModel):
    source_folder: str
    output_folder: str

class DeleteFilesRequest(BaseModel):
    folder: str
    filenames: List[str]

# ========== API Routes ==========

@app.post("/convert-pdfs")
def convert_pdfs(request: ConvertRequest):
    """
    Convert all PDFs from the source folder to Markdown in the output folder.
    """
    source_folder = request.source_folder
    output_folder = request.output_folder

    if not os.path.exists(source_folder):
        raise HTTPException(status_code=400, detail="Source folder does not exist")

    os.makedirs(output_folder, exist_ok=True)

    converted_files = []

    for file_name in os.listdir(source_folder):
        if file_name.endswith(".pdf"):
            source_path = os.path.join(source_folder, file_name)
            output_file_name = os.path.splitext(file_name)[0] + ".md"
            output_file_path = os.path.join(output_folder, output_file_name)

            try:
                print(f"Processing file: {source_path}")
                settings.debug.profile_pipeline_timings = True
                result = converter.convert(source_path).document
                md = result.export_to_markdown()
                with open(output_file_path, "w", encoding="utf-8") as f:
                    f.write(md)
                print(f"Saved Markdown to: {output_file_path}")
                converted_files.append(output_file_name)
            except Exception as e:
                print(f"Failed to process {source_path}: {e}")

    return {"converted_files": converted_files}


@app.get("/list-md-files")
def list_md_files(folder: str = Query(..., description="Path to the folder containing Markdown files")):
    """
    List all Markdown (.md) files in the given folder.
    """
    if not os.path.exists(folder):
        raise HTTPException(status_code=400, detail="Folder does not exist")

    try:
        files = [
            f for f in os.listdir(folder)
            if os.path.isfile(os.path.join(folder, f)) and f.endswith(".md")
        ]
        return files
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.delete("/delete-md-files")
def delete_md_files(request: DeleteFilesRequest):
    """
    Delete specified Markdown files from the given folder.
    """
    deleted = []
    not_found = []

    if not os.path.exists(request.folder):
        raise HTTPException(status_code=400, detail="Folder does not exist")

    for filename in request.filenames:
        file_path = os.path.join(request.folder, filename)
        if os.path.exists(file_path):
            os.remove(file_path)
            deleted.append(filename)
        else:
            not_found.append(filename)

    return {"deleted": deleted, "not_found": not_found}


@app.get("/preview-md-file/{filename}")
def preview_md_file(filename: str, folder: str = Query(..., description="Folder where the Markdown file is located")):
    """
    Return the first 150 words from a specified Markdown file in the given folder.
    """
    file_path = os.path.join(folder, filename)

    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="File not found")

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        words = content.split()
        preview = " ".join(words[:150])
        return {"filename": filename, "preview": preview}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
