def relational_projection(source_data, selected_fields):
    """
    Performs a relational projection, copying selected fields from source.

    Args:
    - source_data (list of dict): The source dataset to project.
    - selected_fields (list of str): The fields to select.
    
    Returns:
    - list of dict: A new dataset containing only the selected fields.
    """
    projected_data = []
    
    for record in source_data:
        projected_record = {field: record[field] for field in selected_fields if field in record}
        projected_data.append(projected_record)
    
    return projected_data

# Example usage:
source_data = [
    {'name': 'Alice', 'age': 30, 'city': 'New York'},
    {'name': 'Bob', 'age': 25, 'city': 'Los Angeles'},
    {'name': 'Charlie', 'age': 35, 'city': 'Chicago'}
]

selected_fields = ['name', 'city']

projected_data = relational_projection(source_data, selected_fields)

print(projected_data)
# Output: [{'name': 'Alice', 'city': 'New York'}, {'name': 'Bob', 'city': 'Los Angeles'}, {'name': 'Charlie', 'city': 'Chicago'}]
