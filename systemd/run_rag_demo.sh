#!/usr/bin/env bash
set -eou pipefail

# NOTE: the relative path is important for run_model to find the DB (in its current state.)
port="%{ demo_port }%"
if [ "$port" -eq "$port" ]; then
    echo "port given."
else
    echo "using standard port 7680"
    port=7680
fi
cd %{ working_directory }%/repo
RAG_MODEL_PATH=%{ working_directory }%/model/%{ model_name }% RAG_PORT="$port" %{ micromamba_location }% run -n rag-demo -r %{ conda_dir }% python run_model.py