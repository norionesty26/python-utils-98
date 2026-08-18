def optimized_function(data):
    unique_data = set(data)
    processed_data = [process_item(item) for item in unique_data]
    return processed_data

def process_item(item):
    # Assumed processing logic
    return item ** 2

if __name__ == '__main__':
    sample_data = [1, 2, 2, 3, 4, 4, 5]
    result = optimized_function(sample_data)
    print(result)