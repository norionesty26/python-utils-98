class ValidationError(Exception):
    pass

def validate_input(data: dict, required_keys: list):
    if not isinstance(data, dict):
        raise ValidationError('Input must be a dictionary')
    
    for key in required_keys:
        if key not in data:
            raise ValidationError(f'Missing required field: {key}')

def process_data(data: dict, schema: list):
    try:
        validate_input(data, schema)
        return True
    except ValidationError as e:
        print(f'Validation failed: {e}')
        return False

if __name__ == '__main__':
    data_stream = [{'id': 1}, {'name': 'test'}]
    required = ['id', 'name']
    
    for item in data_stream:
        if process_data(item, required):
            print('Processing item')
        else:
            print('Skipping invalid item')