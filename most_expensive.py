import json

def most_expensive(file_path: str) -> str:
    """
    get most expensive item from json file
    
    Args:
        file_path (str): path to json file

    Returns:
        str: most expensive item
    """
    main = open('data.json')
    f = json.load(main)
    a = 100000000000
    for i in f.values():
        if a > i:
            m = i
    return m 

# test
file_path = "data.json"
most_expensive_item = most_expensive(file_path)
print(most_expensive_item)