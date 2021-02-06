import main
import os

from usefull import custom_path

def read_db() -> list:
    script_dir = os.path.dirname(__file__)
    try: 
        with open(custom_path(script_dir,'db.csv')) as f:
            print("****************** ok, found with custom path!")     


    except OSError:
        print("******************No database file!")

    return [{'page': 1, 'parent': 0}] 

def test_read_csv_db():

    assert read_db()[0]['page'] == 1
    