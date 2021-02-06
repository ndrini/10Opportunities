import main
import os
import csv

from usefull import guess_type


def read_db(file_name) -> list:
    result = []
    try:
        with open(os.path.dirname(__file__) + '/../' + file_name) as f:
            reader = csv.DictReader(f)
            for line in reader:
                print("Not typed data\t: ", line)
                for key in line:
                    line[key] = guess_type(line[key])
                result.append(line)
                print("Typed data\t: ", line)

    except OSError:
        print("\t*** No database file!")

    return result


def test_read_csv_db_simple():
    '''
    [{'page': 1, 'msg': "1. Mi sembra che", 'parent': 0,
    'level': 'S1', 'label': 1, 'choice': False, 'end': False},
    {'page': 2, 'msg': '...se ti trovassi', 'parent': 1,
    'level': 'S1_2', 'label': 'A', 'choice': True, 'end': False}, ... ]

    page	msg	parent	choice	end
    1	1. Mi sembra che	0	False	False
    2	...se ti trovassi	1	True	False
    '''
    assert read_db('db_simple.csv')[0]['page'] == 1


def test_read_real_db():
    assert len(read_db('db.csv')) == 167
