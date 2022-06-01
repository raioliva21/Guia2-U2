import json

def open_file(file):

    try:
        with open(file, 'r') as fichero:
            data = json.load(fichero)
    except IOError:
        data = []
    
    return data

# se añade data en archivo json
def save_data(data, file):

    with open(file, "w") as fichero:
        json.dump(data, fichero, indent=4)