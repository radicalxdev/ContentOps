import yaml
import os
import argparse

def list_edges(file_path):
    if not os.path.exists(file_path):
        print(f"File {file_path} does not exist.")
        return
    
    with open(file_path, 'r') as f:
        try:
            content = yaml.safe_load(f)
            
            if isinstance(content, dict):
                for task in content.get('tasks'):
                    if 'nodes' in task:
                        for node in task.get('nodes'):
                            if 'edges' in node:
                                for edge in node.get('edges'):
                                    print(f"Option Intent: {edge.get('text')}")
                                    print(f"Option Name: {edge.get('target_node_id')}\n")
        
        except yaml.YAMLError as exc:
            print(f"Error occurred while reading file: {exc}")

# Create parser
parser = argparse.ArgumentParser(description='List edges in a YAML file')

parser.add_argument('Path', metavar='path', type=str, help='Path to the YAML file')

args = parser.parse_args()

list_edges(args.Path)