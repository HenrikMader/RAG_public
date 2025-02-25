#!/usr/bin/env bash
set -eou pipefail

cd %{ working_directory }%
RAG_MODEL_PATH=model/%{ model_name }% micromamba run -n rag-demo -r %{ conda_dir }% python repo/run_model.py