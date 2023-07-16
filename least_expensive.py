import json

def least_expensive(file_path: str) -> str:
    """
    get least expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: least expensive item
    """
    main = open('data.json')
    f = json.load(main)
    a = f['food']
    for i in f.values():
        if a > i:
            m = i
    return m 

# test
file_path = "data.json"
least_expensive_item = least_expensive(file_path)
print(least_expensive_item)
