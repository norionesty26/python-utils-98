import sys

def validate_input(data):
    if not isinstance(data, (int, float)):
        raise ValueError(f'Invalid input type: {type(data).__name__}')
    if not (0 <= data <= 100):
        raise ValueError('Input out of allowed range 0-100')
    return True

def process_value(val):
    return val * 2

def run_loop():
    inputs = [10, 50, 105, 'error', 25]
    results = []
    for item in inputs:
        try:
            validate_input(item)
            results.append(process_value(item))
        except (ValueError, TypeError) as e:
            print(f'Skipping invalid input {item}: {e}', file=sys.stderr)
    return results

if __name__ == '__main__':
    data_output = run_loop()
    print(f'Processed: {data_output}')