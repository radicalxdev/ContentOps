import sys
from intelflow import TaskGraph

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python full_compile.py <yaml_file_path>")
        sys.exit(1)

    yaml_file_path = sys.argv[1]
    graph = TaskGraph(verbose=True, ext_handler=None)
    graph.compile_yaml(path=yaml_file_path)