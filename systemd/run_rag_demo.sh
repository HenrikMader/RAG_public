#!/usr/bin/env bash
set -eou pipefail

# NOTE: the relative path is important for run_model to find the DB (in its current state.)
cd %{ working_directory }%/repo
RAG_MODEL_PATH=%{ working_directory }%/model/%{ model_name }% %{ micromamba_location }% run -n rag-demo -r %{ conda_dir }% python run_model.py