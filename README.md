# ContentOps Repository
This repository is dedicated to Content Operations (ContentOps), focusing on the creation and management of YAML and JSON files that power the content. The repository includes several Python scripts that help in compiling, validating, and converting these files.

`full_compile.py`
The full_compile.py script is used to compile and validate a TaskGraph from a YAML file. This script takes the path to a YAML file as a command-line argument and validates the graph by compiling it.

## Usage
To use `full_compile.py`, you need to pass the path to a YAML file as a command-line argument.

Here is the general command format:

Replace <yaml_file_path> with the path to your YAML file.

For example, if your YAML file is located at recipes/demo_module/expedition.yaml, you would run: 
```
python full_compile.py recipes/demo_module/expedition.yaml
```

YAML_JSON_converter.py
The YAML_JSON_converter.py script is used to convert all YAML files in a specified folder to JSON files. This script takes the path to a folder as a command-line argument and converts all YAML files in that folder to JSON.


## Usage
To use `YAML_JSON_converter.py`, you need to pass the path to a folder as a command-line argument.

Here is the general command format:

Replace <folder_path> with the path to your folder.

For example, if your folder is located at recipes/demo_module, you would run:
```
python YAML_JSON_converter.py recipes/demo_module
```

JSON_to_YAML.py
The JSON_to_YAML.py script is used to convert a JSON file to a YAML file. This script takes the paths to a JSON file and a YAML file as command-line arguments and converts the JSON file to YAML.


## Usage
To use JSON_to_YAML.py, you need to pass the paths to a JSON file and a YAML file as command-line arguments.

Here is the general command format:

Replace <json_file_path> and <yaml_file_path> with the paths to your JSON and YAML files.

For example, if your JSON file is located at recipes/demo_module/expedition.json and you want to convert it to recipes/demo_module/expedition.yaml, you would run:
```
python JSON_to_YAML.py recipes/demo_module/expedition.json recipes/demo_module/expedition.yaml
```
Final Output
The final expected outputs are a valid YAML file compiled with the full compiler and a corresponding JSON file. These files should be packaged together in a .zip file.