import json

def get_data(file_path: str) -> dict:
    """
    get data from json file as dictionary
    
    Args:
        file_path (str): path to json file

    Returns:
        dict: dictionary of data
    """
    main = open('data.json')
    f = json.load(main)
    return f

# test
file_path = "data.json"
data = get_data(file_path)
print(data)
