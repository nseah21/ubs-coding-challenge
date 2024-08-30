import json

def read_json(file_path):
    """
    Reads a JSON file and returns the data.
    
    :param file_path: str - Path to the input JSON file.
    :return: dict - Parsed JSON data.
    """
    with open(file_path, 'r') as f:
        data = json.load(f)
    return data

def process_data(data):
    """
    Processes the data read from the JSON file.
    
    :param data: dict - JSON data to process.
    :return: None
    """
    print(data)

if __name__ == "__main__":
    input_file = 'input.json'  # You can change the file path if needed
    json_data = read_json(input_file)
    process_data(json_data)
