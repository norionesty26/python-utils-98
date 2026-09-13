import sys

def validate_input(data):
    if not isinstance(data, dict):
        raise ValueError("input must be a dictionary")
    if "key" not in data or not isinstance(data["key"], str):
        raise ValueError("missing or invalid key in data")
    return True

def process_stream(data_stream):
    for item in data_stream:
        try:
            if validate_input(item):
                print(f"Processing: {item['key']}")
        except (ValueError, TypeError) as e:
            print(f"Skipping invalid entry: {e}", file=sys.stderr)

if __name__ == "__main__":
    sample_data = [{"key": "val1"}, {"wrong": "data"}, {"key": "val2"}]
    process_stream(sample_data)