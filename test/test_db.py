from usefull import read_db


def test_read_csv_db_simple():
    '''
    page	msg	                parent	choice	end
    1	    1. Mi sembra che	0	    False	False
    2	    ...se ti trovassi	1	    True	False
    '''
    assert read_db('db_simple.csv')[0]['page'] == 1
    assert read_db('db_simple.csv')[0]['msg'][-3:] == 'che'
    assert read_db('db_simple.csv')[1]['msg'][:9] == '...se ti '
    assert read_db('db_simple.csv')[0]['end'] == False

def test_read_real_db():
    assert len(read_db('db.csv')) == 167
