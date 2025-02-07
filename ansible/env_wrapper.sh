#!/usr/bin/env bash
# this wrapper is required to wrap micromamba calls in a nphup context.
# I'm not exactly sure why but this works and without it the commands passed to micromamba do
# not seem to even start running when executed through nohup.

export MAMBA_ROOT_PREFIX=%{ conda_dir }%
eval "$(micromamba shell hook --shell bash)"
micromamba activate rag-demo

# run commands:
$@

micromamba deactivate