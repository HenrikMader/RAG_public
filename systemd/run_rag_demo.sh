#!/usr/bin/env bash
set -eou pipefail

RAG_MODEL_PATH=%{ working_directory }%/model/%{ model_name }% micromamba run -n rag-demo -r %{ conda_dir }% python %{ working_directory }%/repo/run_model.py