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

## YAML_JSON_converter.py
The YAML_JSON_converter.py script is used to convert YAML files to JSON files. This script can accept either a single YAML file or a directory containing multiple YAML files as input. You can also specify the output path for the converted JSON file.

### Usage
To use `YAML_JSON_converter.py`, you can pass either a single YAML file or a directory as a command-line argument.

Replace `<yaml_file_path>` with the path to your YAML file and `<json_file_path>` with the desired path to the output JSON file.

Replace `<folder_path>` with the path to the directory containing the YAML files you want to convert. The script will convert all YAML files in the directory to JSON files with the same name, but with a `.json` extension, in the same directory.

### Converting a single YAML file
```sh
python YAML_JSON_converter.py -f <yaml_file_path> -o <json_file_path>
```
This will convert the specified YAML file to a JSON file at the specified output path.

### Converting all YAML files in a directory
```sh
python YAML_JSON_converter.py -d <folder_path>
```
This will convert all YAML files in the specified directory to JSON files in the same directory. 

Please replace <yaml_file_path>, <json_file_path>, and <folder_path> with the actual paths when you run the commands.


## JSON to YAML
To use JSON_to_YAML.py, you need to pass the paths to a JSON file and a YAML file as command-line arguments.

Here is the general command format:

Replace <json_file_path> and <yaml_file_path> with the paths to your JSON and YAML files.

For example, if your JSON file is located at recipes/demo_module/expedition.json and you want to convert it to recipes/demo_module/expedition.yaml, you would run:
```
python JSON_to_YAML.py recipes/demo_module/expedition.json recipes/demo_module/expedition.yaml
```
Final Output
The final expected outputs are a valid YAML file compiled with the full compiler and a corresponding JSON file. These files should be packaged together in a .zip file.