import yaml
import json
import os
import argparse

def yaml_to_json_in_folder(folder_path):
    try:
        # List all files in the specified folder
        files = os.listdir(folder_path)
        
        # Filter out only YAML files
        yaml_files = [file for file in files if file.endswith('.yaml') or file.endswith('.yml')]
        
        for yaml_file in yaml_files:
            yaml_file_path = os.path.join(folder_path, yaml_file)
            json_file_path = os.path.join(folder_path, yaml_file.rsplit('.', 1)[0] + '.json')
            
            # Load the YAML file
            with open(yaml_file_path, 'r') as yf:
                yaml_content = yaml.safe_load(yf)
            
            # Write the content to a JSON file
            with open(json_file_path, 'w') as jf:
                json.dump(yaml_content, jf, indent=4)
            
            print(f"Successfully converted {yaml_file_path} to {json_file_path}")
    
    except Exception as e:
        print(f"Error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert all YAML files in a folder to JSON files")
    parser.add_argument('folder_path', type=str, help="Path to the folder containing YAML files")
    
    args = parser.parse_args()
    yaml_to_json_in_folder(args.folder_path)
