import json
import os



def read_json(file_name):
    base_path = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(base_path, "test_data", file_name)
    with open(file_path, "r") as f:
        return json.load(f)
