import yaml
import json
import os
import argparse

def yaml_to_json(file_path, output_path=None):
    try:
        # Load the YAML file
        with open(file_path, 'r') as yf:
            yaml_content = yaml.safe_load(yf)
        
        # Determine the output path
        if output_path is None:
            json_file_path = file_path.rsplit('.', 1)[0] + '.json'
        else:
            json_file_path = output_path
        
        # Write the content to a JSON file
        with open(json_file_path, 'w') as jf:
            json.dump(yaml_content, jf, indent=4)
        
        print(f"Successfully converted {file_path} to {json_file_path}")
    
    except Exception as e:
        print(f"Error occurred: {e}")

def yaml_to_json_in_folder(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        
        # Filter out only YAML files
        yaml_files = [file for file in files if file.endswith('.yaml') or file.endswith('.yml')]
        
        for yaml_file in yaml_files:
            yaml_file_path = os.path.join(folder_path, yaml_file)
            json_file_path = os.path.join(folder_path, yaml_file.rsplit('.', 1)[0] + '.json')
            
            yaml_to_json(yaml_file_path, json_file_path)
    
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert YAML files to JSON files")
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('-f', '--file', type=str, help="Path to the YAML file")
    group.add_argument('-d', '--directory', type=str, help="Path to the directory containing YAML files")
    parser.add_argument('-i', '--infer_output', action='store_true', help="Infer output path from input file path")
    parser.add_argument('-o', '--output', type=str, help="Path to the output JSON file (optional)")
    
    args = parser.parse_args()
    
    if args.file:
        if args.infer_output:
            output_path = args.file.rsplit('.', 1)[0] + '.json'
        else:
            output_path = args.output
        yaml_to_json(args.file, output_path)
    else:
        yaml_to_json_in_folder(args.directory)