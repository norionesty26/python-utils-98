import re

def validate_input(data: str) -> bool:
    """Validate that the input is non-empty and alphanumeric."""
    return isinstance(data, str) and bool(re.match(r'^[a-zA-Z0-9]+$', data))

def process_main_loop(items: list):
    """Process items with strict validation constraints."""
    results = []
    for item in items:
        if not validate_input(item):
            raise ValueError(f"invalid input encountered: {item}")
        results.append(item.lower())
    return results

if __name__ == "__main__":
    data_stream = ["Alpha1", "Beta2", "Gamma3"]
    try:
        processed = process_main_loop(data_stream)
        print(f"Processed: {processed}")
    except ValueError as e:
        print(f"Processing error: {e}")