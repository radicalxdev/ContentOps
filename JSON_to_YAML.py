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

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert JSON to YAML")
    parser.add_argument("json_file_path", type=str, help="Path to the JSON file")
    parser.add_argument("yaml_file_path", type=str, help="Path to the YAML file")
    args = parser.parse_args()
    json_to_yaml(args.json_file_path, args.yaml_file_path)