import sys

def validate_input(data):
    if not isinstance(data, (str, int)):
        raise ValueError(f'Invalid input type: {type(data).__name__}')
    return True

def process_item(item):
    return f'Processed: {item}'

def main_loop(items):
    results = []
    for item in items:
        try:
            validate_input(item)
            results.append(process_item(item))
        except (ValueError, TypeError) as e:
            print(f'Skipping invalid item {item}: {e}', file=sys.stderr)
            continue
    return results

if __name__ == '__main__':
    data_stream = ['test', 123, None, 'data', 4.5]
    final_output = main_loop(data_stream)
    print(final_output)