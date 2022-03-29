import os 
from os import path as ps
import pathlib


#this function takes in a source path and moves all the files onto a destination path, if decorated the function moves
#all the python files in the projects directory and the jupyternotebooks onto the onedrive learningpython folder
#however the inputs most be strings and add onto the base path r'C:\Users\Uchek

def learning_python(f):
    def wrapper(*args,**kwargs):
        base_path = os.path.expanduser('~')
        decorated_functions = f(*args,**kwargs)
        documents_path = os.path.join(base_path, r'OneDrive\Documents\Projects')
        destination_directory = os.listdir(documents_path)
        for items in destination_directory:
            try:
                if items.endswith(".ipynb"):
                    print(items)
                    py_file_in_destination = ps.join(documents_path, items)
                    learningpython_path = ps.join(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython', items)
                    os.rename(py_file_in_destination, learningpython_path)
                elif items.endswith('.py'):
                    print(items)
                    py_file_in_destination = ps.join(documents_path, items)
                    learningpython_path = ps.join(r'C:\Users\Uchek\OneDrive\Documents\Projects\learningpython', items)
                    os.rename(py_file_in_destination, learningpython_path)
                else:
                    print('not a python file nor a juyter notebook')
            except FileExistsError:
                print('there are no files in the destination folder that should be on the learningpython folder')
        print('function has been decorated')
        return decorated_functions
    return wrapper


@learning_python
def clutter_free(source_path, destination_path):
    base_path = os.path.expanduser('~')
    downloads_path = os.path.join(base_path, source_path)
    downloads_files = os.listdir(downloads_path)
    documents_path = os.path.join(base_path, destination_path)
    try:
        for file in downloads_files:
            source = ps.join(downloads_path, file)
            destination = ps.join(documents_path, file) 
            os.rename(source, destination)
    except FileExistsError:
        file_to_remove = pathlib.Path(destination)
        file_to_remove.unlink()
    except PermissionError:
        pass
    
    destination_directory = os.listdir(documents_path)
    if not os.path.isdir(documents_path):
        os.mkdir(documents_path)
    for item in downloads_files:
        if item not in destination_directory:
            print(item)








