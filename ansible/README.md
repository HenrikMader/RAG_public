# Ansible Installation scripts for the RAG demo

In this directory all files required to automatically set up the demo environment is located.

For a pure python installation the [rag-environment.yml](rag-environment.yml) contains a installable conda environment description (after adjusting the python version) and additional python packages that need to be installed via pip are located in the [requirements.txt](requirements.txt). 

The [example_inventory.yml](example-inventory.yml) File contains all configuration options for the ansible playbook in [rag-demo.yml](rag-demo.yml).

## Configurable Ansible parameters

### `ansible_user`

The username of the user on the ssh server. Under this user everything will be installed and, if
[auto_start](#auto_start) is set to true, the demo HTTP server will be ran under it.

###  `auto_start`

Setting `auto_start` to true will install the systemd service found under [systemd/](../systemd/). And automatically start it. 
When set to false the whole deployment - including filling out the template with ansible parameters - is skipped.


### `conda_dir`

The directory in which all conda (micromamba) prefixes live. When executing the conda/micromamba commands, the [root prefix](https://mamba.readthedocs.io/en/latest/user_guide/micromamba.html#quickstarts) configuration will be set to this value.

### `demo_port`

HTTP port for the Web Interface deployment.
This will set the `RAG_PORT` environment variable when executing [run_model.py](../run_model.py#L185).
Only used when [`auto_start`](#auto_start) is set to true.

### `micromamba_location`

The location of the micromamba *executable*! Will be placed there if not already present by the 
[micromamba installation playbook](download-and-extract-micromamba.yml)


### `model_name`

Filename of the model gguf file to load.

For example. The granite 3.2 8b model gguf export has the following huggingface repository: [bartowski/granite-3.1-8b-instruct-GGUF](https://huggingface.co/bartowski/ibm-granite_granite-3.2-8b-instruct-GGUF) in which multiple files are listed. The `model_name` would be the file name of the desired gguf file: `granite-3.1-8b-instruct-Q4_K_M.gguf`.

### `model_repository`

The huggingface repository containing the desired model gguf file.

E.g.: [bartowski/granite-3.1-8b-instruct-GGUF](https://huggingface.co/bartowski/ibm-granite_granite-3.2-8b-instruct-GGUF)

### `python_version`

The python version to use for the conda environment. The entire repository is tested with python up to 3.11 on powerpc64le.


### `working_directory`

The working directory und which all downloaded software and runtime artefacts will be stored.
After running the ansible script with `auto_start` enabled, this will include:
- A clone of this repository
- a folder `db/` under which ChromaDB stores its data
- The download of the model (gguf file) for inferencing.