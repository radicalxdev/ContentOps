import os
import glob
import json
import yaml
import argparse

def json_to_yaml(json_file_path, yaml_file_path):
    # Read the JSON file
    with open(json_file_path, 'r') as json_file:
        data = json.load(json_file)
    
    # Write the data to a YAML file
    with open(yaml_file_path, 'w') as yaml_file:
        yaml.dump(data, yaml_file, default_flow_style=False)

    print(f"Converted {json_file_path} to {yaml_file_path}")

def convert_all_json_to_yaml(root_dir):
    # Traverse the directory
    for json_file_path in glob.glob(os.path.join(root_dir, '**', '*.json'), recursive=True):
        # Replace the file extension from .json to .yaml
        yaml_file_path = os.path.splitext(json_file_path)[0] + '.yaml'
        # Convert the JSON file to YAML
        json_to_yaml(json_file_path, yaml_file_path)

def convert_single_json_to_yaml(json_file_path):
    # Replace the file extension from .json to .yaml
    yaml_file_path = os.path.splitext(json_file_path)[0] + '.yaml'
    # Convert the JSON file to YAML
    json_to_yaml(json_file_path, yaml_file_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to YAML")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to a single JSON file")
    group.add_argument('-d', '--directory', type=str, help="Root directory containing JSON files")
    args = parser.parse_args()

    if args.file:
        convert_single_json_to_yaml(args.file)
    else:
        convert_all_json_to_yaml(args.directory)